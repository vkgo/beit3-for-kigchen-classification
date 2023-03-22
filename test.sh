# offical evaluation. use to evaluate the valset.
python -m torch.distributed.launch --nproc_per_node=1 run_beit3_finetuning.py \
        --model beit3_large_patch16_224 \
        --task imagenet \
        --batch_size 128 \
        --sentencepiece_model ./pretrained_model/beit3.spm \
        --finetune ./pretrained_model/beit3_large_itc_patch16_224.pth \
        --data_path ./data/kitchen \
        --eval \
        --dist_eval \
        --checkpoint ./saved_model/checkpoint-best-saved/mp_rank_00_model_states.pt

# hwj's rebuilt evaluation. use to evaluate the testset.
python -m torch.distributed.launch --nproc_per_node=1 run_beit3_finetuning.py \
        --model beit3_large_patch16_224 \
        --task imagenet \
        --batch_size 128 \
        --sentencepiece_model ./pretrained_model/beit3.spm \
        --finetune ./pretrained_model/beit3_large_itc_patch16_224.pth \
        --data_path ./data/kitchen \
        --hwj_test \
        --dist_eval \
        --checkpoint ./saved_model/checkpoint-best-saved/mp_rank_00_model_states.pt