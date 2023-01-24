from haystack.nodes import FARMReader

reader = FARMReader(model_name_or_path="deepset/roberta-base-squad2", 
                    max_seq_len = 512, 
                    context_window_size = 150,
                    doc_stride = 128,
                    batch_size = 32,
                    use_gpu=True
                    )

reader.train(data_dir= '../data', 
             train_filename="data.json", 
             use_gpu=True, 
             n_epochs=10, 
             save_dir="Model"
             )

reader.save(directory="MTE_QA_model")
