from dotenv import load_dotenv
import os


def copy_env_example():

    if not os.path.exists('.env'):
        print("'.env' file not found. Creating it from '.env.example'...")
        with open('.env.example', 'r') as example_file:
            content = example_file.read()
        
        with open('.env', 'w') as env_file:
            env_file.write(content)
        print("'.env' file created from '.env.example'. Please update it with your environment variables.")

def load_env_var(varname:str)->str:
    """
    Load an environment variable from the .env file.
    
    Args:
        varname (str): The name of the environment variable to load.
        
    Returns:
        str: The value of the environment variable.
    """

    copy_env_example()

    load_dotenv()
    try:
        return os.environ[varname]
    except KeyError:
        raise RuntimeError(f"Environment variable '{varname}' not found. Please check your .env file.")


TIME_BETWEEN_REQUESTS = int(load_env_var('TIME_BETWEEN_REQUESTS'))
TOKEN_OLHO_VIVO = load_env_var('TOKEN_OLHO_VIVO')
DB_STRING = load_env_var('DB_STRING')