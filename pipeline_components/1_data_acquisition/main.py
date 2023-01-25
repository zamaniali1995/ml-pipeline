"""
The file should implement data acquisition pipeline.
It should load the raw data from any data source and save it.
"""
from typing import List

from src.utils import Log, load_yaml, parse_arguments, write_parquet
from src.data.acquisition.utils import load_data



def main(arguments_list: List = None):
    """Main method"""
    arguments = parse_arguments(arguments_list=arguments_list)
    config = load_yaml(arguments.config_path)
    main_config = load_yaml(arguments.main_config_path)

    Log.info(main_config.log_msg.acquire_data_start_msg)

    Log.info(main_config.log_msg.load_dataset_start_msg)
    dataset_df = load_data(target_column=main_config.target_column)
    Log.info(main_config.log_msg.load_dataset_end_msg)

    Log.info(main_config.log_msg.save_dataset_start_msg)
    write_parquet(df=dataset_df, path=main_config.path.raw_data_path)
    Log.info(main_config.log_msg.save_dataset_end_msg)

    Log.info(main_config.log_msg.acquire_data_end_msg)


if __name__ == '__main__':
    main()
