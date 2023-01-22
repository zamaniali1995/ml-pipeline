create-env:
	@echo "---- Creating Conda Env ----"
	@conda env create -f ./environment.yaml

delete-env:
	@echo "---- Deleting Conda Env ----"
	@conda env delete --name test-env

acquire-date:
	@echo "---- Acquiring Data ----"
	@python3 pipeline-steps/1_data_acquisition/main.py
