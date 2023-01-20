create-env:
	echo "---- Creating Conda Env ----" 
	conda env create -f ./environment.yaml

delete-env:
	echo "---- Deleting Conda Env ----" 
	conda env delete --name test-env