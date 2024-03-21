# wine
- conda activate C:\Users\mahesh\Desktop\project\wine\wine1
- setup.py
- requirements (pip install - r requirements.txt)
- logging

#### data_ingestion, data_validation (for checking data is correct o not), data_transformation(for feature engineeering), model_trainer(train the model), model_evaluation

##### Workflows
- update config.yaml
- update schema.yaml   (for checking data-type, mention target column name)
- update params.yaml   (for mentioning required parameter for algorithm)
- update the entity     (it is a return type of our-fuction)
- update the configuration manager in src config
- update the components
- update the pipeline
- update the main.py
- update the app.py

#### DVC 
- dvc init
- git add .
- git status
- git commit -m "dvc track"
- dvc add artifacts\data_ingestion\raw.csv
#### ERROR
- delete the artifacts
- git add .
- git commit -m "git untrack"
- git push origin main
- dvc add artifacts/data_ingestion/raw.csv
- git add artifacts/data_ingestion/.gitignore 
- git add artifacts/data_ingestion/raw.csv.dvc
- git commit -m "git dvc track"
- git push origin main
- git status
- git commit -m "changes in data"
