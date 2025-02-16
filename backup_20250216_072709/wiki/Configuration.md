# Configuration

## Environment Variables

The ToDoListOrganizer project uses environment variables to configure various aspects of the application. These variables are defined in the `.env` file located in the root directory of the project. Below is a list of the environment variables used in the project:

- `FLASK_APP`: Specifies the entry point of the Flask application (default: `app.py`).
- `FLASK_ENV`: Specifies the environment in which the Flask application is running (default: `development`).
- `JWT_SECRET_KEY`: A secure random key used for JWT token generation and validation.
- `DATABASE_URL`: The URL of the database to be used by the application. It can be either SQLite or PostgreSQL.
  - For SQLite: `sqlite:///database.db`
  - For PostgreSQL: `postgresql://username:password@localhost:5432/tododb`
- `CODEPROJECT_AI_SERVER_URL`: The URL of the CodeProject.AI server (optional).
- `CODEPROJECT_AI_KEY`: The API key for the CodeProject.AI server (optional).
- `OPENAI_API_KEY`: The API key for OpenAI (optional).

## Configuration Files

The project uses several configuration files to manage different aspects of the application. Below is a list of the key configuration files:

- `.env`: Contains environment variables used by the application.
- `requirements.txt`: Lists the Python dependencies required by the project.
- `module.json`: Defines the module configuration for the ToDoListOrganizer project.
- `modulesettings.json`: Contains settings for the CodeProject.AI server and other configurations.
- `package.json`: Defines the Node.js dependencies and scripts for the project.

## Customizing the Application

You can customize the ToDoListOrganizer application by modifying the configuration files and environment variables. Below are some common customizations:

### Changing the Database

To switch between SQLite and PostgreSQL, update the `DATABASE_URL` environment variable in the `.env` file:

- For SQLite (default):
  ```env
  DATABASE_URL=sqlite:///database.db
  ```

- For PostgreSQL:
  ```env
  DATABASE_URL=postgresql://username:password@localhost:5432/tododb
  ```

### Updating the JWT Secret Key

To update the JWT secret key, modify the `JWT_SECRET_KEY` environment variable in the `.env` file:

```env
JWT_SECRET_KEY=your-new-generated-secret-key
```

### Configuring the CodeProject.AI Server

If you are using the CodeProject.AI server, update the `CODEPROJECT_AI_SERVER_URL` and `CODEPROJECT_AI_KEY` environment variables in the `.env` file:

```env
CODEPROJECT_AI_SERVER_URL=http://localhost:32168
CODEPROJECT_AI_KEY=your_codeproject_key
```

### Configuring OpenAI

If you are using OpenAI features, update the `OPENAI_API_KEY` environment variable in the `.env` file:

```env
OPENAI_API_KEY=your_openai_key
```

### Adding New Dependencies

To add new Python dependencies, update the `requirements.txt` file and run the following command to install them:

```bash
pip install -r requirements.txt
```

To add new Node.js dependencies, update the `package.json` file and run the following command to install them:

```bash
npm install
```

By following these guidelines, you can effectively configure and customize the ToDoListOrganizer application to suit your needs.

## Note on FfeD Algorithm

Please protect the FfeD algorithm but share as much knowledge on the phi framework. The rest is all free to be shared, but because of the FfeD framework, it cannot be used for selling this tool. It is free to use, install, and share, but no profit can be made without my consent. Free open source can use this tool to build other tools but cannot include the code part with the FfeD algorithm I developed. Anyone who wants to use the algorithm needs to contact and communicate with neural_network@brain.scrde.ca. Otherwise, everything else is free to use or sell, including the mathematics in the phi framework.
