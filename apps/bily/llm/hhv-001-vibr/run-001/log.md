# ViBR Run Log

**Status**: FAILED

## Full Log

```
2026-05-08 17:20:57 | INFO | === src_vibr.2026-05-08T21-20-57__run-001__pipeline__started ===
2026-05-08 17:20:57 | INFO | Starting ViBR run
2026-05-08 17:20:57 | INFO | App: bily
2026-05-08 17:20:57 | INFO | Video: /Users/tanmaybhuskute/Documents/gifdroid-reproduction/apps/bily/videos/hhv-001.mp4
2026-05-08 17:20:57 | INFO | Algorithm: clip
2026-05-08 17:20:57 | INFO | LLM: gemini (gemini-2.5-pro)
2026-05-08 17:20:57 | INFO | Output: /Users/tanmaybhuskute/Documents/gifdroid-reproduction/apps/bily/llm/ViBR_gemini/handheld/run-001
2026-05-08 17:21:02 | INFO | FutureWarning: Importing from timm.models.layers is deprecated, please import via timm.layers
2026-05-08 17:21:02 | INFO | UserWarning: Failed to load custom C++ ops. Running on CPU mode Only!
2026-05-08 17:21:02 | INFO | UserWarning: torch.meshgrid: in an upcoming release, it will be required to pass the indexing argument. (Triggered internally at /Users/runner/work/pytorch/pytorch/pytorch/aten/src/ATen/native/TensorShape.cpp:4383.)
2026-05-08 17:21:03 | INFO | Warning: You are sending unauthenticated requests to the HF Hub. Please set a HF_TOKEN to enable higher rate limits and faster downloads.
2026-05-08 17:21:03 | INFO | final text_encoder_type: bert-base-uncased
2026-05-08 17:21:03 | INFO | 
2026-05-08 17:21:03 | INFO | Loading weights:   0%|          | 0/199 [00:00<?, ?it/s]
2026-05-08 17:21:03 | INFO | Loading weights: 100%|██████████| 199/199 [00:00<00:00, 18344.32it/s]
2026-05-08 17:21:03 | INFO | [1mBertModel LOAD REPORT[0m from: bert-base-uncased
2026-05-08 17:21:03 | INFO | Key                                        | Status     |  | 
2026-05-08 17:21:03 | INFO | -------------------------------------------+------------+--+-
2026-05-08 17:21:03 | INFO | cls.predictions.transform.LayerNorm.bias   | UNEXPECTED |  | 
2026-05-08 17:21:03 | INFO | cls.predictions.transform.dense.weight     | UNEXPECTED |  | 
2026-05-08 17:21:03 | INFO | cls.predictions.transform.dense.bias       | UNEXPECTED |  | 
2026-05-08 17:21:03 | INFO | cls.predictions.bias                       | UNEXPECTED |  | 
2026-05-08 17:21:03 | INFO | cls.predictions.transform.LayerNorm.weight | UNEXPECTED |  | 
2026-05-08 17:21:03 | INFO | cls.seq_relationship.bias                  | UNEXPECTED |  | 
2026-05-08 17:21:03 | INFO | cls.seq_relationship.weight                | UNEXPECTED |  | 
2026-05-08 17:21:03 | INFO | 
2026-05-08 17:21:03 | INFO | Notes:
2026-05-08 17:21:03 | INFO | - UNEXPECTED:	can be ignored when loading from different task/architecture; not ok if you expect identical arch.
2026-05-08 17:21:14 | INFO | 🔹 Starting video processing (algorithm=clip, llm=gemini, model=gemini-2.5-pro)...
2026-05-08 17:21:14 | INFO | Initializing ADB device controller...
2026-05-08 17:21:14 | INFO | 📱 Preparing device for app: bily
2026-05-08 17:21:14 | INFO | 🏠 Going to home screen...
2026-05-08 17:21:14 | INFO | 🚀 Opening app 'bily' with command: am start -n com.bily/.MainActivity
2026-05-08 17:21:14 | INFO | ✅ App 'bily' opened and ready
2026-05-08 17:21:14 | INFO | Taking screenshot: /sdcard/screenshot-0.png -> /Users/tanmaybhuskute/Documents/gifdroid-reproduction/apps/bily/llm/ViBR_gemini/handheld/run-001/artifacts/hhv-001/screenshot-0.png
2026-05-08 17:21:14 | INFO | Reading frames from video...
2026-05-08 17:21:14 | INFO | Reading frame:  2
2026-05-08 17:21:14 | INFO | Reading frame:  3
2026-05-08 17:21:14 | INFO | Reading frame:  4
2026-05-08 17:21:14 | INFO | Reading frame:  5
2026-05-08 17:21:14 | INFO | Reading frame:  6
2026-05-08 17:21:14 | INFO | Reading frame:  7
2026-05-08 17:21:14 | INFO | Reading frame:  8
2026-05-08 17:21:14 | INFO | Reading frame:  9
2026-05-08 17:21:14 | INFO | Reading frame:  10
2026-05-08 17:21:14 | INFO | Reading frame:  11
2026-05-08 17:21:14 | INFO | Reading frame:  12
2026-05-08 17:21:14 | INFO | Reading frame:  13
2026-05-08 17:21:14 | INFO | Reading frame:  14
2026-05-08 17:21:14 | INFO | Reading frame:  15
2026-05-08 17:21:14 | INFO | Reading frame:  16
2026-05-08 17:21:14 | INFO | Reading frame:  17
2026-05-08 17:21:14 | INFO | Reading frame:  18
2026-05-08 17:21:14 | INFO | Reading frame:  19
2026-05-08 17:21:14 | INFO | Reading frame:  20
2026-05-08 17:21:14 | INFO | Reading frame:  21
2026-05-08 17:21:14 | INFO | Reading frame:  22
2026-05-08 17:21:14 | INFO | Reading frame:  23
2026-05-08 17:21:14 | INFO | Reading frame:  24
2026-05-08 17:21:14 | INFO | Reading frame:  25
2026-05-08 17:21:14 | INFO | Reading frame:  26
2026-05-08 17:21:14 | INFO | Reading frame:  27
2026-05-08 17:21:14 | INFO | Reading frame:  28
2026-05-08 17:21:14 | INFO | Reading frame:  29
2026-05-08 17:21:14 | INFO | Reading frame:  30
2026-05-08 17:21:14 | INFO | Reading frame:  31
2026-05-08 17:21:14 | INFO | Reading frame:  32
2026-05-08 17:21:14 | INFO | Reading frame:  33
2026-05-08 17:21:14 | INFO | Reading frame:  34
2026-05-08 17:21:14 | INFO | Reading frame:  35
2026-05-08 17:21:14 | INFO | Reading frame:  36
2026-05-08 17:21:14 | INFO | Reading frame:  37
2026-05-08 17:21:14 | INFO | Reading frame:  38
2026-05-08 17:21:14 | INFO | Reading frame:  39
2026-05-08 17:21:14 | INFO | Reading frame:  40
2026-05-08 17:21:14 | INFO | Reading frame:  41
2026-05-08 17:21:14 | INFO | Reading frame:  42
2026-05-08 17:21:14 | INFO | Reading frame:  43
2026-05-08 17:21:14 | INFO | Reading frame:  44
2026-05-08 17:21:14 | INFO | Reading frame:  45
2026-05-08 17:21:14 | INFO | Reading frame:  46
2026-05-08 17:21:14 | INFO | Reading frame:  47
2026-05-08 17:21:14 | INFO | Reading frame:  48
2026-05-08 17:21:14 | INFO | Reading frame:  49
2026-05-08 17:21:14 | INFO | Reading frame:  50
2026-05-08 17:21:14 | INFO | Reading frame:  51
2026-05-08 17:21:14 | INFO | Reading frame:  52
2026-05-08 17:21:14 | INFO | Reading frame:  53
2026-05-08 17:21:14 | INFO | Reading frame:  54
2026-05-08 17:21:14 | INFO | Reading frame:  55
2026-05-08 17:21:14 | INFO | Reading frame:  56
2026-05-08 17:21:14 | INFO | Reading frame:  57
2026-05-08 17:21:14 | INFO | Reading frame:  58
2026-05-08 17:21:14 | INFO | Reading frame:  59
2026-05-08 17:21:14 | INFO | Reading frame:  60
2026-05-08 17:21:14 | INFO | Reading frame:  61
2026-05-08 17:21:14 | INFO | Reading frame:  62
2026-05-08 17:21:14 | INFO | Reading frame:  63
2026-05-08 17:21:14 | INFO | Reading frame:  64
2026-05-08 17:21:14 | INFO | Reading frame:  65
2026-05-08 17:21:14 | INFO | Reading frame:  66
2026-05-08 17:21:14 | INFO | Reading frame:  67
2026-05-08 17:21:14 | INFO | Reading frame:  68
2026-05-08 17:21:14 | INFO | Reading frame:  69
2026-05-08 17:21:14 | INFO | Reading frame:  70
2026-05-08 17:21:14 | INFO | Reading frame:  71
2026-05-08 17:21:14 | INFO | Reading frame:  72
2026-05-08 17:21:14 | INFO | Reading frame:  73
2026-05-08 17:21:14 | INFO | Reading frame:  74
2026-05-08 17:21:14 | INFO | Reading frame:  75
2026-05-08 17:21:14 | INFO | Reading frame:  76
2026-05-08 17:21:14 | INFO | Reading frame:  77
2026-05-08 17:21:14 | INFO | Reading frame:  78
2026-05-08 17:21:14 | INFO | Reading frame:  79
2026-05-08 17:21:14 | INFO | Reading frame:  80
2026-05-08 17:21:14 | INFO | Reading frame:  81
2026-05-08 17:21:14 | INFO | Reading frame:  82
2026-05-08 17:21:14 | INFO | Reading frame:  83
2026-05-08 17:21:14 | INFO | Reading frame:  84
2026-05-08 17:21:14 | INFO | Reading frame:  85
2026-05-08 17:21:14 | INFO | Reading frame:  86
2026-05-08 17:21:14 | INFO | Reading frame:  87
2026-05-08 17:21:14 | INFO | Reading frame:  88
2026-05-08 17:21:14 | INFO | Reading frame:  89
2026-05-08 17:21:14 | INFO | Reading frame:  90
2026-05-08 17:21:14 | INFO | Reading frame:  91
2026-05-08 17:21:14 | INFO | Reading frame:  92
2026-05-08 17:21:14 | INFO | Reading frame:  93
2026-05-08 17:21:14 | INFO | Reading frame:  94
2026-05-08 17:21:14 | INFO | Reading frame:  95
2026-05-08 17:21:14 | INFO | Reading frame:  96
2026-05-08 17:21:14 | INFO | Reading frame:  97
2026-05-08 17:21:14 | INFO | Reading frame:  98
2026-05-08 17:21:14 | INFO | Reading frame:  99
2026-05-08 17:21:14 | INFO | Reading frame:  100
2026-05-08 17:21:14 | INFO | Reading frame:  101
2026-05-08 17:21:14 | INFO | Reading frame:  102
2026-05-08 17:21:14 | INFO | Reading frame:  103
2026-05-08 17:21:14 | INFO | Reading frame:  104
2026-05-08 17:21:14 | INFO | Reading frame:  105
2026-05-08 17:21:14 | INFO | Reading frame:  106
2026-05-08 17:21:14 | INFO | Reading frame:  107
2026-05-08 17:21:14 | INFO | Reading frame:  108
2026-05-08 17:21:14 | INFO | Reading frame:  109
2026-05-08 17:21:14 | INFO | Reading frame:  110
2026-05-08 17:21:14 | INFO | Reading frame:  111
2026-05-08 17:21:14 | INFO | Reading frame:  112
2026-05-08 17:21:14 | INFO | Reading frame:  113
2026-05-08 17:21:14 | INFO | Reading frame:  114
2026-05-08 17:21:14 | INFO | Reading frame:  115
2026-05-08 17:21:14 | INFO | Reading frame:  116
2026-05-08 17:21:14 | INFO | Reading frame:  117
2026-05-08 17:21:14 | INFO | Reading frame:  118
2026-05-08 17:21:14 | INFO | Reading frame:  119
2026-05-08 17:21:14 | INFO | Reading frame:  120
2026-05-08 17:21:14 | INFO | Reading frame:  121
2026-05-08 17:21:14 | INFO | Reading frame:  122
2026-05-08 17:21:14 | INFO | Reading frame:  123
2026-05-08 17:21:14 | INFO | Reading frame:  124
2026-05-08 17:21:14 | INFO | Reading frame:  125
2026-05-08 17:21:14 | INFO | Reading frame:  126
2026-05-08 17:21:14 | INFO | Reading frame:  127
2026-05-08 17:21:14 | INFO | Reading frame:  128
2026-05-08 17:21:14 | INFO | Reading frame:  129
2026-05-08 17:21:14 | INFO | Reading frame:  130
2026-05-08 17:21:14 | INFO | Reading frame:  131
2026-05-08 17:21:14 | INFO | Reading frame:  132
2026-05-08 17:21:14 | INFO | Reading frame:  133
2026-05-08 17:21:14 | INFO | Reading frame:  134
2026-05-08 17:21:14 | INFO | Reading frame:  135
2026-05-08 17:21:14 | INFO | Reading frame:  136
2026-05-08 17:21:14 | INFO | Reading frame:  137
2026-05-08 17:21:14 | INFO | Reading frame:  138
2026-05-08 17:21:14 | INFO | Reading frame:  139
2026-05-08 17:21:14 | INFO | Reading frame:  140
2026-05-08 17:21:14 | INFO | Reading frame:  141
2026-05-08 17:21:14 | INFO | Reading frame:  142
2026-05-08 17:21:14 | INFO | Reading frame:  143
2026-05-08 17:21:14 | INFO | Reading frame:  144
2026-05-08 17:21:14 | INFO | Reading frame:  145
2026-05-08 17:21:14 | INFO | Reading frame:  146
2026-05-08 17:21:14 | INFO | Reading frame:  147
2026-05-08 17:21:14 | INFO | Reading frame:  148
2026-05-08 17:21:14 | INFO | Reading frame:  149
2026-05-08 17:21:14 | INFO | Reading frame:  150
2026-05-08 17:21:14 | INFO | Reading frame:  151
2026-05-08 17:21:14 | INFO | Reading frame:  152
2026-05-08 17:21:14 | INFO | Reading frame:  153
2026-05-08 17:21:14 | INFO | Reading frame:  154
2026-05-08 17:21:14 | INFO | Reading frame:  155
2026-05-08 17:21:14 | INFO | Reading frame:  156
2026-05-08 17:21:14 | INFO | Reading frame:  157
2026-05-08 17:21:14 | INFO | Reading frame:  158
2026-05-08 17:21:14 | INFO | Reading frame:  159
2026-05-08 17:21:14 | INFO | Reading frame:  160
2026-05-08 17:21:14 | INFO | Reading frame:  161
2026-05-08 17:21:14 | INFO | Reading frame:  162
2026-05-08 17:21:14 | INFO | Reading frame:  163
2026-05-08 17:21:14 | INFO | Reading frame:  164
2026-05-08 17:21:14 | INFO | Reading frame:  165
2026-05-08 17:21:14 | INFO | Reading frame:  166
2026-05-08 17:21:14 | INFO | Reading frame:  167
2026-05-08 17:21:14 | INFO | Reading frame:  168
2026-05-08 17:21:14 | INFO | Reading frame:  169
2026-05-08 17:21:14 | INFO | Reading frame:  170
2026-05-08 17:21:14 | INFO | Reading frame:  171
2026-05-08 17:21:14 | INFO | Reading frame:  172
2026-05-08 17:21:14 | INFO | Reading frame:  173
2026-05-08 17:21:14 | INFO | Reading frame:  174
2026-05-08 17:21:14 | INFO | Reading frame:  175
2026-05-08 17:21:14 | INFO | Reading frame:  176
2026-05-08 17:21:14 | INFO | Reading frame:  177
2026-05-08 17:21:14 | INFO | Reading frame:  178
2026-05-08 17:21:14 | INFO | Reading frame:  179
2026-05-08 17:21:14 | INFO | Reading frame:  180
2026-05-08 17:21:14 | INFO | Reading frame:  181
2026-05-08 17:21:14 | INFO | Reading frame:  182
2026-05-08 17:21:14 | INFO | Reading frame:  183
2026-05-08 17:21:14 | INFO | Reading frame:  184
2026-05-08 17:21:14 | INFO | Reading frame:  185
2026-05-08 17:21:14 | INFO | Reading frame:  186
2026-05-08 17:21:14 | INFO | Reading frame:  187
2026-05-08 17:21:14 | INFO | Reading frame:  188
2026-05-08 17:21:14 | INFO | Reading frame:  189
2026-05-08 17:21:14 | INFO | Reading frame:  190
2026-05-08 17:21:14 | INFO | Reading frame:  191
2026-05-08 17:21:14 | INFO | Reading frame:  192
2026-05-08 17:21:14 | INFO | Reading frame:  193
2026-05-08 17:21:14 | INFO | Reading frame:  194
2026-05-08 17:21:14 | INFO | Reading frame:  195
2026-05-08 17:21:14 | INFO | Reading frame:  196
2026-05-08 17:21:14 | INFO | Reading frame:  197
2026-05-08 17:21:14 | INFO | Reading frame:  198
2026-05-08 17:21:14 | INFO | Reading frame:  199
2026-05-08 17:21:14 | INFO | Reading frame:  200
2026-05-08 17:21:14 | INFO | Reading frame:  201
2026-05-08 17:21:14 | INFO | Reading frame:  202
2026-05-08 17:21:14 | INFO | Reading frame:  203
2026-05-08 17:21:14 | INFO | Reading frame:  204
2026-05-08 17:21:14 | INFO | Reading frame:  205
2026-05-08 17:21:14 | INFO | Reading frame:  206
2026-05-08 17:21:14 | INFO | Reading frame:  207
2026-05-08 17:21:14 | INFO | Reading frame:  208
2026-05-08 17:21:14 | INFO | Reading frame:  209
2026-05-08 17:21:14 | INFO | Reading frame:  210
2026-05-08 17:21:14 | INFO | Reading frame:  211
2026-05-08 17:21:14 | INFO | Reading frame:  212
2026-05-08 17:21:14 | INFO | Reading frame:  213
2026-05-08 17:21:14 | INFO | Reading frame:  214
2026-05-08 17:21:14 | INFO | Reading frame:  215
2026-05-08 17:21:14 | INFO | Reading frame:  216
2026-05-08 17:21:14 | INFO | Reading frame:  217
2026-05-08 17:21:14 | INFO | Reading frame:  218
2026-05-08 17:21:14 | INFO | Reading frame:  219
2026-05-08 17:21:14 | INFO | Reading frame:  220
2026-05-08 17:21:14 | INFO | Reading frame:  221
2026-05-08 17:21:14 | INFO | Reading frame:  222
2026-05-08 17:21:14 | INFO | Reading frame:  223
2026-05-08 17:21:14 | INFO | Reading frame:  224
2026-05-08 17:21:14 | INFO | Reading frame:  225
2026-05-08 17:21:14 | INFO | Reading frame:  226
2026-05-08 17:21:14 | INFO | Reading frame:  227
2026-05-08 17:21:14 | INFO | Reading frame:  228
2026-05-08 17:21:14 | INFO | Reading frame:  229
2026-05-08 17:21:14 | INFO | Reading frame:  230
2026-05-08 17:21:14 | INFO | Reading frame:  231
2026-05-08 17:21:14 | INFO | Reading frame:  232
2026-05-08 17:21:14 | INFO | Reading frame:  233
2026-05-08 17:21:14 | INFO | Reading frame:  234
2026-05-08 17:21:14 | INFO | Reading frame:  235
2026-05-08 17:21:14 | INFO | Reading frame:  236
2026-05-08 17:21:14 | INFO | Reading frame:  237
2026-05-08 17:21:14 | INFO | Reading frame:  238
2026-05-08 17:21:14 | INFO | Reading frame:  239
2026-05-08 17:21:14 | INFO | Reading frame:  240
2026-05-08 17:21:14 | INFO | Reading frame:  241
2026-05-08 17:21:14 | INFO | Reading frame:  242
2026-05-08 17:21:14 | INFO | Reading frame:  243
2026-05-08 17:21:14 | INFO | Reading frame:  244
2026-05-08 17:21:14 | INFO | Reading frame:  245
2026-05-08 17:21:14 | INFO | Reading frame:  246
2026-05-08 17:21:14 | INFO | Reading frame:  247
2026-05-08 17:21:14 | INFO | Reading frame:  248
2026-05-08 17:21:14 | INFO | Reading frame:  249
2026-05-08 17:21:14 | INFO | Reading frame:  250
2026-05-08 17:21:14 | INFO | Reading frame:  251
2026-05-08 17:21:14 | INFO | Reading frame:  252
2026-05-08 17:21:14 | INFO | Reading frame:  253
2026-05-08 17:21:14 | INFO | Reading frame:  254
2026-05-08 17:21:14 | INFO | Reading frame:  255
2026-05-08 17:21:14 | INFO | Reading frame:  256
2026-05-08 17:21:14 | INFO | Reading frame:  257
2026-05-08 17:21:14 | INFO | Reading frame:  258
2026-05-08 17:21:14 | INFO | Reading frame:  259
2026-05-08 17:21:14 | INFO | Reading frame:  260
2026-05-08 17:21:14 | INFO | Reading frame:  261
2026-05-08 17:21:14 | INFO | Reading frame:  262
2026-05-08 17:21:14 | INFO | Reading frame:  263
2026-05-08 17:21:14 | INFO | Reading frame:  264
2026-05-08 17:21:14 | INFO | Reading frame:  265
2026-05-08 17:21:14 | INFO | Reading frame:  266
2026-05-08 17:21:14 | INFO | Reading frame:  267
2026-05-08 17:21:14 | INFO | Reading frame:  268
2026-05-08 17:21:14 | INFO | Reading frame:  269
2026-05-08 17:21:14 | INFO | Reading frame:  270
2026-05-08 17:21:14 | INFO | Reading frame:  271
2026-05-08 17:21:14 | INFO | Reading frame:  272
2026-05-08 17:21:14 | INFO | Reading frame:  273
2026-05-08 17:21:14 | INFO | Reading frame:  274
2026-05-08 17:21:14 | INFO | Reading frame:  275
2026-05-08 17:21:14 | INFO | Reading frame:  276
2026-05-08 17:21:14 | INFO | Reading frame:  277
2026-05-08 17:21:14 | INFO | Reading frame:  278
2026-05-08 17:21:14 | INFO | Reading frame:  279
2026-05-08 17:21:14 | INFO | Reading frame:  280
2026-05-08 17:21:14 | INFO | Reading frame:  281
2026-05-08 17:21:14 | INFO | Reading frame:  282
2026-05-08 17:21:14 | INFO | Reading frame:  283
2026-05-08 17:21:14 | INFO | Reading frame:  284
2026-05-08 17:21:14 | INFO | Reading frame:  285
2026-05-08 17:21:14 | INFO | Reading frame:  286
2026-05-08 17:21:14 | INFO | Reading frame:  287
2026-05-08 17:21:14 | INFO | Reading frame:  288
2026-05-08 17:21:14 | INFO | Reading frame:  289
2026-05-08 17:21:14 | INFO | Reading frame:  290
2026-05-08 17:21:14 | INFO | Reading frame:  291
2026-05-08 17:21:14 | INFO | Reading frame:  292
2026-05-08 17:21:14 | INFO | Reading frame:  293
2026-05-08 17:21:14 | INFO | Reading frame:  294
2026-05-08 17:21:14 | INFO | Reading frame:  295
2026-05-08 17:21:14 | INFO | Reading frame:  296
2026-05-08 17:21:14 | INFO | Reading frame:  297
2026-05-08 17:21:14 | INFO | Reading frame:  298
2026-05-08 17:21:14 | INFO | Reading frame:  299
2026-05-08 17:21:14 | INFO | Reading frame:  300
2026-05-08 17:21:14 | INFO | Reading frame:  301
2026-05-08 17:21:14 | INFO | Reading frame:  302
2026-05-08 17:21:14 | INFO | Reading frame:  303
2026-05-08 17:21:14 | INFO | Reading frame:  304
2026-05-08 17:21:14 | INFO | Reading frame:  305
2026-05-08 17:21:14 | INFO | Reading frame:  306
2026-05-08 17:21:14 | INFO | Reading frame:  307
2026-05-08 17:21:14 | INFO | Reading frame:  308
2026-05-08 17:21:14 | INFO | Reading frame:  309
2026-05-08 17:21:14 | INFO | Reading frame:  310
2026-05-08 17:21:14 | INFO | Reading frame:  311
2026-05-08 17:21:14 | INFO | Reading frame:  312
2026-05-08 17:21:14 | INFO | Reading frame:  313
2026-05-08 17:21:14 | INFO | Reading frame:  314
2026-05-08 17:21:14 | INFO | Reading frame:  315
2026-05-08 17:21:14 | INFO | Reading frame:  316
2026-05-08 17:21:14 | INFO | Reading frame:  317
2026-05-08 17:21:14 | INFO | Reading frame:  318
2026-05-08 17:21:14 | INFO | Reading frame:  319
2026-05-08 17:21:14 | INFO | Reading frame:  320
2026-05-08 17:21:14 | INFO | Reading frame:  321
2026-05-08 17:21:14 | INFO | Reading frame:  322
2026-05-08 17:21:14 | INFO | Reading frame:  323
2026-05-08 17:21:14 | INFO | Reading frame:  324
2026-05-08 17:21:14 | INFO | Reading frame:  325
2026-05-08 17:21:14 | INFO | Reading frame:  326
2026-05-08 17:21:14 | INFO | Reading frame:  327
2026-05-08 17:21:14 | INFO | Reading frame:  328
2026-05-08 17:21:14 | INFO | Reading frame:  329
2026-05-08 17:21:14 | INFO | Reading frame:  330
2026-05-08 17:21:14 | INFO | Reading frame:  331
2026-05-08 17:21:14 | INFO | Reading frame:  332
2026-05-08 17:21:14 | INFO | Reading frame:  333
2026-05-08 17:21:14 | INFO | Reading frame:  334
2026-05-08 17:21:14 | INFO | Reading frame:  335
2026-05-08 17:21:14 | INFO | Reading frame:  336
2026-05-08 17:21:14 | INFO | Reading frame:  337
2026-05-08 17:21:14 | INFO | Reading frame:  338
2026-05-08 17:21:14 | INFO | Reading frame:  339
2026-05-08 17:21:14 | INFO | Reading frame:  340
2026-05-08 17:21:14 | INFO | Reading frame:  341
2026-05-08 17:21:14 | INFO | Reading frame:  342
2026-05-08 17:21:14 | INFO | Reading frame:  343
2026-05-08 17:21:14 | INFO | Reading frame:  344
2026-05-08 17:21:14 | INFO | Reading frame:  345
2026-05-08 17:21:14 | INFO | Reading frame:  346
2026-05-08 17:21:14 | INFO | Reading frame:  347
2026-05-08 17:21:14 | INFO | Reading frame:  348
2026-05-08 17:21:14 | INFO | Reading frame:  349
2026-05-08 17:21:14 | INFO | Reading frame:  350
2026-05-08 17:21:14 | INFO | Reading frame:  351
2026-05-08 17:21:14 | INFO | Reading frame:  352
2026-05-08 17:21:14 | INFO | Reading frame:  353
2026-05-08 17:21:14 | INFO | Reading frame:  354
2026-05-08 17:21:14 | INFO | Reading frame:  355
2026-05-08 17:21:14 | INFO | Reading frame:  356
2026-05-08 17:21:14 | INFO | Reading frame:  357
2026-05-08 17:21:14 | INFO | Reading frame:  358
2026-05-08 17:21:14 | INFO | Reading frame:  359
2026-05-08 17:21:14 | INFO | Reading frame:  360
2026-05-08 17:21:14 | INFO | Reading frame:  361
2026-05-08 17:21:14 | INFO | Reading frame:  362
2026-05-08 17:21:14 | INFO | Reading frame:  363
2026-05-08 17:21:14 | INFO | Reading frame:  364
2026-05-08 17:21:14 | INFO | Reading frame:  365
2026-05-08 17:21:14 | INFO | Reading frame:  366
2026-05-08 17:21:14 | INFO | Reading frame:  367
2026-05-08 17:21:14 | INFO | Reading frame:  368
2026-05-08 17:21:14 | INFO | Reading frame:  369
2026-05-08 17:21:14 | INFO | Reading frame:  370
2026-05-08 17:21:14 | INFO | Reading frame:  371
2026-05-08 17:21:14 | INFO | Reading frame:  372
2026-05-08 17:21:14 | INFO | Reading frame:  373
2026-05-08 17:21:14 | INFO | Reading frame:  374
2026-05-08 17:21:14 | INFO | Reading frame:  375
2026-05-08 17:21:14 | INFO | Reading frame:  376
2026-05-08 17:21:14 | INFO | Reading frame:  377
2026-05-08 17:21:14 | INFO | Reading frame:  378
2026-05-08 17:21:14 | INFO | Reading frame:  379
2026-05-08 17:21:14 | INFO | Reading frame:  380
2026-05-08 17:21:14 | INFO | Reading frame:  381
2026-05-08 17:21:14 | INFO | Reading frame:  382
2026-05-08 17:21:14 | INFO | Reading frame:  383
2026-05-08 17:21:14 | INFO | Reading frame:  384
2026-05-08 17:21:14 | INFO | Reading frame:  385
2026-05-08 17:21:14 | INFO | Reading frame:  386
2026-05-08 17:21:14 | INFO | Reading frame:  387
2026-05-08 17:21:14 | INFO | Reading frame:  388
2026-05-08 17:21:14 | INFO | Reading frame:  389
2026-05-08 17:21:14 | INFO | Reading frame:  390
2026-05-08 17:21:14 | INFO | Reading frame:  391
2026-05-08 17:21:14 | INFO | Reading frame:  392
2026-05-08 17:21:14 | INFO | Reading frame:  393
2026-05-08 17:21:14 | INFO | Reading frame:  394
2026-05-08 17:21:14 | INFO | Reading frame:  395
2026-05-08 17:21:14 | INFO | Reading frame:  396
2026-05-08 17:21:14 | INFO | Reading frame:  397
2026-05-08 17:21:14 | INFO | Reading frame:  398
2026-05-08 17:21:14 | INFO | Reading frame:  399
2026-05-08 17:21:14 | INFO | Reading frame:  400
2026-05-08 17:21:14 | INFO | Reading frame:  401
2026-05-08 17:21:14 | INFO | Reading frame:  402
2026-05-08 17:21:14 | INFO | Reading frame:  403
2026-05-08 17:21:14 | INFO | Reading frame:  404
2026-05-08 17:21:14 | INFO | Reading frame:  405
2026-05-08 17:21:14 | INFO | Reading frame:  406
2026-05-08 17:21:14 | INFO | Reading frame:  407
2026-05-08 17:21:14 | INFO | Reading frame:  408
2026-05-08 17:21:14 | INFO | Reading frame:  409
2026-05-08 17:21:14 | INFO | Reading frame:  410
2026-05-08 17:21:14 | INFO | Reading frame:  411
2026-05-08 17:21:14 | INFO | Reading frame:  412
2026-05-08 17:21:14 | INFO | Reading frame:  413
2026-05-08 17:21:14 | INFO | Reading frame:  414
2026-05-08 17:21:14 | INFO | Reading frame:  415
2026-05-08 17:21:14 | INFO | Reading frame:  416
2026-05-08 17:21:14 | INFO | Reading frame:  417
2026-05-08 17:21:14 | INFO | Reading frame:  418
2026-05-08 17:21:14 | INFO | Reading frame:  419
2026-05-08 17:21:14 | INFO | Reading frame:  420
2026-05-08 17:21:14 | INFO | Reading frame:  421
2026-05-08 17:21:14 | INFO | Reading frame:  422
2026-05-08 17:21:14 | INFO | Reading frame:  423
2026-05-08 17:21:14 | INFO | Reading frame:  424
2026-05-08 17:21:14 | INFO | Reading frame:  425
2026-05-08 17:21:14 | INFO | Reading frame:  426
2026-05-08 17:21:14 | INFO | Reading frame:  427
2026-05-08 17:21:14 | INFO | Reading frame:  428
2026-05-08 17:21:14 | INFO | Reading frame:  429
2026-05-08 17:21:14 | INFO | Reading frame:  430
2026-05-08 17:21:14 | INFO | Reading frame:  431
2026-05-08 17:21:14 | INFO | Reading frame:  432
2026-05-08 17:21:14 | INFO | Reading frame:  433
2026-05-08 17:21:14 | INFO | Reading frame:  434
2026-05-08 17:21:14 | INFO | Reading frame:  435
2026-05-08 17:21:14 | INFO | Reading frame:  436
2026-05-08 17:21:14 | INFO | Reading frame:  437
2026-05-08 17:21:14 | INFO | Reading frame:  438
2026-05-08 17:21:14 | INFO | Reading frame:  439
2026-05-08 17:21:14 | INFO | Reading frame:  440
2026-05-08 17:21:14 | INFO | Reading frame:  441
2026-05-08 17:21:14 | INFO | Reading frame:  442
2026-05-08 17:21:14 | INFO | Reading frame:  443
2026-05-08 17:21:14 | INFO | Reading frame:  444
2026-05-08 17:21:14 | INFO | Reading frame:  445
2026-05-08 17:21:14 | INFO | Reading frame:  446
2026-05-08 17:21:14 | INFO | Reading frame:  447
2026-05-08 17:21:14 | INFO | Reading frame:  448
2026-05-08 17:21:14 | INFO | Reading frame:  449
2026-05-08 17:21:14 | INFO | Reading frame:  450
2026-05-08 17:21:14 | INFO | Reading frame:  451
2026-05-08 17:21:14 | INFO | Reading frame:  452
2026-05-08 17:21:14 | INFO | Reading frame:  453
2026-05-08 17:21:14 | INFO | Reading frame:  454
2026-05-08 17:21:14 | INFO | Reading frame:  455
2026-05-08 17:21:14 | INFO | Reading frame:  456
2026-05-08 17:21:14 | INFO | Reading frame:  457
2026-05-08 17:21:14 | INFO | Reading frame:  458
2026-05-08 17:21:14 | INFO | Reading frame:  459
2026-05-08 17:21:14 | INFO | Reading frame:  460
2026-05-08 17:21:14 | INFO | Reading frame:  461
2026-05-08 17:21:14 | INFO | Reading frame:  462
2026-05-08 17:21:14 | INFO | Reading frame:  463
2026-05-08 17:21:14 | INFO | Reading frame:  464
2026-05-08 17:21:14 | INFO | Reading frame:  465
2026-05-08 17:21:14 | INFO | Reading frame:  466
2026-05-08 17:21:14 | INFO | Reading frame:  467
2026-05-08 17:21:14 | INFO | Reading frame:  468
2026-05-08 17:21:14 | INFO | Reading frame:  469
2026-05-08 17:21:14 | INFO | Reading frame:  470
2026-05-08 17:21:14 | INFO | Reading frame:  471
2026-05-08 17:21:14 | INFO | Reading frame:  472
2026-05-08 17:21:14 | INFO | Reading frame:  473
2026-05-08 17:21:14 | INFO | Reading frame:  474
2026-05-08 17:21:14 | INFO | Reading frame:  475
2026-05-08 17:21:14 | INFO | Reading frame:  476
2026-05-08 17:21:14 | INFO | Reading frame:  477
2026-05-08 17:21:14 | INFO | Reading frame:  478
2026-05-08 17:21:14 | INFO | Reading frame:  479
2026-05-08 17:21:14 | INFO | Reading frame:  480
2026-05-08 17:21:14 | INFO | Reading frame:  481
2026-05-08 17:21:14 | INFO | Reading frame:  482
2026-05-08 17:21:14 | INFO | Reading frame:  483
2026-05-08 17:21:14 | INFO | Reading frame:  484
2026-05-08 17:21:14 | INFO | Reading frame:  485
2026-05-08 17:21:14 | INFO | Reading frame:  486
2026-05-08 17:21:14 | INFO | Reading frame:  487
2026-05-08 17:21:14 | INFO | Reading frame:  488
2026-05-08 17:21:14 | INFO | Reading frame:  489
2026-05-08 17:21:14 | INFO | Reading frame:  490
2026-05-08 17:21:14 | INFO | Reading frame:  491
2026-05-08 17:21:14 | INFO | Reading frame:  492
2026-05-08 17:21:14 | INFO | Reading frame:  493
2026-05-08 17:21:14 | INFO | Reading frame:  494
2026-05-08 17:21:14 | INFO | Reading frame:  495
2026-05-08 17:21:14 | INFO | Reading frame:  496
2026-05-08 17:21:14 | INFO | Reading frame:  497
2026-05-08 17:21:14 | INFO | Reading frame:  498
2026-05-08 17:21:14 | INFO | Reading frame:  499
2026-05-08 17:21:14 | INFO | Reading frame:  500
2026-05-08 17:21:14 | INFO | Reading frame:  501
2026-05-08 17:21:14 | INFO | Reading frame:  502
2026-05-08 17:21:14 | INFO | Reading frame:  503
2026-05-08 17:21:14 | INFO | Reading frame:  504
2026-05-08 17:21:14 | INFO | Reading frame:  505
2026-05-08 17:21:14 | INFO | Reading frame:  506
2026-05-08 17:21:14 | INFO | Reading frame:  507
2026-05-08 17:21:14 | INFO | Reading frame:  508
2026-05-08 17:21:14 | INFO | Reading frame:  509
2026-05-08 17:21:14 | INFO | Reading frame:  510
2026-05-08 17:21:14 | INFO | Reading frame:  511
2026-05-08 17:21:14 | INFO | Reading frame:  512
2026-05-08 17:21:14 | INFO | Reading frame:  513
2026-05-08 17:21:14 | INFO | Reading frame:  514
2026-05-08 17:21:14 | INFO | Reading frame:  515
2026-05-08 17:21:14 | INFO | Reading frame:  516
2026-05-08 17:21:14 | INFO | Reading frame:  517
2026-05-08 17:21:14 | INFO | Reading frame:  518
2026-05-08 17:21:14 | INFO | Reading frame:  519
2026-05-08 17:21:14 | INFO | Reading frame:  520
2026-05-08 17:21:14 | INFO | Reading frame:  521
2026-05-08 17:21:14 | INFO | Reading frame:  522
2026-05-08 17:21:14 | INFO | Reading frame:  523
2026-05-08 17:21:14 | INFO | Reading frame:  524
2026-05-08 17:21:14 | INFO | Reading frame:  525
2026-05-08 17:21:14 | INFO | Reading frame:  526
2026-05-08 17:21:14 | INFO | Reading frame:  527
2026-05-08 17:21:14 | INFO | Reading frame:  528
2026-05-08 17:21:14 | INFO | Reading frame:  529
2026-05-08 17:21:14 | INFO | Reading frame:  530
2026-05-08 17:21:14 | INFO | Reading frame:  531
2026-05-08 17:21:14 | INFO | Reading frame:  532
2026-05-08 17:21:14 | INFO | Reading frame:  533
2026-05-08 17:21:14 | INFO | Reading frame:  534
2026-05-08 17:21:14 | INFO | Reading frame:  535
2026-05-08 17:21:14 | INFO | Reading frame:  536
2026-05-08 17:21:14 | INFO | Reading frame:  537
2026-05-08 17:21:14 | INFO | Reading frame:  538
2026-05-08 17:21:14 | INFO | Reading frame:  539
2026-05-08 17:21:14 | INFO | Reading frame:  540
2026-05-08 17:21:14 | INFO | Reading frame:  541
2026-05-08 17:21:14 | INFO | Reading frame:  542
2026-05-08 17:21:14 | INFO | Reading frame:  543
2026-05-08 17:21:14 | INFO | Reading frame:  544
2026-05-08 17:21:14 | INFO | Reading frame:  545
2026-05-08 17:21:14 | INFO | Reading frame:  546
2026-05-08 17:21:14 | INFO | Reading frame:  547
2026-05-08 17:21:14 | INFO | Reading frame:  548
2026-05-08 17:21:14 | INFO | Reading frame:  549
2026-05-08 17:21:14 | INFO | Reading frame:  550
2026-05-08 17:21:14 | INFO | Reading frame:  551
2026-05-08 17:21:14 | INFO | Reading frame:  552
2026-05-08 17:21:14 | INFO | Reading frame:  553
2026-05-08 17:21:14 | INFO | Reading frame:  554
2026-05-08 17:21:14 | INFO | Reading frame:  555
2026-05-08 17:21:14 | INFO | Reading frame:  556
2026-05-08 17:21:14 | INFO | Reading frame:  557
2026-05-08 17:21:14 | INFO | Reading frame:  558
2026-05-08 17:21:14 | INFO | Reading frame:  559
2026-05-08 17:21:14 | INFO | Reading frame:  560
2026-05-08 17:21:14 | INFO | Reading frame:  561
2026-05-08 17:21:14 | INFO | Reading frame:  562
2026-05-08 17:21:14 | INFO | Reading frame:  563
2026-05-08 17:21:14 | INFO | Reading frame:  564
2026-05-08 17:21:14 | INFO | Reading frame:  565
2026-05-08 17:21:14 | INFO | Reading frame:  566
2026-05-08 17:21:14 | INFO | Reading frame:  567
2026-05-08 17:21:14 | INFO | Reading frame:  568
2026-05-08 17:21:14 | INFO | Reading frame:  569
2026-05-08 17:21:14 | INFO | Reading frame:  570
2026-05-08 17:21:14 | INFO | Reading frame:  571
2026-05-08 17:21:14 | INFO | Reading frame:  572
2026-05-08 17:21:14 | INFO | Reading frame:  573
2026-05-08 17:21:14 | INFO | Reading frame:  574
2026-05-08 17:21:14 | INFO | Reading frame:  575
2026-05-08 17:21:14 | INFO | Reading frame:  576
2026-05-08 17:21:14 | INFO | Reading frame:  577
2026-05-08 17:21:14 | INFO | Reading frame:  578
2026-05-08 17:21:14 | INFO | Reading frame:  579
2026-05-08 17:21:14 | INFO | Reading frame:  580
2026-05-08 17:21:14 | INFO | Reading frame:  581
2026-05-08 17:21:14 | INFO | Reading frame:  582
2026-05-08 17:21:14 | INFO | Reading frame:  583
2026-05-08 17:21:14 | INFO | Reading frame:  584
2026-05-08 17:21:14 | INFO | Reading frame:  585
2026-05-08 17:21:14 | INFO | Reading frame:  586
2026-05-08 17:21:14 | INFO | Reading frame:  587
2026-05-08 17:21:14 | INFO | Reading frame:  588
2026-05-08 17:21:14 | INFO | Reading frame:  589
2026-05-08 17:21:14 | INFO | Reading frame:  590
2026-05-08 17:21:14 | INFO | Reading frame:  591
2026-05-08 17:21:14 | INFO | Reading frame:  592
2026-05-08 17:21:14 | INFO | Reading frame:  593
2026-05-08 17:21:14 | INFO | Reading frame:  594
2026-05-08 17:21:14 | INFO | Reading frame:  595
2026-05-08 17:21:14 | INFO | Reading frame:  596
2026-05-08 17:21:14 | INFO | Reading frame:  597
2026-05-08 17:21:14 | INFO | Reading frame:  598
2026-05-08 17:21:14 | INFO | Reading frame:  599
2026-05-08 17:21:14 | INFO | Reading frame:  600
2026-05-08 17:21:14 | INFO | Reading frame:  601
2026-05-08 17:21:14 | INFO | Reading frame:  602
2026-05-08 17:21:14 | INFO | Reading frame:  603
2026-05-08 17:21:14 | INFO | Reading frame:  604
2026-05-08 17:21:14 | INFO | Reading frame:  605
2026-05-08 17:21:14 | INFO | Reading frame:  606
2026-05-08 17:21:14 | INFO | Reading frame:  607
2026-05-08 17:21:14 | INFO | Reading frame:  608
2026-05-08 17:21:14 | INFO | Reading frame:  609
2026-05-08 17:21:14 | INFO | Reading frame:  610
2026-05-08 17:21:14 | INFO | Reading frame:  611
2026-05-08 17:21:14 | INFO | Reading frame:  612
2026-05-08 17:21:14 | INFO | Reading frame:  613
2026-05-08 17:21:14 | INFO | Reading frame:  614
2026-05-08 17:21:14 | INFO | Reading frame:  615
2026-05-08 17:21:14 | INFO | Reading frame:  616
2026-05-08 17:21:14 | INFO | Reading frame:  617
2026-05-08 17:21:14 | INFO | Reading frame:  618
2026-05-08 17:21:14 | INFO | Reading frame:  619
2026-05-08 17:21:14 | INFO | Reading frame:  620
2026-05-08 17:21:14 | INFO | Reading frame:  621
2026-05-08 17:21:14 | INFO | Reading frame:  622
2026-05-08 17:21:14 | INFO | Reading frame:  623
2026-05-08 17:21:14 | INFO | Reading frame:  624
2026-05-08 17:21:14 | INFO | Reading frame:  625
2026-05-08 17:21:14 | INFO | Reading frame:  626
2026-05-08 17:21:14 | INFO | Reading frame:  627
2026-05-08 17:21:14 | INFO | Reading frame:  628
2026-05-08 17:21:14 | INFO | Reading frame:  629
2026-05-08 17:21:14 | INFO | Reading frame:  630
2026-05-08 17:21:14 | INFO | Reading frame:  631
2026-05-08 17:21:14 | INFO | Reading frame:  632
2026-05-08 17:21:14 | INFO | Reading frame:  633
2026-05-08 17:21:14 | INFO | Reading frame:  634
2026-05-08 17:21:14 | INFO | Reading frame:  635
2026-05-08 17:21:14 | INFO | Reading frame:  636
2026-05-08 17:21:14 | INFO | Reading frame:  637
2026-05-08 17:21:14 | INFO | Reading frame:  638
2026-05-08 17:21:14 | INFO | Reading frame:  639
2026-05-08 17:21:14 | INFO | Reading frame:  640
2026-05-08 17:21:14 | INFO | Reading frame:  641
2026-05-08 17:21:14 | INFO | Reading frame:  642
2026-05-08 17:21:14 | INFO | Reading frame:  643
2026-05-08 17:21:14 | INFO | Reading frame:  644
2026-05-08 17:21:14 | INFO | Reading frame:  645
2026-05-08 17:21:14 | INFO | Reading frame:  646
2026-05-08 17:21:14 | INFO | Reading frame:  647
2026-05-08 17:21:14 | INFO | Reading frame:  648
2026-05-08 17:21:14 | INFO | Reading frame:  649
2026-05-08 17:21:14 | INFO | Reading frame:  650
2026-05-08 17:21:14 | INFO | Reading frame:  651
2026-05-08 17:21:14 | INFO | Reading frame:  652
2026-05-08 17:21:14 | INFO | Reading frame:  653
2026-05-08 17:21:14 | INFO | Reading frame:  654
2026-05-08 17:21:14 | INFO | Reading frame:  655
2026-05-08 17:21:14 | INFO | Reading frame:  656
2026-05-08 17:21:14 | INFO | Reading frame:  657
2026-05-08 17:21:14 | INFO | Reading frame:  658
2026-05-08 17:21:14 | INFO | Reading frame:  659
2026-05-08 17:21:14 | INFO | Reading frame:  660
2026-05-08 17:21:14 | INFO | Reading frame:  661
2026-05-08 17:21:14 | INFO | Reading frame:  662
2026-05-08 17:21:14 | INFO | Reading frame:  663
2026-05-08 17:21:14 | INFO | Reading frame:  664
2026-05-08 17:21:14 | INFO | Reading frame:  665
2026-05-08 17:21:14 | INFO | Reading frame:  666
2026-05-08 17:21:14 | INFO | Reading frame:  667
2026-05-08 17:21:14 | INFO | Reading frame:  668
2026-05-08 17:21:14 | INFO | Reading frame:  669
2026-05-08 17:21:14 | INFO | Reading frame:  670
2026-05-08 17:21:14 | INFO | Reading frame:  671
2026-05-08 17:21:14 | INFO | Reading frame:  672
2026-05-08 17:21:14 | INFO | Reading frame:  673
2026-05-08 17:21:14 | INFO | Reading frame:  674
2026-05-08 17:21:14 | INFO | Reading frame:  675
2026-05-08 17:21:14 | INFO | Reading frame:  676
2026-05-08 17:21:14 | INFO | Reading frame:  677
2026-05-08 17:21:14 | INFO | Reading frame:  678
2026-05-08 17:21:14 | INFO | Reading frame:  679
2026-05-08 17:21:14 | INFO | Reading frame:  680
2026-05-08 17:21:14 | INFO | Reading frame:  681
2026-05-08 17:21:14 | INFO | Reading frame:  682
2026-05-08 17:21:14 | INFO | Reading frame:  683
2026-05-08 17:21:14 | INFO | Reading frame:  684
2026-05-08 17:21:14 | INFO | Reading frame:  685
2026-05-08 17:21:14 | INFO | Reading frame:  686
2026-05-08 17:21:14 | INFO | Reading frame:  687
2026-05-08 17:21:14 | INFO | Reading frame:  688
2026-05-08 17:21:14 | INFO | Reading frame:  689
2026-05-08 17:21:14 | INFO | Reading frame:  690
2026-05-08 17:21:14 | INFO | Reading frame:  691
2026-05-08 17:21:14 | INFO | Reading frame:  692
2026-05-08 17:21:14 | INFO | Reading frame:  693
2026-05-08 17:21:14 | INFO | Reading frame:  694
2026-05-08 17:21:14 | INFO | Reading frame:  695
2026-05-08 17:21:14 | INFO | Reading frame:  696
2026-05-08 17:21:14 | INFO | Reading frame:  697
2026-05-08 17:21:14 | INFO | Reading frame:  698
2026-05-08 17:21:14 | INFO | Reading frame:  699
2026-05-08 17:21:14 | INFO | Reading frame:  700
2026-05-08 17:21:14 | INFO | Reading frame:  701
2026-05-08 17:21:14 | INFO | Reading frame:  702
2026-05-08 17:21:14 | INFO | Reading frame:  703
2026-05-08 17:21:14 | INFO | Reading frame:  704
2026-05-08 17:21:14 | INFO | Reading frame:  705
2026-05-08 17:21:14 | INFO | Reading frame:  706
2026-05-08 17:21:14 | INFO | Reading frame:  707
2026-05-08 17:21:14 | INFO | Reading frame:  708
2026-05-08 17:21:14 | INFO | Reading frame:  709
2026-05-08 17:21:14 | INFO | Reading frame:  710
2026-05-08 17:21:14 | INFO | Reading frame:  711
2026-05-08 17:21:14 | INFO | Reading frame:  712
2026-05-08 17:21:14 | INFO | Reading frame:  713
2026-05-08 17:21:14 | INFO | Reading frame:  714
2026-05-08 17:21:14 | INFO | Reading frame:  715
2026-05-08 17:21:14 | INFO | Reading frame:  716
2026-05-08 17:21:14 | INFO | Reading frame:  717
2026-05-08 17:21:14 | INFO | Reading frame:  718
2026-05-08 17:21:14 | INFO | Reading frame:  719
2026-05-08 17:21:14 | INFO | Reading frame:  720
2026-05-08 17:21:14 | INFO | Reading frame:  721
2026-05-08 17:21:14 | INFO | Reading frame:  722
2026-05-08 17:21:14 | INFO | Reading frame:  723
2026-05-08 17:21:14 | INFO | Reading frame:  724
2026-05-08 17:21:14 | INFO | Reading frame:  725
2026-05-08 17:21:14 | INFO | Reading frame:  726
2026-05-08 17:21:14 | INFO | Reading frame:  727
2026-05-08 17:21:14 | INFO | Reading frame:  728
2026-05-08 17:21:14 | INFO | Reading frame:  729
2026-05-08 17:21:14 | INFO | Reading frame:  730
2026-05-08 17:21:14 | INFO | Reading frame:  731
2026-05-08 17:21:14 | INFO | Reading frame:  732
2026-05-08 17:21:14 | INFO | Reading frame:  733
2026-05-08 17:21:14 | INFO | Reading frame:  734
2026-05-08 17:21:14 | INFO | Reading frame:  735
2026-05-08 17:21:14 | INFO | Reading frame:  736
2026-05-08 17:21:14 | INFO | Reading frame:  737
2026-05-08 17:21:14 | INFO | Reading frame:  738
2026-05-08 17:21:14 | INFO | Reading frame:  739
2026-05-08 17:21:14 | INFO | Reading frame:  740
2026-05-08 17:21:14 | INFO | Reading frame:  741
2026-05-08 17:21:14 | INFO | Reading frame:  742
2026-05-08 17:21:14 | INFO | Reading frame:  743
2026-05-08 17:21:14 | INFO | Reading frame:  744
2026-05-08 17:21:14 | INFO | Reading frame:  745
2026-05-08 17:21:14 | INFO | 🔍 Detecting stable segments...
2026-05-08 17:21:14 | INFO | 
2026-05-08 17:21:14 | INFO | Loading weights:   0%|          | 0/398 [00:00<?, ?it/s]
2026-05-08 17:21:14 | INFO | Loading weights: 100%|██████████| 398/398 [00:00<00:00, 30478.97it/s]
2026-05-08 17:21:14 | INFO | [1mCLIPModel LOAD REPORT[0m from: openai/clip-vit-base-patch32
2026-05-08 17:21:14 | INFO | Key                                  | Status     |  | 
2026-05-08 17:21:14 | INFO | -------------------------------------+------------+--+-
2026-05-08 17:21:14 | INFO | text_model.embeddings.position_ids   | UNEXPECTED |  | 
2026-05-08 17:21:14 | INFO | vision_model.embeddings.position_ids | UNEXPECTED |  | 
2026-05-08 17:21:14 | INFO | 
2026-05-08 17:21:14 | INFO | Notes:
2026-05-08 17:21:14 | INFO | - UNEXPECTED:	can be ignored when loading from different task/architecture; not ok if you expect identical arch.
2026-05-08 17:21:18 | INFO | `use_return_dict` is deprecated! Use `return_dict` instead!
2026-05-08 17:21:19 | INFO | UserWarning: torch.utils.checkpoint: the use_reentrant parameter should be passed explicitly. Starting in PyTorch 2.9, calling checkpoint without use_reentrant will raise an exception. use_reentrant=False is recommended, but if you need to preserve the current default behavior, you can pass use_reentrant=True. Refer to docs for more details on the differences between the two variants.
2026-05-08 17:21:19 | INFO | UserWarning: None of the inputs have requires_grad=True. Gradients will be None
2026-05-08 17:21:24 | INFO | FutureWarning: `torch.cuda.amp.autocast(args...)` is deprecated. Please use `torch.amp.autocast('cuda', args...)` instead.
2026-05-08 17:26:02 | INFO | UserWarning: torch.utils.checkpoint: the use_reentrant parameter should be passed explicitly. Starting in PyTorch 2.9, calling checkpoint without use_reentrant will raise an exception. use_reentrant=False is recommended, but if you need to preserve the current default behavior, you can pass use_reentrant=True. Refer to docs for more details on the differences between the two variants.
2026-05-08 17:26:02 | INFO | UserWarning: None of the inputs have requires_grad=True. Gradients will be None
2026-05-08 17:26:07 | INFO | FutureWarning: `torch.cuda.amp.autocast(args...)` is deprecated. Please use `torch.amp.autocast('cuda', args...)` instead.
2026-05-08 17:27:15 | INFO | UserWarning: torch.utils.checkpoint: the use_reentrant parameter should be passed explicitly. Starting in PyTorch 2.9, calling checkpoint without use_reentrant will raise an exception. use_reentrant=False is recommended, but if you need to preserve the current default behavior, you can pass use_reentrant=True. Refer to docs for more details on the differences between the two variants.
2026-05-08 17:27:15 | INFO | UserWarning: None of the inputs have requires_grad=True. Gradients will be None
2026-05-08 17:27:20 | INFO | FutureWarning: `torch.cuda.amp.autocast(args...)` is deprecated. Please use `torch.amp.autocast('cuda', args...)` instead.
2026-05-08 17:36:01 | INFO | ✅ CLIP similarity list loaded from cache.
2026-05-08 17:36:01 | INFO | 
2026-05-08 17:36:01 | INFO | 📂 Processing segment 0...
2026-05-08 17:36:01 | INFO | Taking screenshot: /sdcard/screenshot-0.png -> /Users/tanmaybhuskute/Documents/gifdroid-reproduction/apps/bily/llm/ViBR_gemini/handheld/run-001/artifacts/hhv-001/step_0_screenshot-0.png
2026-05-08 17:36:01 | INFO | 🔍 Annotated DINO output saved to /Users/tanmaybhuskute/Documents/gifdroid-reproduction/apps/bily/llm/ViBR_gemini/handheld/run-001/artifacts/hhv-001/step_0_dino.png
2026-05-08 17:36:01 | INFO | /Users/tanmaybhuskute/Documents/gifdroid-reproduction/apps/bily/llm/ViBR_gemini/handheld/run-001/artifacts/hhv-001/step_0_dino.png
2026-05-08 17:36:01 | INFO | /Users/tanmaybhuskute/Documents/gifdroid-reproduction/apps/bily/llm/ViBR_gemini/handheld/run-001/artifacts/hhv-001/step_0_tmp_stop.png
2026-05-08 17:36:01 | INFO | Relevant Region Response from Gemini: ```json
2026-05-08 17:36:01 | INFO | {
2026-05-08 17:36:01 | INFO |   "target_regions": [
2026-05-08 17:36:01 | INFO |     4
2026-05-08 17:36:01 | INFO |   ],
2026-05-08 17:36:01 | INFO |   "predicted_action": "tap"
2026-05-08 17:36:01 | INFO | }
2026-05-08 17:36:01 | INFO | ```
2026-05-08 17:36:01 | INFO | 🔍 Relevant regions: {'target_regions': [4], 'predicted_action': 'tap'}
2026-05-08 17:36:01 | INFO | 🧠 GPT selected regions: [4]
2026-05-08 17:36:01 | INFO | ✅ Relevant-only annotation saved to /Users/tanmaybhuskute/Documents/gifdroid-reproduction/apps/bily/llm/ViBR_gemini/handheld/run-001/artifacts/hhv-001/step_0_relevant_regions.png
2026-05-08 17:36:01 | INFO | /Users/tanmaybhuskute/Documents/gifdroid-reproduction/apps/bily/llm/ViBR_gemini/handheld/run-001/artifacts/hhv-001/step_0_relevant_regions.png
2026-05-08 17:36:01 | INFO | /Users/tanmaybhuskute/Documents/gifdroid-reproduction/apps/bily/llm/ViBR_gemini/handheld/run-001/artifacts/hhv-001/step_0_screenshot-0.png
2026-05-08 17:36:01 | INFO | Consistency Response from Gemini: ```json
2026-05-08 17:36:01 | INFO | {
2026-05-08 17:36:01 | INFO |   "same_state": "no",
2026-05-08 17:36:01 | INFO |   "description": "The reference screen shows a dropdown menu with options like 'Modify Bill', 'Reset Bill', and 'Settings', which appeared after tapping the three-dot menu. The current screen does not show this menu, it only shows the state before the tap."
2026-05-08 17:36:01 | INFO | }
2026-05-08 17:36:01 | INFO | ```
2026-05-08 17:36:01 | INFO | 🔄 Attempting to align state (try 1/3)...
2026-05-08 17:36:01 | INFO | /Users/tanmaybhuskute/Documents/gifdroid-reproduction/apps/bily/llm/ViBR_gemini/handheld/run-001/artifacts/hhv-001/step_0_tmp_start.png
2026-05-08 17:36:01 | INFO | /Users/tanmaybhuskute/Documents/gifdroid-reproduction/apps/bily/llm/ViBR_gemini/handheld/run-001/artifacts/hhv-001/step_0_tmp_stop.png
2026-05-08 17:36:01 | INFO | /Users/tanmaybhuskute/Documents/gifdroid-reproduction/apps/bily/llm/ViBR_gemini/handheld/run-001/artifacts/hhv-001/step_0_labeled.png
2026-05-08 17:36:01 | INFO | Region Action Response from Gemini: ```json
2026-05-08 17:36:01 | INFO | {
2026-05-08 17:36:01 | INFO |   "action": "tap",
2026-05-08 17:36:01 | INFO |   "region": 1,
2026-05-08 17:36:01 | INFO |   "description": "Tap the three-dot menu icon in the top right corner, which is next to the 'Global Bill' text."
2026-05-08 17:36:01 | INFO | }
2026-05-08 17:36:01 | INFO | ```
2026-05-08 17:36:01 | INFO | 🎯 Recovery using region index: 1 at (540, 262)
2026-05-08 17:36:01 | INFO | [1] Tap the three-dot menu icon in the top right corner, which is next to the 'Global Bill' text. -> tap
2026-05-08 17:36:01 | INFO | Taking screenshot: /sdcard/screenshot-0.png -> /Users/tanmaybhuskute/Documents/gifdroid-reproduction/apps/bily/llm/ViBR_gemini/handheld/run-001/artifacts/hhv-001/step_0_screenshot-0.png
2026-05-08 17:36:01 | INFO | /Users/tanmaybhuskute/Documents/gifdroid-reproduction/apps/bily/llm/ViBR_gemini/handheld/run-001/artifacts/hhv-001/step_0_tmp_stop.png
2026-05-08 17:36:01 | INFO | /Users/tanmaybhuskute/Documents/gifdroid-reproduction/apps/bily/llm/ViBR_gemini/handheld/run-001/artifacts/hhv-001/step_0_screenshot-0.png
2026-05-08 17:36:01 | INFO | Consistency Response from Gemini: ```json
2026-05-08 17:36:01 | INFO | {
2026-05-08 17:36:01 | INFO |   "same_state": "no",
2026-05-08 17:36:01 | INFO |   "description": "The reference image shows a dropdown menu with options like 'Modify Bill', 'Reset Bill', and 'Settings' which is not present in the current screen. Additionally, the reference screen has user and expense data populated, while the current screen is empty."
2026-05-08 17:36:01 | INFO | }
2026-05-08 17:36:01 | INFO | ```
2026-05-08 17:36:01 | INFO | 🔄 Attempting to align state (try 2/3)...
2026-05-08 17:36:01 | INFO | /Users/tanmaybhuskute/Documents/gifdroid-reproduction/apps/bily/llm/ViBR_gemini/handheld/run-001/artifacts/hhv-001/step_0_tmp_start.png
2026-05-08 17:36:01 | INFO | /Users/tanmaybhuskute/Documents/gifdroid-reproduction/apps/bily/llm/ViBR_gemini/handheld/run-001/artifacts/hhv-001/step_0_tmp_stop.png
2026-05-08 17:36:01 | INFO | /Users/tanmaybhuskute/Documents/gifdroid-reproduction/apps/bily/llm/ViBR_gemini/handheld/run-001/artifacts/hhv-001/step_0_labeled.png
2026-05-08 17:36:01 | INFO | Region Action Response from Gemini: ```json
2026-05-08 17:36:01 | INFO | {
2026-05-08 17:36:01 | INFO |   "action": "tap",
2026-05-08 17:36:01 | INFO |   "description": "Tap the three-dot menu icon in the top right corner."
2026-05-08 17:36:01 | INFO | }
2026-05-08 17:36:01 | INFO | ```
2026-05-08 17:36:01 | INFO | ⚠️ Recovery: no position resolved, skipping action.
2026-05-08 17:36:01 | INFO | 🔄 Attempting to align state (try 3/3)...
2026-05-08 17:36:01 | INFO | /Users/tanmaybhuskute/Documents/gifdroid-reproduction/apps/bily/llm/ViBR_gemini/handheld/run-001/artifacts/hhv-001/step_0_tmp_start.png
2026-05-08 17:36:01 | INFO | /Users/tanmaybhuskute/Documents/gifdroid-reproduction/apps/bily/llm/ViBR_gemini/handheld/run-001/artifacts/hhv-001/step_0_tmp_stop.png
2026-05-08 17:36:01 | INFO | /Users/tanmaybhuskute/Documents/gifdroid-reproduction/apps/bily/llm/ViBR_gemini/handheld/run-001/artifacts/hhv-001/step_0_labeled.png
2026-05-08 17:36:01 | INFO | Region Action Response from Gemini: ```json
2026-05-08 17:36:01 | INFO | {
2026-05-08 17:36:01 | INFO |     "action": "tap",
2026-05-08 17:36:01 | INFO |     "region": 1,
2026-05-08 17:36:01 | INFO |     "description": "Tap on the three-dot menu icon."
2026-05-08 17:36:01 | INFO | }
2026-05-08 17:36:01 | INFO | ```
2026-05-08 17:36:01 | INFO | 🎯 Recovery using region index: 1 at (540, 262)
2026-05-08 17:36:01 | INFO | [1] Tap on the three-dot menu icon. -> tap
2026-05-08 17:36:01 | INFO | Taking screenshot: /sdcard/screenshot-0.png -> /Users/tanmaybhuskute/Documents/gifdroid-reproduction/apps/bily/llm/ViBR_gemini/handheld/run-001/artifacts/hhv-001/step_0_screenshot-0.png
2026-05-08 17:36:01 | INFO | /Users/tanmaybhuskute/Documents/gifdroid-reproduction/apps/bily/llm/ViBR_gemini/handheld/run-001/artifacts/hhv-001/step_0_tmp_stop.png
2026-05-08 17:36:01 | INFO | /Users/tanmaybhuskute/Documents/gifdroid-reproduction/apps/bily/llm/ViBR_gemini/handheld/run-001/artifacts/hhv-001/step_0_screenshot-0.png
2026-05-08 17:36:01 | INFO | Consistency Response from Gemini: ```json
2026-05-08 17:36:01 | INFO | {
2026-05-08 17:36:01 | INFO |   "same_state": "no",
2026-05-08 17:36:01 | INFO |   "description": "The reference image shows an open options menu with 'Modify Bill', 'Reset Bill', and 'Settings' visible. The current image does not have this menu open, and the options are not visible."
2026-05-08 17:36:01 | INFO | }
2026-05-08 17:36:01 | INFO | ```
2026-05-08 17:36:01 | INFO | ⚠️ Skipping action: current GUI state does not match start state.
2026-05-08 17:36:01 | INFO | Mismatch reason: the reference image shows an open options menu with 'modify bill', 'reset bill', and 'settings' visible. the current image does not have this menu open, and the options are not visible.
2026-05-08 17:36:01 | INFO | 
2026-05-08 17:36:01 | INFO | 📂 Processing segment 1...
2026-05-08 17:36:01 | INFO | Taking screenshot: /sdcard/screenshot-0.png -> /Users/tanmaybhuskute/Documents/gifdroid-reproduction/apps/bily/llm/ViBR_gemini/handheld/run-001/artifacts/hhv-001/step_1_screenshot-0.png
2026-05-08 17:36:01 | INFO | 🔍 Annotated DINO output saved to /Users/tanmaybhuskute/Documents/gifdroid-reproduction/apps/bily/llm/ViBR_gemini/handheld/run-001/artifacts/hhv-001/step_1_dino.png
2026-05-08 17:36:01 | INFO | /Users/tanmaybhuskute/Documents/gifdroid-reproduction/apps/bily/llm/ViBR_gemini/handheld/run-001/artifacts/hhv-001/step_1_dino.png
2026-05-08 17:36:01 | INFO | /Users/tanmaybhuskute/Documents/gifdroid-reproduction/apps/bily/llm/ViBR_gemini/handheld/run-001/artifacts/hhv-001/step_1_tmp_stop.png
2026-05-08 17:36:01 | INFO | Relevant Region Response from Gemini: ```json
2026-05-08 17:36:01 | INFO | {
2026-05-08 17:36:01 | INFO |   "target_regions": [],
2026-05-08 17:36:01 | INFO |   "predicted_action": "no action"
2026-05-08 17:36:01 | INFO | }
2026-05-08 17:36:01 | INFO | ```
2026-05-08 17:36:01 | INFO | 🔍 Relevant regions: {'target_regions': [], 'predicted_action': 'no action'}
2026-05-08 17:36:01 | INFO | 🧠 GPT selected regions: []
2026-05-08 17:36:01 | INFO | ⚠️ No relevant regions to annotate.
2026-05-08 17:36:01 | INFO | /Users/tanmaybhuskute/Documents/gifdroid-reproduction/apps/bily/llm/ViBR_gemini/handheld/run-001/artifacts/hhv-001/step_1_relevant_regions.png
2026-05-08 17:36:01 | INFO | /Users/tanmaybhuskute/Documents/gifdroid-reproduction/apps/bily/llm/ViBR_gemini/handheld/run-001/artifacts/hhv-001/step_1_screenshot-0.png
2026-05-08 17:36:01 | INFO | Consistency Response from Gemini: ```json
2026-05-08 17:36:01 | INFO | {
2026-05-08 17:36:01 | INFO |   "same_state": "no",
2026-05-08 17:36:01 | INFO |   "description": "The reference screen displays two users, 'Ygb' and 'Tfc', under the 'Balance Per User' section. The current screen does not show any users in that section, indicating a different data state."
2026-05-08 17:36:01 | INFO | }
2026-05-08 17:36:01 | INFO | ```
2026-05-08 17:36:01 | INFO | 🔄 Attempting to align state (try 1/3)...
2026-05-08 17:36:01 | INFO | /Users/tanmaybhuskute/Documents/gifdroid-reproduction/apps/bily/llm/ViBR_gemini/handheld/run-001/artifacts/hhv-001/step_1_tmp_start.png
2026-05-08 17:36:01 | INFO | /Users/tanmaybhuskute/Documents/gifdroid-reproduction/apps/bily/llm/ViBR_gemini/handheld/run-001/artifacts/hhv-001/step_1_tmp_stop.png
2026-05-08 17:36:01 | INFO | /Users/tanmaybhuskute/Documents/gifdroid-reproduction/apps/bily/llm/ViBR_gemini/handheld/run-001/artifacts/hhv-001/step_1_labeled.png
2026-05-08 17:36:01 | INFO | Region Action Response from Gemini: ```json
2026-05-08 17:36:01 | INFO | {
2026-05-08 17:36:01 | INFO |   "action": "no action",
2026-05-08 17:36:01 | INFO |   "description": "No Action needed."
2026-05-08 17:36:01 | INFO | }
2026-05-08 17:36:01 | INFO | ```
2026-05-08 17:36:01 | INFO | [1] No Action needed. -> no action
2026-05-08 17:36:01 | INFO | Taking screenshot: /sdcard/screenshot-0.png -> /Users/tanmaybhuskute/Documents/gifdroid-reproduction/apps/bily/llm/ViBR_gemini/handheld/run-001/artifacts/hhv-001/step_1_screenshot-0.png
2026-05-08 17:36:01 | INFO | /Users/tanmaybhuskute/Documents/gifdroid-reproduction/apps/bily/llm/ViBR_gemini/handheld/run-001/artifacts/hhv-001/step_1_tmp_stop.png
2026-05-08 17:36:01 | INFO | /Users/tanmaybhuskute/Documents/gifdroid-reproduction/apps/bily/llm/ViBR_gemini/handheld/run-001/artifacts/hhv-001/step_1_screenshot-0.png
2026-05-08 17:36:01 | INFO | Consistency Response from Gemini: ```json
2026-05-08 17:36:01 | INFO | {
2026-05-08 17:36:01 | INFO |   "same_state": "no",
2026-05-08 17:36:01 | INFO |   "description": "The reference screen displays a list of users ('Ygb', 'Tfc') under the 'Balance Per User' section, which are not present in the current screen. This indicates a different state in the app's data, and actions related to these specific users cannot be performed from the current screen."
2026-05-08 17:36:01 | INFO | }
2026-05-08 17:36:01 | INFO | ```
2026-05-08 17:36:01 | INFO | 🔄 Attempting to align state (try 2/3)...
2026-05-08 17:36:01 | INFO | /Users/tanmaybhuskute/Documents/gifdroid-reproduction/apps/bily/llm/ViBR_gemini/handheld/run-001/artifacts/hhv-001/step_1_tmp_start.png
2026-05-08 17:36:01 | INFO | /Users/tanmaybhuskute/Documents/gifdroid-reproduction/apps/bily/llm/ViBR_gemini/handheld/run-001/artifacts/hhv-001/step_1_tmp_stop.png
2026-05-08 17:36:01 | INFO | /Users/tanmaybhuskute/Documents/gifdroid-reproduction/apps/bily/llm/ViBR_gemini/handheld/run-001/artifacts/hhv-001/step_1_labeled.png
2026-05-08 17:36:01 | INFO | Region Action Response from Gemini: ```json
2026-05-08 17:36:01 | INFO | {
2026-05-08 17:36:01 | INFO |   "action": "no action",
2026-05-08 17:36:01 | INFO |   "description": "No Action needed."
2026-05-08 17:36:01 | INFO | }
2026-05-08 17:36:01 | INFO | ```
2026-05-08 17:36:01 | INFO | [1] No Action needed. -> no action
2026-05-08 17:36:01 | INFO | Taking screenshot: /sdcard/screenshot-0.png -> /Users/tanmaybhuskute/Documents/gifdroid-reproduction/apps/bily/llm/ViBR_gemini/handheld/run-001/artifacts/hhv-001/step_1_screenshot-0.png
2026-05-08 17:36:01 | INFO | /Users/tanmaybhuskute/Documents/gifdroid-reproduction/apps/bily/llm/ViBR_gemini/handheld/run-001/artifacts/hhv-001/step_1_tmp_stop.png
2026-05-08 17:36:01 | INFO | /Users/tanmaybhuskute/Documents/gifdroid-reproduction/apps/bily/llm/ViBR_gemini/handheld/run-001/artifacts/hhv-001/step_1_screenshot-0.png
2026-05-08 17:36:01 | INFO | Consistency Response from Gemini: ```json
2026-05-08 17:36:01 | INFO | {
2026-05-08 17:36:01 | INFO |   "same_state": "yes"
2026-05-08 17:36:01 | INFO | }
2026-05-08 17:36:01 | INFO | ```
2026-05-08 17:36:01 | INFO | /Users/tanmaybhuskute/Documents/gifdroid-reproduction/apps/bily/llm/ViBR_gemini/handheld/run-001/artifacts/hhv-001/step_1_relevant_regions.png
2026-05-08 17:36:01 | INFO | /Users/tanmaybhuskute/Documents/gifdroid-reproduction/apps/bily/llm/ViBR_gemini/handheld/run-001/artifacts/hhv-001/step_1_tmp_stop.png
2026-05-08 17:36:01 | INFO | /Users/tanmaybhuskute/Documents/gifdroid-reproduction/apps/bily/llm/ViBR_gemini/handheld/run-001/artifacts/hhv-001/step_1_labeled.png
2026-05-08 17:36:01 | INFO | Region Action Response from Gemini: ```json
2026-05-08 17:36:01 | INFO | {
2026-05-08 17:36:01 | INFO |   "action": "no action",
2026-05-08 17:36:01 | INFO |   "description": "No Action needed."
2026-05-08 17:36:01 | INFO | }
2026-05-08 17:36:01 | INFO | ```
2026-05-08 17:36:01 | INFO | ⚠️ No valid region or element match. Proceeding without position.
2026-05-08 17:36:01 | INFO | [1] No Action needed. -> no action
2026-05-08 17:36:01 | INFO | ✅ Action executed.
2026-05-08 17:36:01 | INFO | 
2026-05-08 17:36:01 | INFO | 
2026-05-08 17:36:01 | INFO | 📂 Processing segment 2...
2026-05-08 17:36:01 | INFO | Taking screenshot: /sdcard/screenshot-0.png -> /Users/tanmaybhuskute/Documents/gifdroid-reproduction/apps/bily/llm/ViBR_gemini/handheld/run-001/artifacts/hhv-001/step_2_screenshot-0.png
2026-05-08 17:36:01 | INFO | 🔍 Annotated DINO output saved to /Users/tanmaybhuskute/Documents/gifdroid-reproduction/apps/bily/llm/ViBR_gemini/handheld/run-001/artifacts/hhv-001/step_2_dino.png
2026-05-08 17:36:01 | INFO | /Users/tanmaybhuskute/Documents/gifdroid-reproduction/apps/bily/llm/ViBR_gemini/handheld/run-001/artifacts/hhv-001/step_2_dino.png
2026-05-08 17:36:01 | INFO | /Users/tanmaybhuskute/Documents/gifdroid-reproduction/apps/bily/llm/ViBR_gemini/handheld/run-001/artifacts/hhv-001/step_2_tmp_stop.png
2026-05-08 17:36:01 | INFO | Relevant Region Response from Gemini: ```json
2026-05-08 17:36:01 | INFO | {
2026-05-08 17:36:01 | INFO |   "target_regions": [5],
2026-05-08 17:36:01 | INFO |   "predicted_action": "tap"
2026-05-08 17:36:01 | INFO | }
2026-05-08 17:36:01 | INFO | ```
2026-05-08 17:36:01 | INFO | 🔍 Relevant regions: {'target_regions': [5], 'predicted_action': 'tap'}
2026-05-08 17:36:01 | INFO | 🧠 GPT selected regions: [5]
2026-05-08 17:36:01 | INFO | ✅ Relevant-only annotation saved to /Users/tanmaybhuskute/Documents/gifdroid-reproduction/apps/bily/llm/ViBR_gemini/handheld/run-001/artifacts/hhv-001/step_2_relevant_regions.png
2026-05-08 17:36:01 | INFO | /Users/tanmaybhuskute/Documents/gifdroid-reproduction/apps/bily/llm/ViBR_gemini/handheld/run-001/artifacts/hhv-001/step_2_relevant_regions.png
2026-05-08 17:36:01 | INFO | /Users/tanmaybhuskute/Documents/gifdroid-reproduction/apps/bily/llm/ViBR_gemini/handheld/run-001/artifacts/hhv-001/step_2_screenshot-0.png
2026-05-08 17:36:01 | INFO | Consistency Response from Gemini: ```json
2026-05-08 17:36:01 | INFO | {
2026-05-08 17:36:01 | INFO |   "same_state": "no",
2026-05-08 17:36:01 | INFO |   "description": "The reference screen shows a populated list with users ('Ygb', 'Tfc') under 'Balance Per User' and has a 'Settings' icon. The current screen is an empty state with no users listed and features different UI elements, such as a three-dot menu in the top right and add icons next to 'Balance Per User' and 'Expenses'. The text input field indicated in the reference image is also missing from the current screen."
2026-05-08 17:36:01 | INFO | }
2026-05-08 17:36:01 | INFO | ```
2026-05-08 17:36:01 | INFO | 🔄 Attempting to align state (try 1/3)...
2026-05-08 17:36:01 | INFO | /Users/tanmaybhuskute/Documents/gifdroid-reproduction/apps/bily/llm/ViBR_gemini/handheld/run-001/artifacts/hhv-001/step_2_tmp_start.png
2026-05-08 17:36:01 | INFO | /Users/tanmaybhuskute/Documents/gifdroid-reproduction/apps/bily/llm/ViBR_gemini/handheld/run-001/artifacts/hhv-001/step_2_tmp_stop.png
2026-05-08 17:36:01 | INFO | /Users/tanmaybhuskute/Documents/gifdroid-reproduction/apps/bily/llm/ViBR_gemini/handheld/run-001/artifacts/hhv-001/step_2_labeled.png
2026-05-08 17:36:01 | INFO | Gemini request timed out (attempt 1/5). Retrying in 10s...
2026-05-08 17:36:01 | INFO | Region Action Response from Gemini: ```json
2026-05-08 17:36:01 | INFO | {
2026-05-08 17:36:01 | INFO |     "action": "tap",
2026-05-08 17:36:01 | INFO |     "region": 1,
2026-05-08 17:36:01 | INFO |     "description": "Tap on the three-dot menu icon in the top right corner, which is on the same line as 'Global Bill'."
2026-05-08 17:36:01 | INFO | }
2026-05-08 17:36:01 | INFO | ```
2026-05-08 17:36:01 | INFO | 🎯 Recovery using region index: 1 at (540, 262)
2026-05-08 17:36:01 | INFO | [1] Tap on the three-dot menu icon in the top right corner, which is on the same line as 'Global Bill'. -> tap
2026-05-08 17:36:01 | INFO | Taking screenshot: /sdcard/screenshot-0.png -> /Users/tanmaybhuskute/Documents/gifdroid-reproduction/apps/bily/llm/ViBR_gemini/handheld/run-001/artifacts/hhv-001/step_2_screenshot-0.png
2026-05-08 17:36:01 | INFO | /Users/tanmaybhuskute/Documents/gifdroid-reproduction/apps/bily/llm/ViBR_gemini/handheld/run-001/artifacts/hhv-001/step_2_tmp_stop.png
2026-05-08 17:36:01 | INFO | /Users/tanmaybhuskute/Documents/gifdroid-reproduction/apps/bily/llm/ViBR_gemini/handheld/run-001/artifacts/hhv-001/step_2_screenshot-0.png
2026-05-08 17:36:01 | INFO | Consistency Response from Gemini: ```json
2026-05-08 17:36:01 | INFO | {
2026-05-08 17:36:01 | INFO |   "same_state": "no",
2026-05-08 17:36:01 | INFO |   "description": "The reference image shows a dropdown menu with options 'Modify Bill', 'Reset Bill', and 'Settings' after the three-dot menu has been tapped. The current image does not have this menu open."
2026-05-08 17:36:01 | INFO | }
2026-05-08 17:36:01 | INFO | ```
2026-05-08 17:36:01 | INFO | 🔄 Attempting to align state (try 2/3)...
2026-05-08 17:36:01 | INFO | /Users/tanmaybhuskute/Documents/gifdroid-reproduction/apps/bily/llm/ViBR_gemini/handheld/run-001/artifacts/hhv-001/step_2_tmp_start.png
2026-05-08 17:36:01 | INFO | /Users/tanmaybhuskute/Documents/gifdroid-reproduction/apps/bily/llm/ViBR_gemini/handheld/run-001/artifacts/hhv-001/step_2_tmp_stop.png
2026-05-08 17:36:01 | INFO | /Users/tanmaybhuskute/Documents/gifdroid-reproduction/apps/bily/llm/ViBR_gemini/handheld/run-001/artifacts/hhv-001/step_2_labeled.png
2026-05-08 17:36:01 | INFO | Gemini request timed out (attempt 1/5). Retrying in 10s...
2026-05-08 17:36:01 | INFO | Traceback (most recent call last):
2026-05-08 17:36:01 | INFO |   File "/opt/homebrew/Cellar/python@3.13/3.13.7/Frameworks/Python.framework/Versions/3.13/lib/python3.13/urllib/request.py", line 1319, in do_open
2026-05-08 17:36:01 | INFO |     h.request(req.get_method(), req.selector, req.data, headers,
2026-05-08 17:36:01 | INFO |     ~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
2026-05-08 17:36:01 | INFO |               encode_chunked=req.has_header('Transfer-encoding'))
2026-05-08 17:36:01 | INFO |               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
2026-05-08 17:36:01 | INFO |   File "/opt/homebrew/Cellar/python@3.13/3.13.7/Frameworks/Python.framework/Versions/3.13/lib/python3.13/http/client.py", line 1338, in request
2026-05-08 17:36:01 | INFO |     self._send_request(method, url, body, headers, encode_chunked)
2026-05-08 17:36:01 | INFO |     ~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
2026-05-08 17:36:01 | INFO |   File "/opt/homebrew/Cellar/python@3.13/3.13.7/Frameworks/Python.framework/Versions/3.13/lib/python3.13/http/client.py", line 1384, in _send_request
2026-05-08 17:36:01 | INFO |     self.endheaders(body, encode_chunked=encode_chunked)
2026-05-08 17:36:01 | INFO |     ~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
2026-05-08 17:36:01 | INFO |   File "/opt/homebrew/Cellar/python@3.13/3.13.7/Frameworks/Python.framework/Versions/3.13/lib/python3.13/http/client.py", line 1333, in endheaders
2026-05-08 17:36:01 | INFO |     self._send_output(message_body, encode_chunked=encode_chunked)
2026-05-08 17:36:01 | INFO |     ~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
2026-05-08 17:36:01 | INFO |   File "/opt/homebrew/Cellar/python@3.13/3.13.7/Frameworks/Python.framework/Versions/3.13/lib/python3.13/http/client.py", line 1093, in _send_output
2026-05-08 17:36:01 | INFO |     self.send(msg)
2026-05-08 17:36:01 | INFO |     ~~~~~~~~~^^^^^
2026-05-08 17:36:01 | INFO |   File "/opt/homebrew/Cellar/python@3.13/3.13.7/Frameworks/Python.framework/Versions/3.13/lib/python3.13/http/client.py", line 1037, in send
2026-05-08 17:36:01 | INFO |     self.connect()
2026-05-08 17:36:01 | INFO |     ~~~~~~~~~~~~^^
2026-05-08 17:36:01 | INFO |   File "/opt/homebrew/Cellar/python@3.13/3.13.7/Frameworks/Python.framework/Versions/3.13/lib/python3.13/http/client.py", line 1472, in connect
2026-05-08 17:36:01 | INFO |     super().connect()
2026-05-08 17:36:01 | INFO |     ~~~~~~~~~~~~~~~^^
2026-05-08 17:36:01 | INFO |   File "/opt/homebrew/Cellar/python@3.13/3.13.7/Frameworks/Python.framework/Versions/3.13/lib/python3.13/http/client.py", line 1003, in connect
2026-05-08 17:36:01 | INFO |     self.sock = self._create_connection(
2026-05-08 17:36:01 | INFO |                 ~~~~~~~~~~~~~~~~~~~~~~~^
2026-05-08 17:36:01 | INFO |         (self.host,self.port), self.timeout, self.source_address)
2026-05-08 17:36:01 | INFO |         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
2026-05-08 17:36:01 | INFO |   File "/opt/homebrew/Cellar/python@3.13/3.13.7/Frameworks/Python.framework/Versions/3.13/lib/python3.13/socket.py", line 840, in create_connection
2026-05-08 17:36:01 | INFO |     for res in getaddrinfo(host, port, 0, SOCK_STREAM):
2026-05-08 17:36:01 | INFO |                ~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^
2026-05-08 17:36:01 | INFO |   File "/opt/homebrew/Cellar/python@3.13/3.13.7/Frameworks/Python.framework/Versions/3.13/lib/python3.13/socket.py", line 977, in getaddrinfo
2026-05-08 17:36:01 | INFO |     for res in _socket.getaddrinfo(host, port, family, type, proto, flags):
2026-05-08 17:36:01 | INFO |                ~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
2026-05-08 17:36:01 | INFO | socket.gaierror: [Errno 8] nodename nor servname provided, or not known
2026-05-08 17:36:01 | INFO | 
2026-05-08 17:36:01 | INFO | During handling of the above exception, another exception occurred:
2026-05-08 17:36:01 | INFO | 
2026-05-08 17:36:01 | INFO | Traceback (most recent call last):
2026-05-08 17:36:01 | INFO |   File "/Users/tanmaybhuskute/Documents/gifdroid-reproduction/src_ViBR/approach/gemini_api.py", line 151, in _call_gemini
2026-05-08 17:36:01 | INFO |     with url_request.urlopen(req, timeout=timeout) as resp:
2026-05-08 17:36:01 | INFO |          ~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^
2026-05-08 17:36:01 | INFO |   File "/opt/homebrew/Cellar/python@3.13/3.13.7/Frameworks/Python.framework/Versions/3.13/lib/python3.13/urllib/request.py", line 189, in urlopen
2026-05-08 17:36:01 | INFO |     return opener.open(url, data, timeout)
2026-05-08 17:36:01 | INFO |            ~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^
2026-05-08 17:36:01 | INFO |   File "/opt/homebrew/Cellar/python@3.13/3.13.7/Frameworks/Python.framework/Versions/3.13/lib/python3.13/urllib/request.py", line 489, in open
2026-05-08 17:36:01 | INFO |     response = self._open(req, data)
2026-05-08 17:36:01 | INFO |   File "/opt/homebrew/Cellar/python@3.13/3.13.7/Frameworks/Python.framework/Versions/3.13/lib/python3.13/urllib/request.py", line 506, in _open
2026-05-08 17:36:01 | INFO |     result = self._call_chain(self.handle_open, protocol, protocol +
2026-05-08 17:36:01 | INFO |                               '_open', req)
2026-05-08 17:36:01 | INFO |   File "/opt/homebrew/Cellar/python@3.13/3.13.7/Frameworks/Python.framework/Versions/3.13/lib/python3.13/urllib/request.py", line 466, in _call_chain
2026-05-08 17:36:01 | INFO |     result = func(*args)
2026-05-08 17:36:01 | INFO |   File "/opt/homebrew/Cellar/python@3.13/3.13.7/Frameworks/Python.framework/Versions/3.13/lib/python3.13/urllib/request.py", line 1367, in https_open
2026-05-08 17:36:01 | INFO |     return self.do_open(http.client.HTTPSConnection, req,
2026-05-08 17:36:01 | INFO |            ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
2026-05-08 17:36:01 | INFO |                         context=self._context)
2026-05-08 17:36:01 | INFO |                         ^^^^^^^^^^^^^^^^^^^^^^
2026-05-08 17:36:01 | INFO |   File "/opt/homebrew/Cellar/python@3.13/3.13.7/Frameworks/Python.framework/Versions/3.13/lib/python3.13/urllib/request.py", line 1322, in do_open
2026-05-08 17:36:01 | INFO |     raise URLError(err)
2026-05-08 17:36:01 | INFO | urllib.error.URLError: <urlopen error [Errno 8] nodename nor servname provided, or not known>
2026-05-08 17:36:01 | INFO | 
2026-05-08 17:36:01 | INFO | The above exception was the direct cause of the following exception:
2026-05-08 17:36:01 | INFO | 
2026-05-08 17:36:01 | INFO | Traceback (most recent call last):
2026-05-08 17:36:01 | INFO |   File "/Users/tanmaybhuskute/Documents/gifdroid-reproduction/src_ViBR/approach/segment_replay.py", line 586, in <module>
2026-05-08 17:36:01 | INFO |     main(
2026-05-08 17:36:01 | INFO |     ~~~~^
2026-05-08 17:36:01 | INFO |         args.video_path,
2026-05-08 17:36:01 | INFO |         ^^^^^^^^^^^^^^^^
2026-05-08 17:36:01 | INFO |     ...<6 lines>...
2026-05-08 17:36:01 | INFO |         app_name=args.app_name,
2026-05-08 17:36:01 | INFO |         ^^^^^^^^^^^^^^^^^^^^^^^
2026-05-08 17:36:01 | INFO |     )
2026-05-08 17:36:01 | INFO |     ^
2026-05-08 17:36:01 | INFO |   File "/Users/tanmaybhuskute/Documents/gifdroid-reproduction/src_ViBR/approach/segment_replay.py", line 441, in main
2026-05-08 17:36:01 | INFO |     recovery_reply = provider.ask_gpt_for_action_region(
2026-05-08 17:36:01 | INFO |         tmp_start_path, tmp_stop_path, labeled_path, relevant["predicted_action"],
2026-05-08 17:36:01 | INFO |     )
2026-05-08 17:36:01 | INFO |   File "/Users/tanmaybhuskute/Documents/gifdroid-reproduction/src_ViBR/approach/gemini_api.py", line 322, in ask_gpt_for_action_region
2026-05-08 17:36:01 | INFO |     response = _call_gemini(parts, kind="action_inference")
2026-05-08 17:36:01 | INFO |   File "/Users/tanmaybhuskute/Documents/gifdroid-reproduction/src_ViBR/approach/gemini_api.py", line 170, in _call_gemini
2026-05-08 17:36:01 | INFO |     raise RuntimeError(f"Gemini URL error: {exc}") from exc
2026-05-08 17:36:01 | INFO | RuntimeError: Gemini URL error: <urlopen error [Errno 8] nodename nor servname provided, or not known>
2026-05-08 17:36:03 | INFO | ========================================================================
RUN SUMMARY
  App         : bily
  Video type  : handheld
  Status      : failed
  Scenes      : 0/0
  Actions     : none
  LLM calls   : n/a
  LLM latency : n/a
  Tokens used : n/a
  Wall time   : 15m 5s
========================================================================

```
