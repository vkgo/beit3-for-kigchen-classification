rm nohup.out
export CUDA_HOME=/usr/local/cuda
nohup python -m torch.distributed.launch --nproc_per_node=4 run_beit3_finetuning.py \
        --model beit3_large_patch16_224 \
        --task imagenet \
        --batch_size 128 \
        --layer_decay 0.8 \
        --lr 2e-4 \
        --update_freq 1 \
        --epochs 256 \
        --warmup_epochs 5 \
        --drop_path 0.25 \
        --sentencepiece_model ./pretrained_model/beit3.spm \
        --finetune ./pretrained_model/beit3_large_itc_patch16_224.pth \
        --data_path ./data/kitchen \
        --output_dir ./saved_model \
        --log_dir ./logs \
        --weight_decay 0.05 \
        --seed 42 \
        --save_ckpt_freq 5 \
        --dist_eval \
        --mixup 0.8 \
        --cutmix 1.0 \
        --enable_deepspeed \
        --checkpoint_activations &
tail -f nohup.out
echo "完成"