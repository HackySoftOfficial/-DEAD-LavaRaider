import logging
import colorlog
from flask import Flask, request, jsonify, send_from_directory
import mysql.connector
from mysql.connector import Error
import os

# Set up colored logging
formatter = colorlog.ColoredFormatter(
    '%(asctime)s - %(log_color)s%(levelname)s%(reset)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S',
    log_colors={
        'DEBUG': 'cyan',
        'INFO': 'green',
        'WARNING': 'yellow',
        'ERROR': 'red',
        'CRITICAL': 'bold_red',
    }
)

handler = logging.StreamHandler()
handler.setFormatter(formatter)

logger = logging.getLogger()
logger.setLevel(logging.INFO)
logger.addHandler(handler)

app = Flask(__name__)

def create_connection():
    try:
        connection = mysql.connector.connect(
            host='185.197.74.254',
            user='Lavapi',
            password='8gFi8NB8b75rR0dM8IxoQefInwJqiQA3FpJ6z08Q9AzLU3TIxv',
            database='lava_eula',
            port=3306
        )
        if connection.is_connected():
            logger.info('Database connection established.')
            return connection
    except Error as e:
        logger.error(f"Database connection error: {e}")
        return None

@app.route('/key', methods=['POST'])
def validate_license_key():
    data = request.get_json()
    if not data:
        logger.warning('No data provided in request.')
        return jsonify({'valid': False, 'error': 'No data provided'}), 400

    license_key = data.get('key')
    hwid = data.get('hwid')

    if not isinstance(license_key, str) or not isinstance(hwid, str):
        logger.warning('Invalid data type for license key or HWID.')
        return jsonify({'valid': False, 'error': 'License key and HWID must be strings'}), 400

    if not license_key and not hwid:
        logger.warning('Both license key and HWID are missing in request data.')
        return jsonify({'valid': False, 'error': 'License key and HWID are required'}), 400
    if not license_key:
        logger.warning('License key is missing in request data.')
        return jsonify({'valid': False, 'error': 'License key is required'}), 400
    if not hwid:
        logger.warning('HWID is missing in request data.')
        return jsonify({'valid': False, 'error': 'HWID is required'}), 400

    user_agent = request.headers.get('User-Agent')
    lava_version = request.headers.get('LavaVersion')

    if user_agent != 'LavaRaider':
        logger.warning(f'Invalid User-Agent: {user_agent}')
        return jsonify({'valid': False, 'error': 'Invalid User-Agent'}), 400

    connection = create_connection()
    if connection is None:
        return jsonify({'valid': False, 'error': 'Database connection failed'}), 500

    try:
        cursor = connection.cursor(dictionary=True)
        query = '''
        SELECT COUNT(*) AS count 
        FROM license_keys 
        WHERE `license_key` = %s AND `hwid` = %s
        '''
        cursor.execute(query, (license_key, hwid))
        result = cursor.fetchone()
        if result['count'] > 0:
            is_valid = True
        else:
            is_valid = False
            # Further refine which part is invalid
            query_check_key = '''
            SELECT COUNT(*) AS count 
            FROM license_keys 
            WHERE `license_key` = %s
            '''
            cursor.execute(query_check_key, (license_key,))
            key_result = cursor.fetchone()
            
            query_check_hwid = '''
            SELECT COUNT(*) AS count 
            FROM license_keys 
            WHERE `hwid` = %s
            '''
            cursor.execute(query_check_hwid, (hwid,))
            hwid_result = cursor.fetchone()

            if key_result['count'] == 0 and hwid_result['count'] == 0:
                error_msg = 'Both license key and HWID are invalid'
            elif key_result['count'] == 0:
                error_msg = 'License key is invalid'
            elif hwid_result['count'] == 0:
                error_msg = 'HWID is invalid'
            else:
                error_msg = 'Unknown error'
        
        if is_valid:
            logger.info('License key and HWID validation result: True')
            return jsonify({'valid': True})
        else:
            logger.warning(f'License key and HWID validation result: False. Error: {error_msg}')
            return jsonify({'valid': False, 'error': error_msg}), 400

    except Error as e:
        logger.error(f"Database query error: {e}")
        return jsonify({'valid': False, 'error': str(e)}), 500

    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            logger.info('Database connection closed.')

@app.route('/versions', methods=['GET'])
def list_versions():
    # Read the versions from the file
    with open('versions.txt') as file:
        versions = file.read().splitlines()
    
    # Convert the versions to the desired JSON format
    return jsonify({'versions': sorted(versions)})

@app.route('/versions/<path:filename>', methods=['GET'])
def get_version_file(filename):
    versions_dir = 'versions'  # Directory where your version files are stored
    
    # Check if the file exists in the directory
    file_path = os.path.join(versions_dir, filename)
    if os.path.exists(file_path):
        return send_from_directory(versions_dir, filename + ".exe")
    else:
        return jsonify({"error": "File not found"}), 404

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
