import os
import warnings
warnings.filterwarnings("ignore")

# #############################################
# # BenchMark Bike
# # #############################################
bike_shared_params_st_mgcn = ('python ST_MGCN_Obj.py '
                         '--Dataset Bike '
                         '--CT 6 '
                         '--PT 7 '
                         '--TT 4 '
                         '--K 1 '
                         '--L 1 '
                         '--Graph Distance-Correlation-Interaction '
                         '--LSTMUnits 64 '
                         '--LSTMLayers 3 '
                         '--DataRange All '
                         '--TrainDays 365 '
                         '--threshold_correlation 0 '
                         '--threshold_distance 1000 '
                         '--threshold_interaction 500 '
                         '--Epoch 10000 '
                         '--Train True '
                         '--lr 5e-4 '
                         '--patience 0.1 '
                         '--ESlength 100 '
                         '--BatchSize 16 '
                         '--MergeWay sum '
                         )

os.system(bike_shared_params_st_mgcn + ' --City Chicago --external_method not-not-not '
                                      '  --DataRange 0.5 --TrainDays 183 --MergeIndex 6 --CodeVersion no_context_30 ')

os.system(bike_shared_params_st_mgcn + ' --City Chicago --external_method not-not-concat '
                                      '  --DataRange 0.5 --TrainDays 183 --MergeIndex 6 --CodeVersion not_not_concat_30 ')

os.system(bike_shared_params_st_mgcn + ' --City Chicago --external_method emb-not-concat '
                                      '  --DataRange 0.5 --TrainDays 183 --MergeIndex 6 --CodeVersion emb_not_concat_30 ')

os.system(bike_shared_params_st_mgcn + ' --City Chicago --external_method multi-not-concat '
                                      '  --DataRange 0.5 --TrainDays 183 --MergeIndex 6 --CodeVersion multi_not_concat_30 ')

os.system(bike_shared_params_st_mgcn + ' --City Chicago --external_method not-linear-add '
                                      '  --DataRange 0.5 --TrainDays 183 --MergeIndex 6 --CodeVersion not_linear_add_30 ')

os.system(bike_shared_params_st_mgcn + ' --City Chicago --external_method not-linear-gating '
                                      '  --DataRange 0.5 --TrainDays 183 --MergeIndex 6 --CodeVersion not_linear_gating_30 ')

os.system(bike_shared_params_st_mgcn + ' --City Chicago --external_lstm_len 4 --external_method lstm-linear-add '
                                      '  --DataRange 0.5 --TrainDays 183 --MergeIndex 6 --CodeVersion lstm_linear_add_30 ')

os.system(bike_shared_params_st_mgcn + ' --City Chicago --external_method emb-linear-add '
                                      '  --DataRange 0.5 --TrainDays 183 --MergeIndex 6 --CodeVersion emb_linear_add_30')

os.system(bike_shared_params_st_mgcn + ' --City Chicago --external_method emb-linear-gating '
                                      '  --DataRange 0.5 --TrainDays 183 --MergeIndex 6 --CodeVersion emb_linear_gating_30 ')

os.system(bike_shared_params_st_mgcn + ' --City Chicago --external_method multi-linear-add '
                                      '  --DataRange 0.5 --TrainDays 183 --MergeIndex 6 --CodeVersion multi_linear_add_30 ')

os.system(bike_shared_params_st_mgcn + ' --City Chicago --external_method multi-linear-gating '
                                      '  --DataRange 0.5 --TrainDays 183 --MergeIndex 6 --CodeVersion multi_linear_gating_30 ')

os.system(bike_shared_params_st_mgcn + ' --City Chicago --external_lstm_len 4 --external_method lstm-not-concat '
                                      '  --DataRange 0.5 --TrainDays 183 --MergeIndex 6 --CodeVersion lstm4_not_concat_30 ')

os.system(bike_shared_params_st_mgcn + ' --City Chicago --external_lstm_len 4 --external_method lstm-linear-gating '
                                      '  --DataRange 0.5 --TrainDays 183 --MergeIndex 6 --CodeVersion lstm4_linear_gating_30 ')

os.system(bike_shared_params_st_mgcn + ' --City Chicago --external_method earlyconcat '
                                      '  --DataRange 0.5 --TrainDays 183 --MergeIndex 6 --CodeVersion earlyconcat_30 ')

os.system(bike_shared_params_st_mgcn + ' --City Chicago --external_method earlyadd '
                                      '  --DataRange 0.5 --TrainDays 183 --MergeIndex 6 --CodeVersion earlyadd_30 ')



# # ###############################################
# # BenchMark Metro
# ###############################################

metro_shared_params_st_mgcn = ('python ST_MGCN_Obj.py '
                         '--Dataset Metro '
                         '--CT 6 '
                         '--PT 7 '
                         '--TT 4 '
                         '--K 1 '
                         '--L 1 '
                         '--Graph Distance-Correlation-Line '
                         '--LSTMUnits 64 '
                         '--LSTMLayers 3 '
                         '--DataRange All '
                         '--TrainDays All '
                         '--threshold_correlation 0.7 '
                         '--threshold_distance 5000 '
                         '--threshold_interaction 30 '
                         '--Epoch 10000 '
                         '--Train True '
                         '--lr 1e-4 '
                         '--patience 0.1 '
                         '--ESlength 100 '
                         '--BatchSize 16 '
                         '--MergeWay sum '
                         )

os.system(metro_shared_params_st_mgcn + ' --City Shanghai --external_method not-not-not '
                                      '  --MergeIndex 6 --CodeVersion no_context_30 ')

os.system(metro_shared_params_st_mgcn + ' --City Shanghai --external_method not-not-concat '
                                      '  --MergeIndex 6 --CodeVersion not_not_concat_30 ')

os.system(metro_shared_params_st_mgcn + ' --City Shanghai --external_method emb-not-concat '
                                      '  --MergeIndex 6 --CodeVersion emb_not_concat_30 ')

os.system(metro_shared_params_st_mgcn + ' --City Shanghai --external_method multi-not-concat '
                                      '  --MergeIndex 6 --CodeVersion multi_not_concat_30 ')

os.system(metro_shared_params_st_mgcn + ' --City Shanghai --external_method not-linear-add '
                                      '  --MergeIndex 6 --CodeVersion not_linear_add_30 ')

os.system(metro_shared_params_st_mgcn + ' --City Shanghai --external_method not-linear-gating '
                                      '  --MergeIndex 6 --CodeVersion not_linear_gating_30 ')

os.system(metro_shared_params_st_mgcn + ' --City Shanghai --external_lstm_len 4 --external_method lstm-linear-add '
                                      '  --MergeIndex 6 --CodeVersion lstm_linear_add_30 ')

os.system(metro_shared_params_st_mgcn + ' --City Shanghai --external_method emb-linear-add '
                                      '  --MergeIndex 6 --CodeVersion emb_linear_add_30 ')

os.system(metro_shared_params_st_mgcn + ' --City Shanghai --external_method emb-linear-gating '
                                      '  --MergeIndex 6 --CodeVersion emb_linear_gating_30 ')


os.system(metro_shared_params_st_mgcn + ' --City Shanghai --external_method multi-linear-add '
                                      '  --MergeIndex 6 --CodeVersion multi_linear_add_30 ')

os.system(metro_shared_params_st_mgcn + ' --City Shanghai --external_method multi-linear-gating '
                                      '  --MergeIndex 6 --CodeVersion multi_linear_gating_30 ')

os.system(metro_shared_params_st_mgcn + ' --City Shanghai --external_lstm_len 4 --external_method lstm-not-concat '
                                      '  --MergeIndex 6 --CodeVersion lstm4_not_concat_30 ')

os.system(metro_shared_params_st_mgcn + ' --City Shanghai --external_lstm_len 4 --external_method lstm-linear-gating '
                                      '  --MergeIndex 6 --CodeVersion lstm4_linear_gating_30 ')

os.system(metro_shared_params_st_mgcn + ' --City Shanghai --external_method earlyconcat '
                                      '  --MergeIndex 6 --CodeVersion earlyconcat_30 ')

os.system(metro_shared_params_st_mgcn + ' --City Shanghai --external_method earlyadd '
                                      '  --MergeIndex 6 --CodeVersion earlyadd_30 ')


# # ###############################################
# # # BenchMark ChargeStation
# # ###############################################
cs_shared_params_st_mgcn = ('python ST_MGCN_Obj.py '
                         '--Dataset ChargeStation '
                         '--CT 6 '
                         '--PT 7 '
                         '--TT 4 '
                         '--K 1 '
                         '--L 1 '
                         '--Graph Distance-Correlation '
                         '--LSTMUnits 64 '
                         '--LSTMLayers 3 '
                         '--DataRange All '
                         '--TrainDays All '
                         '--threshold_correlation 0.1 '
                         '--threshold_distance 1000 '
                         '--threshold_interaction 500 '
                         '--Epoch 10000 '
                         '--Train True '
                         '--lr 5e-4 '
                         '--patience 0.1 '
                         '--ESlength 100 '
                         '--BatchSize 16 '
                         '--MergeWay max '
                         )

os.system(cs_shared_params_st_mgcn + ' --City Beijing --external_method not-not-not '
                                      '  --MergeIndex 1 --CodeVersion no_context_30 ')

os.system(cs_shared_params_st_mgcn + ' --City Beijing --external_method not-not-concat '
                                      '  --MergeIndex 1 --CodeVersion not_not_concat_30 ')

os.system(cs_shared_params_st_mgcn + ' --City Beijing --external_method emb-not-concat '
                                      '  --MergeIndex 1 --CodeVersion emb_not_concat_30 ')

os.system(cs_shared_params_st_mgcn + ' --City Beijing --external_method multi-not-concat '
                                      '  --MergeIndex 1 --CodeVersion multi_not_concat_30 ')

os.system(cs_shared_params_st_mgcn + ' --City Beijing --external_method not-linear-add '
                                      '  --MergeIndex 1 --CodeVersion not_linear_add_30 ')

os.system(cs_shared_params_st_mgcn + ' --City Beijing --external_method not-linear-gating '
                                      '  --MergeIndex 1 --CodeVersion not_linear_gating_30 ')

os.system(cs_shared_params_st_mgcn + ' --City Beijing --external_lstm_len 4 --external_method lstm-linear-add '
                                      '  --MergeIndex 1 --CodeVersion lstm_linear_add_30 ')

os.system(cs_shared_params_st_mgcn + ' --City Beijing --external_method emb-linear-add '
                                      '  --MergeIndex 1 --CodeVersion emb_linear_add_30 ')

os.system(cs_shared_params_st_mgcn + ' --City Beijing --external_method emb-linear-gating '
                                      '  --MergeIndex 1 --CodeVersion emb_linear_gating_30 ')

os.system(cs_shared_params_st_mgcn + ' --City Beijing --external_method multi-linear-add '
                                      '  --MergeIndex 1 --CodeVersion multi_linear_add_30 ')

os.system(cs_shared_params_st_mgcn + ' --City Beijing --external_method multi-linear-gating '
                                      '  --MergeIndex 1 --CodeVersion multi_linear_gating_30 ')

os.system(cs_shared_params_st_mgcn + ' --City Beijing --external_lstm_len 4 --external_method lstm-not-concat '
                                      '  --MergeIndex 1 --CodeVersion lstm4_not_concat_30 ')

os.system(cs_shared_params_st_mgcn + ' --City Beijing --external_lstm_len 4 --external_method lstm-linear-gating '
                                      '  --MergeIndex 1 --CodeVersion lstm4_linear_gating_30 ')

os.system(cs_shared_params_st_mgcn + ' --City Beijing --external_method earlyconcat '
                                      '  --MergeIndex 1 --CodeVersion earlyconcat_30 ')

os.system(cs_shared_params_st_mgcn + ' --City Beijing --external_method earlyadd '
                                      '  --MergeIndex 1 --CodeVersion earlyadd_30 ')

