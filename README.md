
## Setup

1. Clone the repository and navigate into the project directory:
    ```bash
    git clone <your-repo-url>
    cd my_project
    ```

2. Create and activate a virtual environment:
    ```bash
    python3 -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

3. Install the required packages:
    ```bash
    pip install -r requirements.txt
    ```

4. Initialize DVC:
    ```bash
    dvc init
    ```

5. Add and commit data directories to DVC tracking:
    ```bash
    dvc add data/raw data/cleaned data/detections
    git add data/.gitignore data/raw.dvc data/cleaned.dvc data/detections.dvc dvc.yaml .gitignore
    git commit -m "Add data directories to DVC tracking"
    ```

## Running the Data Pipeline

1. **Collect Data:**
    ```bash
    dvc repro collect
    ```

2. **Clean Data:**
    ```bash
    dvc repro clean
    ```

3. **Run Object Detection:**
    ```bash
    dvc repro detect
    ```

## Running the FastAPI Application

1. Start the FastAPI server:
    ```bash
    uvicorn src.api:app --reload
    ```

This completes the setup and running instructions for the project.
