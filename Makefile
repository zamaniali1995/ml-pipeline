create-env:
	@echo "---- Creating Conda Env ----"
	@conda env create -f ./environment.yaml

delete-env:
	@echo "---- Deleting Conda Env ----"
	@conda env delete --name test-env

create-package:
	@echo "---- Creating a package ----"
	@pip3 install -e .

acquire-date:
	@echo "---- Acquiring Data ----"
	@python3 pipeline_components/1_data_acquisition/main.py \
		--config_path=./config/data_acquisition/config.yaml \
		--main_config_path=./config/config.yaml

process-date:
	@echo "---- Processing Data ----"
	@python3 pipeline_components/2_data_processing/main.py \
		--config_path=./config/data_processing/config.yaml \
		--main_config_path=./config/config.yaml

train-model:
	@echo "---- Training Model ----"
	@python3 pipeline_components/3_model_training/main.py \
		--config_path=./config/model_training/config.yaml \
		--main_config_path=./config/config.yaml

evaluate-model:
	@echo "---- Evaluating Model ----"
	@python3 pipeline_components/4_model_validation/main.py \
		--config_path=./config/model_validation/config.yaml \
		--main_config_path=./config/config.yaml

run-server:
	@echo "---- Running Server ----"
	@python3 app/run.py \
		--main_config_path=./config/config.yaml
