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
	@python3 pipeline_components/1_data_acquisition/main.py
