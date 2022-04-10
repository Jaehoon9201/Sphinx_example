


"""
    my main
    ~~~~~~~~~
"""


class main_tester(object):
    """두 개의 int 값을 입력받아 다양한 연산을 할 수 있도록 하는 클래스.

    :param int a: a 값
    :param int b: b 값
    """

    def __init__(self, a, b):
        self._a = a
        self._b = b

    def is_same(self):
        """미리 입력받은 a와 b값이 같은지 확인하여 결과를 반환합니다.

        :return: boolean True or False에 대한 결과, a와 b가 값으면 True, 다르면 False

        예제:
            다음과 같이 사용하세요:

            >>> Test(1, 2).is_same()
            False

        """
        return self._a == self._b

    def plus(self):
        """미리 입력받은 a와 b값을 더한 결과를 반환합니다.

        :returns: int a + b에 대한 결과

        예제:
            다음과 같이 사용하세요:

            >>> Test(2, 1).plus()
            3


        """
        return self._a + self._b

#
#
# def run(train_iter):
#     """메인 알고리즘을 동작시킴
#
#     :returns: 메인 알고리즘에 대한 결과
#
#     예제:
#         다음과 같이 사용하세요:
#
#         >>> for 문에 넣어 iter 동작
#         >>> 또는 단일 동작을 시켜서 알고리즘 구동
#
#
#     """
#
#     if cfg.MODEL.MULTI_MODAL_for_LOW_FREQ == 0:
#         model = nn.AudioClassifier(device, num_lay=cfg.MODEL.NUM_LAY, ch=cfg.DATA.CH)
#     elif cfg.MODEL.MULTI_MODAL_for_LOW_FREQ == 1:
#         model = nn.AudioClassifier_MultiModal_for_LowFreq(device, num_lay=cfg.MODEL.NUM_LAY, ch=cfg.DATA.CH)
#
#     # if cfg.TRAIN.FLAG == True :
#     #     solver.training(neuralnet=model, dataset=train_dataset, epochs=cfg.TRAIN.MAX_EPOCH,
#     #                     batch_size=cfg.TRAIN.BATCH_SIZE, device=device, train_iter=train_iter,
#     #                     learning_rate=cfg.MODEL.lr, mic_num=cfg.DATA.MIC_NUM, mic_data_stack=cfg.DATA.MIC_DATA_STACK,
#     #                     lr_decay=cfg.MODEL.lr_decay, multi_modal_lf=cfg.MODEL.MULTI_MODAL_for_LOW_FREQ)
#
#     model = torch.load('model/%d_model_best.pt' %(train_iter))
#     model = model.eval()
#     solver.test(neuralnet=model, dataset_singly=test_dataset_singly, dataset=test_dataset,
#                 tot_test_dataset=tot_test_dataset, dataset_for_MeanStd=tot_train_dataset,
#                 num_class=cfg.DATA.LABEL_NUM, device=device, train_iter=train_iter, mic_num=cfg.DATA.MIC_NUM,
#                 mic_data_stack=cfg.DATA.MIC_DATA_STACK, multi_modal_lf=cfg.MODEL.MULTI_MODAL_for_LOW_FREQ)
#
#
# if __name__ == '__main__':
#     """주요 메인문
#
#     """
#
#     if cfg.DATA_GENERATOR.FLAG == True:
#         (train_df, test_df) \
#             = Dataset_Generator(cfg.DATA.LABEL_NUM, cfg.DATA.LABEL_NUM,
#                                 cfg.DATA.PARTIAL_NUM_for_TRAIN, cfg.DATA.PARTIAL_NUM_for_TEST,
#                                 cfg.DATA.TRAIN_DIS_LOC_NUM, cfg.DATA.TEST_DIS_LOC_NUM)
#     elif cfg.DATA_GENERATOR.FLAG == False:
#         train_csv = '__freezed_dataset/train M123__AudioName_Partial.csv'
#         train_df = pd.read_csv(train_csv)
#         train_df = train_df.values[0:, :]
#
#         train_df = pd.DataFrame(train_df,
#                                 columns=['num', 'mic1_path', 'mic1_file_name', 'mic2_path', 'mic2_file_name',
#                                          'mic3_path',
#                                          'mic3_file_name', 'LABEL'])
#         train_df = train_df.loc[:,
#                    ['mic1_path', 'mic1_file_name', 'mic2_path', 'mic2_file_name', 'mic3_path', 'mic3_file_name',
#                     'LABEL']]
#
#         test_csv = '__freezed_dataset/test M123__AudioName_Partial.csv'
#         test_df = pd.read_csv(test_csv)
#         test_df = test_df.values[0:, :]
#         test_df = pd.DataFrame(test_df,
#                                columns=['num', 'mic1_path', 'mic1_file_name', 'mic2_path', 'mic2_file_name',
#                                         'mic3_path',
#                                         'mic3_file_name', 'LABEL'])
#         test_df = test_df.loc[:,
#                   ['mic1_path', 'mic1_file_name', 'mic2_path', 'mic2_file_name', 'mic3_path', 'mic3_file_name',
#                    'LABEL']]
#
#         (train_dataset, tot_train_dataset, test_dataset_singly, test_dataset, tot_test_dataset) \
#             = Data_Loader(train_df, test_df, cfg.DATA.MIC_NUM, cfg.DATA.SR, cfg.DATA.N_MELS,
#                           cfg.DATA.N_FFT, cfg.DATA.HOP_LEN, cfg.DATA.N_FFT_LF, cfg.DATA.HOP_LEN_LF, cfg.DATA.MIC_DATA_STACK,
#                           cfg.DATA.SHIFT_LIMIT_TR, cfg.DATA.MAX_MASK_PCT_TR, cfg.DATA.N_FREQ_MASKS_TR, cfg.DATA.N_TIME_MASKS_TR,
#                           cfg.DATA.SHIFT_LIMIT_TE, cfg.DATA.MAX_MASK_PCT_TE, cfg.DATA.N_FREQ_MASKS_TE, cfg.DATA.N_TIME_MASKS_TE,
#                           cfg.MODEL.MULTI_MODAL_for_LOW_FREQ)
#
#     for train_iter in range(0, cfg.TRAIN.TRAIN_ITER):
#         run(train_iter)
