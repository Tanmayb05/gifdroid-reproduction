# ViBR Run Log

**Status**: SUCCESS

## Full Log

```
2026-05-08 14:00:38 | INFO | === src_vibr.2026-05-08T18-00-38__run-008__pipeline__started ===
2026-05-08 14:00:38 | INFO | Starting ViBR run
2026-05-08 14:00:38 | INFO | App: antennapod
2026-05-08 14:00:38 | INFO | Video: /Users/tanmaybhuskute/Documents/gifdroid-reproduction/apps/antennapod/videos/hhv-002.mp4
2026-05-08 14:00:38 | INFO | Algorithm: clip
2026-05-08 14:00:38 | INFO | LLM: gemini (gemini-2.5-pro)
2026-05-08 14:00:38 | INFO | Output: /Users/tanmaybhuskute/Documents/gifdroid-reproduction/apps/antennapod/llm/ViBR_gemini/handheld/run-008
2026-05-08 14:00:42 | INFO | FutureWarning: Importing from timm.models.layers is deprecated, please import via timm.layers
2026-05-08 14:00:42 | INFO | UserWarning: Failed to load custom C++ ops. Running on CPU mode Only!
2026-05-08 14:00:42 | INFO | UserWarning: torch.meshgrid: in an upcoming release, it will be required to pass the indexing argument. (Triggered internally at /Users/runner/work/pytorch/pytorch/pytorch/aten/src/ATen/native/TensorShape.cpp:4383.)
2026-05-08 14:00:43 | INFO | Warning: You are sending unauthenticated requests to the HF Hub. Please set a HF_TOKEN to enable higher rate limits and faster downloads.
2026-05-08 14:00:44 | INFO | final text_encoder_type: bert-base-uncased
2026-05-08 14:00:44 | INFO | 
2026-05-08 14:00:44 | INFO | Loading weights:   0%|          | 0/199 [00:00<?, ?it/s]
2026-05-08 14:00:44 | INFO | Loading weights: 100%|██████████| 199/199 [00:00<00:00, 14992.84it/s]
2026-05-08 14:00:44 | INFO | [1mBertModel LOAD REPORT[0m from: bert-base-uncased
2026-05-08 14:00:44 | INFO | Key                                        | Status     |  | 
2026-05-08 14:00:44 | INFO | -------------------------------------------+------------+--+-
2026-05-08 14:00:44 | INFO | cls.predictions.transform.dense.weight     | UNEXPECTED |  | 
2026-05-08 14:00:44 | INFO | cls.seq_relationship.weight                | UNEXPECTED |  | 
2026-05-08 14:00:44 | INFO | cls.predictions.transform.LayerNorm.weight | UNEXPECTED |  | 
2026-05-08 14:00:44 | INFO | cls.seq_relationship.bias                  | UNEXPECTED |  | 
2026-05-08 14:00:44 | INFO | cls.predictions.bias                       | UNEXPECTED |  | 
2026-05-08 14:00:44 | INFO | cls.predictions.transform.dense.bias       | UNEXPECTED |  | 
2026-05-08 14:00:44 | INFO | cls.predictions.transform.LayerNorm.bias   | UNEXPECTED |  | 
2026-05-08 14:00:44 | INFO | 
2026-05-08 14:00:44 | INFO | Notes:
2026-05-08 14:00:44 | INFO | - UNEXPECTED:	can be ignored when loading from different task/architecture; not ok if you expect identical arch.
2026-05-08 14:00:54 | INFO | 🔹 Starting video processing (algorithm=clip, llm=gemini, model=gemini-2.5-pro)...
2026-05-08 14:00:54 | INFO | Initializing ADB device controller...
2026-05-08 14:00:54 | INFO | 📱 Preparing device for app: antennapod
2026-05-08 14:00:54 | INFO | 🏠 Going to home screen...
2026-05-08 14:00:54 | INFO | 🚀 Opening app 'antennapod' with command: am start -n de.danoeh.antennapod/.activity.SplashActivity
2026-05-08 14:00:54 | INFO | ✅ App 'antennapod' opened and ready
2026-05-08 14:00:54 | INFO | Taking screenshot: /sdcard/screenshot-0.png -> /Users/tanmaybhuskute/Documents/gifdroid-reproduction/apps/antennapod/llm/ViBR_gemini/handheld/run-008/artifacts/hhv-002/screenshot-0.png
2026-05-08 14:00:54 | INFO | Reading frames from video...
2026-05-08 14:00:54 | INFO | Reading frame:  2
2026-05-08 14:00:54 | INFO | Reading frame:  3
2026-05-08 14:00:54 | INFO | Reading frame:  4
2026-05-08 14:00:54 | INFO | Reading frame:  5
2026-05-08 14:00:54 | INFO | Reading frame:  6
2026-05-08 14:00:54 | INFO | Reading frame:  7
2026-05-08 14:00:54 | INFO | Reading frame:  8
2026-05-08 14:00:54 | INFO | Reading frame:  9
2026-05-08 14:00:54 | INFO | Reading frame:  10
2026-05-08 14:00:54 | INFO | Reading frame:  11
2026-05-08 14:00:54 | INFO | Reading frame:  12
2026-05-08 14:00:54 | INFO | Reading frame:  13
2026-05-08 14:00:54 | INFO | Reading frame:  14
2026-05-08 14:00:54 | INFO | Reading frame:  15
2026-05-08 14:00:54 | INFO | Reading frame:  16
2026-05-08 14:00:54 | INFO | Reading frame:  17
2026-05-08 14:00:54 | INFO | Reading frame:  18
2026-05-08 14:00:54 | INFO | Reading frame:  19
2026-05-08 14:00:54 | INFO | Reading frame:  20
2026-05-08 14:00:54 | INFO | Reading frame:  21
2026-05-08 14:00:54 | INFO | Reading frame:  22
2026-05-08 14:00:54 | INFO | Reading frame:  23
2026-05-08 14:00:54 | INFO | Reading frame:  24
2026-05-08 14:00:54 | INFO | Reading frame:  25
2026-05-08 14:00:54 | INFO | Reading frame:  26
2026-05-08 14:00:54 | INFO | Reading frame:  27
2026-05-08 14:00:54 | INFO | Reading frame:  28
2026-05-08 14:00:54 | INFO | Reading frame:  29
2026-05-08 14:00:54 | INFO | Reading frame:  30
2026-05-08 14:00:54 | INFO | Reading frame:  31
2026-05-08 14:00:54 | INFO | Reading frame:  32
2026-05-08 14:00:54 | INFO | Reading frame:  33
2026-05-08 14:00:54 | INFO | Reading frame:  34
2026-05-08 14:00:54 | INFO | Reading frame:  35
2026-05-08 14:00:54 | INFO | Reading frame:  36
2026-05-08 14:00:54 | INFO | Reading frame:  37
2026-05-08 14:00:54 | INFO | Reading frame:  38
2026-05-08 14:00:54 | INFO | Reading frame:  39
2026-05-08 14:00:54 | INFO | Reading frame:  40
2026-05-08 14:00:54 | INFO | Reading frame:  41
2026-05-08 14:00:54 | INFO | Reading frame:  42
2026-05-08 14:00:54 | INFO | Reading frame:  43
2026-05-08 14:00:54 | INFO | Reading frame:  44
2026-05-08 14:00:54 | INFO | Reading frame:  45
2026-05-08 14:00:54 | INFO | Reading frame:  46
2026-05-08 14:00:54 | INFO | Reading frame:  47
2026-05-08 14:00:54 | INFO | Reading frame:  48
2026-05-08 14:00:54 | INFO | Reading frame:  49
2026-05-08 14:00:54 | INFO | Reading frame:  50
2026-05-08 14:00:54 | INFO | Reading frame:  51
2026-05-08 14:00:54 | INFO | Reading frame:  52
2026-05-08 14:00:54 | INFO | Reading frame:  53
2026-05-08 14:00:54 | INFO | Reading frame:  54
2026-05-08 14:00:54 | INFO | Reading frame:  55
2026-05-08 14:00:54 | INFO | Reading frame:  56
2026-05-08 14:00:54 | INFO | Reading frame:  57
2026-05-08 14:00:54 | INFO | Reading frame:  58
2026-05-08 14:00:54 | INFO | Reading frame:  59
2026-05-08 14:00:54 | INFO | Reading frame:  60
2026-05-08 14:00:54 | INFO | Reading frame:  61
2026-05-08 14:00:54 | INFO | Reading frame:  62
2026-05-08 14:00:54 | INFO | Reading frame:  63
2026-05-08 14:00:54 | INFO | Reading frame:  64
2026-05-08 14:00:54 | INFO | Reading frame:  65
2026-05-08 14:00:54 | INFO | Reading frame:  66
2026-05-08 14:00:54 | INFO | Reading frame:  67
2026-05-08 14:00:54 | INFO | Reading frame:  68
2026-05-08 14:00:54 | INFO | Reading frame:  69
2026-05-08 14:00:54 | INFO | Reading frame:  70
2026-05-08 14:00:54 | INFO | Reading frame:  71
2026-05-08 14:00:54 | INFO | Reading frame:  72
2026-05-08 14:00:54 | INFO | Reading frame:  73
2026-05-08 14:00:54 | INFO | Reading frame:  74
2026-05-08 14:00:54 | INFO | Reading frame:  75
2026-05-08 14:00:54 | INFO | Reading frame:  76
2026-05-08 14:00:54 | INFO | Reading frame:  77
2026-05-08 14:00:54 | INFO | Reading frame:  78
2026-05-08 14:00:54 | INFO | Reading frame:  79
2026-05-08 14:00:54 | INFO | Reading frame:  80
2026-05-08 14:00:54 | INFO | Reading frame:  81
2026-05-08 14:00:54 | INFO | Reading frame:  82
2026-05-08 14:00:54 | INFO | Reading frame:  83
2026-05-08 14:00:54 | INFO | Reading frame:  84
2026-05-08 14:00:54 | INFO | Reading frame:  85
2026-05-08 14:00:54 | INFO | Reading frame:  86
2026-05-08 14:00:54 | INFO | Reading frame:  87
2026-05-08 14:00:54 | INFO | Reading frame:  88
2026-05-08 14:00:54 | INFO | Reading frame:  89
2026-05-08 14:00:54 | INFO | Reading frame:  90
2026-05-08 14:00:54 | INFO | Reading frame:  91
2026-05-08 14:00:54 | INFO | Reading frame:  92
2026-05-08 14:00:54 | INFO | Reading frame:  93
2026-05-08 14:00:54 | INFO | Reading frame:  94
2026-05-08 14:00:54 | INFO | Reading frame:  95
2026-05-08 14:00:54 | INFO | Reading frame:  96
2026-05-08 14:00:54 | INFO | Reading frame:  97
2026-05-08 14:00:54 | INFO | Reading frame:  98
2026-05-08 14:00:54 | INFO | Reading frame:  99
2026-05-08 14:00:54 | INFO | Reading frame:  100
2026-05-08 14:00:54 | INFO | Reading frame:  101
2026-05-08 14:00:54 | INFO | Reading frame:  102
2026-05-08 14:00:54 | INFO | Reading frame:  103
2026-05-08 14:00:54 | INFO | Reading frame:  104
2026-05-08 14:00:54 | INFO | Reading frame:  105
2026-05-08 14:00:54 | INFO | Reading frame:  106
2026-05-08 14:00:54 | INFO | Reading frame:  107
2026-05-08 14:00:54 | INFO | Reading frame:  108
2026-05-08 14:00:54 | INFO | Reading frame:  109
2026-05-08 14:00:54 | INFO | Reading frame:  110
2026-05-08 14:00:54 | INFO | Reading frame:  111
2026-05-08 14:00:54 | INFO | Reading frame:  112
2026-05-08 14:00:54 | INFO | Reading frame:  113
2026-05-08 14:00:54 | INFO | Reading frame:  114
2026-05-08 14:00:54 | INFO | Reading frame:  115
2026-05-08 14:00:54 | INFO | Reading frame:  116
2026-05-08 14:00:54 | INFO | Reading frame:  117
2026-05-08 14:00:54 | INFO | Reading frame:  118
2026-05-08 14:00:54 | INFO | Reading frame:  119
2026-05-08 14:00:54 | INFO | Reading frame:  120
2026-05-08 14:00:54 | INFO | Reading frame:  121
2026-05-08 14:00:54 | INFO | Reading frame:  122
2026-05-08 14:00:54 | INFO | Reading frame:  123
2026-05-08 14:00:54 | INFO | Reading frame:  124
2026-05-08 14:00:54 | INFO | Reading frame:  125
2026-05-08 14:00:54 | INFO | Reading frame:  126
2026-05-08 14:00:54 | INFO | Reading frame:  127
2026-05-08 14:00:54 | INFO | Reading frame:  128
2026-05-08 14:00:54 | INFO | Reading frame:  129
2026-05-08 14:00:54 | INFO | Reading frame:  130
2026-05-08 14:00:54 | INFO | Reading frame:  131
2026-05-08 14:00:54 | INFO | Reading frame:  132
2026-05-08 14:00:54 | INFO | Reading frame:  133
2026-05-08 14:00:54 | INFO | Reading frame:  134
2026-05-08 14:00:54 | INFO | Reading frame:  135
2026-05-08 14:00:54 | INFO | Reading frame:  136
2026-05-08 14:00:54 | INFO | Reading frame:  137
2026-05-08 14:00:54 | INFO | Reading frame:  138
2026-05-08 14:00:54 | INFO | Reading frame:  139
2026-05-08 14:00:54 | INFO | Reading frame:  140
2026-05-08 14:00:54 | INFO | Reading frame:  141
2026-05-08 14:00:54 | INFO | Reading frame:  142
2026-05-08 14:00:54 | INFO | Reading frame:  143
2026-05-08 14:00:54 | INFO | Reading frame:  144
2026-05-08 14:00:54 | INFO | Reading frame:  145
2026-05-08 14:00:54 | INFO | Reading frame:  146
2026-05-08 14:00:54 | INFO | Reading frame:  147
2026-05-08 14:00:54 | INFO | Reading frame:  148
2026-05-08 14:00:54 | INFO | Reading frame:  149
2026-05-08 14:00:54 | INFO | Reading frame:  150
2026-05-08 14:00:54 | INFO | Reading frame:  151
2026-05-08 14:00:54 | INFO | Reading frame:  152
2026-05-08 14:00:54 | INFO | Reading frame:  153
2026-05-08 14:00:54 | INFO | Reading frame:  154
2026-05-08 14:00:54 | INFO | Reading frame:  155
2026-05-08 14:00:54 | INFO | Reading frame:  156
2026-05-08 14:00:54 | INFO | Reading frame:  157
2026-05-08 14:00:54 | INFO | Reading frame:  158
2026-05-08 14:00:54 | INFO | Reading frame:  159
2026-05-08 14:00:54 | INFO | Reading frame:  160
2026-05-08 14:00:54 | INFO | Reading frame:  161
2026-05-08 14:00:54 | INFO | Reading frame:  162
2026-05-08 14:00:54 | INFO | Reading frame:  163
2026-05-08 14:00:54 | INFO | Reading frame:  164
2026-05-08 14:00:54 | INFO | Reading frame:  165
2026-05-08 14:00:54 | INFO | Reading frame:  166
2026-05-08 14:00:54 | INFO | Reading frame:  167
2026-05-08 14:00:54 | INFO | Reading frame:  168
2026-05-08 14:00:54 | INFO | Reading frame:  169
2026-05-08 14:00:54 | INFO | Reading frame:  170
2026-05-08 14:00:54 | INFO | Reading frame:  171
2026-05-08 14:00:54 | INFO | Reading frame:  172
2026-05-08 14:00:54 | INFO | Reading frame:  173
2026-05-08 14:00:54 | INFO | Reading frame:  174
2026-05-08 14:00:54 | INFO | Reading frame:  175
2026-05-08 14:00:54 | INFO | Reading frame:  176
2026-05-08 14:00:54 | INFO | Reading frame:  177
2026-05-08 14:00:54 | INFO | Reading frame:  178
2026-05-08 14:00:54 | INFO | Reading frame:  179
2026-05-08 14:00:54 | INFO | Reading frame:  180
2026-05-08 14:00:54 | INFO | Reading frame:  181
2026-05-08 14:00:54 | INFO | Reading frame:  182
2026-05-08 14:00:54 | INFO | Reading frame:  183
2026-05-08 14:00:54 | INFO | Reading frame:  184
2026-05-08 14:00:54 | INFO | Reading frame:  185
2026-05-08 14:00:54 | INFO | Reading frame:  186
2026-05-08 14:00:54 | INFO | Reading frame:  187
2026-05-08 14:00:54 | INFO | Reading frame:  188
2026-05-08 14:00:54 | INFO | Reading frame:  189
2026-05-08 14:00:54 | INFO | Reading frame:  190
2026-05-08 14:00:54 | INFO | Reading frame:  191
2026-05-08 14:00:54 | INFO | Reading frame:  192
2026-05-08 14:00:54 | INFO | Reading frame:  193
2026-05-08 14:00:54 | INFO | Reading frame:  194
2026-05-08 14:00:54 | INFO | Reading frame:  195
2026-05-08 14:00:54 | INFO | Reading frame:  196
2026-05-08 14:00:54 | INFO | Reading frame:  197
2026-05-08 14:00:54 | INFO | Reading frame:  198
2026-05-08 14:00:54 | INFO | Reading frame:  199
2026-05-08 14:00:54 | INFO | Reading frame:  200
2026-05-08 14:00:54 | INFO | Reading frame:  201
2026-05-08 14:00:54 | INFO | Reading frame:  202
2026-05-08 14:00:54 | INFO | Reading frame:  203
2026-05-08 14:00:54 | INFO | Reading frame:  204
2026-05-08 14:00:54 | INFO | Reading frame:  205
2026-05-08 14:00:54 | INFO | Reading frame:  206
2026-05-08 14:00:54 | INFO | Reading frame:  207
2026-05-08 14:00:54 | INFO | Reading frame:  208
2026-05-08 14:00:54 | INFO | Reading frame:  209
2026-05-08 14:00:54 | INFO | Reading frame:  210
2026-05-08 14:00:54 | INFO | Reading frame:  211
2026-05-08 14:00:54 | INFO | Reading frame:  212
2026-05-08 14:00:54 | INFO | Reading frame:  213
2026-05-08 14:00:54 | INFO | Reading frame:  214
2026-05-08 14:00:54 | INFO | Reading frame:  215
2026-05-08 14:00:54 | INFO | Reading frame:  216
2026-05-08 14:00:54 | INFO | Reading frame:  217
2026-05-08 14:00:54 | INFO | Reading frame:  218
2026-05-08 14:00:54 | INFO | Reading frame:  219
2026-05-08 14:00:54 | INFO | Reading frame:  220
2026-05-08 14:00:54 | INFO | Reading frame:  221
2026-05-08 14:00:54 | INFO | Reading frame:  222
2026-05-08 14:00:54 | INFO | Reading frame:  223
2026-05-08 14:00:54 | INFO | Reading frame:  224
2026-05-08 14:00:54 | INFO | Reading frame:  225
2026-05-08 14:00:54 | INFO | Reading frame:  226
2026-05-08 14:00:54 | INFO | Reading frame:  227
2026-05-08 14:00:54 | INFO | Reading frame:  228
2026-05-08 14:00:54 | INFO | Reading frame:  229
2026-05-08 14:00:54 | INFO | Reading frame:  230
2026-05-08 14:00:54 | INFO | Reading frame:  231
2026-05-08 14:00:54 | INFO | Reading frame:  232
2026-05-08 14:00:54 | INFO | Reading frame:  233
2026-05-08 14:00:54 | INFO | Reading frame:  234
2026-05-08 14:00:54 | INFO | Reading frame:  235
2026-05-08 14:00:54 | INFO | Reading frame:  236
2026-05-08 14:00:54 | INFO | Reading frame:  237
2026-05-08 14:00:54 | INFO | Reading frame:  238
2026-05-08 14:00:54 | INFO | Reading frame:  239
2026-05-08 14:00:54 | INFO | Reading frame:  240
2026-05-08 14:00:54 | INFO | Reading frame:  241
2026-05-08 14:00:54 | INFO | Reading frame:  242
2026-05-08 14:00:54 | INFO | Reading frame:  243
2026-05-08 14:00:54 | INFO | Reading frame:  244
2026-05-08 14:00:54 | INFO | Reading frame:  245
2026-05-08 14:00:54 | INFO | Reading frame:  246
2026-05-08 14:00:54 | INFO | Reading frame:  247
2026-05-08 14:00:54 | INFO | Reading frame:  248
2026-05-08 14:00:54 | INFO | Reading frame:  249
2026-05-08 14:00:54 | INFO | Reading frame:  250
2026-05-08 14:00:54 | INFO | Reading frame:  251
2026-05-08 14:00:54 | INFO | Reading frame:  252
2026-05-08 14:00:54 | INFO | Reading frame:  253
2026-05-08 14:00:54 | INFO | Reading frame:  254
2026-05-08 14:00:54 | INFO | Reading frame:  255
2026-05-08 14:00:54 | INFO | Reading frame:  256
2026-05-08 14:00:54 | INFO | Reading frame:  257
2026-05-08 14:00:54 | INFO | Reading frame:  258
2026-05-08 14:00:54 | INFO | Reading frame:  259
2026-05-08 14:00:54 | INFO | Reading frame:  260
2026-05-08 14:00:54 | INFO | Reading frame:  261
2026-05-08 14:00:54 | INFO | Reading frame:  262
2026-05-08 14:00:54 | INFO | Reading frame:  263
2026-05-08 14:00:54 | INFO | Reading frame:  264
2026-05-08 14:00:54 | INFO | Reading frame:  265
2026-05-08 14:00:54 | INFO | Reading frame:  266
2026-05-08 14:00:54 | INFO | Reading frame:  267
2026-05-08 14:00:54 | INFO | Reading frame:  268
2026-05-08 14:00:54 | INFO | Reading frame:  269
2026-05-08 14:00:54 | INFO | Reading frame:  270
2026-05-08 14:00:54 | INFO | Reading frame:  271
2026-05-08 14:00:54 | INFO | Reading frame:  272
2026-05-08 14:00:54 | INFO | Reading frame:  273
2026-05-08 14:00:54 | INFO | Reading frame:  274
2026-05-08 14:00:54 | INFO | Reading frame:  275
2026-05-08 14:00:54 | INFO | Reading frame:  276
2026-05-08 14:00:54 | INFO | Reading frame:  277
2026-05-08 14:00:54 | INFO | Reading frame:  278
2026-05-08 14:00:54 | INFO | Reading frame:  279
2026-05-08 14:00:54 | INFO | Reading frame:  280
2026-05-08 14:00:54 | INFO | Reading frame:  281
2026-05-08 14:00:54 | INFO | Reading frame:  282
2026-05-08 14:00:54 | INFO | Reading frame:  283
2026-05-08 14:00:54 | INFO | Reading frame:  284
2026-05-08 14:00:54 | INFO | Reading frame:  285
2026-05-08 14:00:54 | INFO | Reading frame:  286
2026-05-08 14:00:54 | INFO | Reading frame:  287
2026-05-08 14:00:54 | INFO | Reading frame:  288
2026-05-08 14:00:54 | INFO | Reading frame:  289
2026-05-08 14:00:54 | INFO | Reading frame:  290
2026-05-08 14:00:54 | INFO | Reading frame:  291
2026-05-08 14:00:54 | INFO | Reading frame:  292
2026-05-08 14:00:54 | INFO | Reading frame:  293
2026-05-08 14:00:54 | INFO | Reading frame:  294
2026-05-08 14:00:54 | INFO | Reading frame:  295
2026-05-08 14:00:54 | INFO | Reading frame:  296
2026-05-08 14:00:54 | INFO | Reading frame:  297
2026-05-08 14:00:54 | INFO | Reading frame:  298
2026-05-08 14:00:54 | INFO | Reading frame:  299
2026-05-08 14:00:54 | INFO | Reading frame:  300
2026-05-08 14:00:54 | INFO | Reading frame:  301
2026-05-08 14:00:54 | INFO | Reading frame:  302
2026-05-08 14:00:54 | INFO | Reading frame:  303
2026-05-08 14:00:54 | INFO | Reading frame:  304
2026-05-08 14:00:54 | INFO | Reading frame:  305
2026-05-08 14:00:54 | INFO | Reading frame:  306
2026-05-08 14:00:54 | INFO | Reading frame:  307
2026-05-08 14:00:54 | INFO | Reading frame:  308
2026-05-08 14:00:54 | INFO | Reading frame:  309
2026-05-08 14:00:54 | INFO | Reading frame:  310
2026-05-08 14:00:54 | INFO | Reading frame:  311
2026-05-08 14:00:54 | INFO | Reading frame:  312
2026-05-08 14:00:54 | INFO | Reading frame:  313
2026-05-08 14:00:54 | INFO | Reading frame:  314
2026-05-08 14:00:54 | INFO | Reading frame:  315
2026-05-08 14:00:54 | INFO | Reading frame:  316
2026-05-08 14:00:54 | INFO | Reading frame:  317
2026-05-08 14:00:54 | INFO | Reading frame:  318
2026-05-08 14:00:54 | INFO | Reading frame:  319
2026-05-08 14:00:54 | INFO | Reading frame:  320
2026-05-08 14:00:54 | INFO | Reading frame:  321
2026-05-08 14:00:54 | INFO | Reading frame:  322
2026-05-08 14:00:54 | INFO | Reading frame:  323
2026-05-08 14:00:54 | INFO | Reading frame:  324
2026-05-08 14:00:54 | INFO | Reading frame:  325
2026-05-08 14:00:54 | INFO | Reading frame:  326
2026-05-08 14:00:54 | INFO | Reading frame:  327
2026-05-08 14:00:54 | INFO | Reading frame:  328
2026-05-08 14:00:54 | INFO | Reading frame:  329
2026-05-08 14:00:54 | INFO | Reading frame:  330
2026-05-08 14:00:54 | INFO | Reading frame:  331
2026-05-08 14:00:54 | INFO | Reading frame:  332
2026-05-08 14:00:54 | INFO | Reading frame:  333
2026-05-08 14:00:54 | INFO | Reading frame:  334
2026-05-08 14:00:54 | INFO | Reading frame:  335
2026-05-08 14:00:54 | INFO | Reading frame:  336
2026-05-08 14:00:54 | INFO | Reading frame:  337
2026-05-08 14:00:54 | INFO | Reading frame:  338
2026-05-08 14:00:54 | INFO | Reading frame:  339
2026-05-08 14:00:54 | INFO | Reading frame:  340
2026-05-08 14:00:54 | INFO | Reading frame:  341
2026-05-08 14:00:54 | INFO | Reading frame:  342
2026-05-08 14:00:54 | INFO | Reading frame:  343
2026-05-08 14:00:54 | INFO | Reading frame:  344
2026-05-08 14:00:54 | INFO | Reading frame:  345
2026-05-08 14:00:54 | INFO | Reading frame:  346
2026-05-08 14:00:54 | INFO | Reading frame:  347
2026-05-08 14:00:54 | INFO | Reading frame:  348
2026-05-08 14:00:54 | INFO | Reading frame:  349
2026-05-08 14:00:54 | INFO | Reading frame:  350
2026-05-08 14:00:54 | INFO | Reading frame:  351
2026-05-08 14:00:54 | INFO | Reading frame:  352
2026-05-08 14:00:54 | INFO | Reading frame:  353
2026-05-08 14:00:54 | INFO | Reading frame:  354
2026-05-08 14:00:54 | INFO | Reading frame:  355
2026-05-08 14:00:54 | INFO | Reading frame:  356
2026-05-08 14:00:54 | INFO | Reading frame:  357
2026-05-08 14:00:54 | INFO | Reading frame:  358
2026-05-08 14:00:54 | INFO | Reading frame:  359
2026-05-08 14:00:54 | INFO | Reading frame:  360
2026-05-08 14:00:54 | INFO | Reading frame:  361
2026-05-08 14:00:54 | INFO | Reading frame:  362
2026-05-08 14:00:54 | INFO | Reading frame:  363
2026-05-08 14:00:54 | INFO | Reading frame:  364
2026-05-08 14:00:54 | INFO | Reading frame:  365
2026-05-08 14:00:54 | INFO | Reading frame:  366
2026-05-08 14:00:54 | INFO | Reading frame:  367
2026-05-08 14:00:54 | INFO | Reading frame:  368
2026-05-08 14:00:54 | INFO | Reading frame:  369
2026-05-08 14:00:54 | INFO | Reading frame:  370
2026-05-08 14:00:54 | INFO | Reading frame:  371
2026-05-08 14:00:54 | INFO | Reading frame:  372
2026-05-08 14:00:54 | INFO | Reading frame:  373
2026-05-08 14:00:54 | INFO | Reading frame:  374
2026-05-08 14:00:54 | INFO | Reading frame:  375
2026-05-08 14:00:54 | INFO | Reading frame:  376
2026-05-08 14:00:54 | INFO | Reading frame:  377
2026-05-08 14:00:54 | INFO | Reading frame:  378
2026-05-08 14:00:54 | INFO | Reading frame:  379
2026-05-08 14:00:54 | INFO | Reading frame:  380
2026-05-08 14:00:54 | INFO | Reading frame:  381
2026-05-08 14:00:54 | INFO | Reading frame:  382
2026-05-08 14:00:54 | INFO | Reading frame:  383
2026-05-08 14:00:54 | INFO | Reading frame:  384
2026-05-08 14:00:54 | INFO | Reading frame:  385
2026-05-08 14:00:54 | INFO | Reading frame:  386
2026-05-08 14:00:54 | INFO | Reading frame:  387
2026-05-08 14:00:54 | INFO | Reading frame:  388
2026-05-08 14:00:57 | INFO | Reading frame:  389
2026-05-08 14:00:57 | INFO | Reading frame:  390
2026-05-08 14:00:57 | INFO | Reading frame:  391
2026-05-08 14:00:57 | INFO | Reading frame:  392
2026-05-08 14:00:57 | INFO | Reading frame:  393
2026-05-08 14:00:57 | INFO | Reading frame:  394
2026-05-08 14:00:57 | INFO | Reading frame:  395
2026-05-08 14:00:57 | INFO | Reading frame:  396
2026-05-08 14:00:57 | INFO | Reading frame:  397
2026-05-08 14:00:57 | INFO | Reading frame:  398
2026-05-08 14:00:57 | INFO | Reading frame:  399
2026-05-08 14:00:57 | INFO | Reading frame:  400
2026-05-08 14:00:57 | INFO | Reading frame:  401
2026-05-08 14:00:57 | INFO | Reading frame:  402
2026-05-08 14:00:57 | INFO | Reading frame:  403
2026-05-08 14:00:57 | INFO | Reading frame:  404
2026-05-08 14:00:57 | INFO | Reading frame:  405
2026-05-08 14:00:57 | INFO | Reading frame:  406
2026-05-08 14:00:57 | INFO | Reading frame:  407
2026-05-08 14:00:57 | INFO | Reading frame:  408
2026-05-08 14:00:57 | INFO | Reading frame:  409
2026-05-08 14:00:57 | INFO | Reading frame:  410
2026-05-08 14:00:57 | INFO | Reading frame:  411
2026-05-08 14:00:57 | INFO | Reading frame:  412
2026-05-08 14:00:57 | INFO | Reading frame:  413
2026-05-08 14:00:57 | INFO | Reading frame:  414
2026-05-08 14:00:57 | INFO | Reading frame:  415
2026-05-08 14:00:57 | INFO | Reading frame:  416
2026-05-08 14:00:57 | INFO | Reading frame:  417
2026-05-08 14:00:57 | INFO | Reading frame:  418
2026-05-08 14:00:57 | INFO | Reading frame:  419
2026-05-08 14:00:57 | INFO | Reading frame:  420
2026-05-08 14:00:57 | INFO | Reading frame:  421
2026-05-08 14:00:57 | INFO | Reading frame:  422
2026-05-08 14:00:57 | INFO | Reading frame:  423
2026-05-08 14:00:57 | INFO | Reading frame:  424
2026-05-08 14:00:57 | INFO | Reading frame:  425
2026-05-08 14:00:57 | INFO | Reading frame:  426
2026-05-08 14:00:57 | INFO | Reading frame:  427
2026-05-08 14:00:57 | INFO | Reading frame:  428
2026-05-08 14:00:57 | INFO | Reading frame:  429
2026-05-08 14:00:57 | INFO | Reading frame:  430
2026-05-08 14:00:57 | INFO | Reading frame:  431
2026-05-08 14:00:57 | INFO | Reading frame:  432
2026-05-08 14:00:57 | INFO | Reading frame:  433
2026-05-08 14:00:57 | INFO | Reading frame:  434
2026-05-08 14:00:57 | INFO | Reading frame:  435
2026-05-08 14:00:57 | INFO | Reading frame:  436
2026-05-08 14:00:57 | INFO | Reading frame:  437
2026-05-08 14:00:57 | INFO | Reading frame:  438
2026-05-08 14:00:57 | INFO | Reading frame:  439
2026-05-08 14:00:57 | INFO | Reading frame:  440
2026-05-08 14:00:57 | INFO | Reading frame:  441
2026-05-08 14:00:57 | INFO | Reading frame:  442
2026-05-08 14:00:57 | INFO | Reading frame:  443
2026-05-08 14:00:57 | INFO | Reading frame:  444
2026-05-08 14:00:57 | INFO | Reading frame:  445
2026-05-08 14:00:57 | INFO | Reading frame:  446
2026-05-08 14:00:57 | INFO | Reading frame:  447
2026-05-08 14:00:57 | INFO | Reading frame:  448
2026-05-08 14:00:57 | INFO | Reading frame:  449
2026-05-08 14:00:57 | INFO | Reading frame:  450
2026-05-08 14:00:57 | INFO | Reading frame:  451
2026-05-08 14:00:57 | INFO | Reading frame:  452
2026-05-08 14:00:57 | INFO | Reading frame:  453
2026-05-08 14:00:57 | INFO | Reading frame:  454
2026-05-08 14:00:57 | INFO | Reading frame:  455
2026-05-08 14:00:57 | INFO | Reading frame:  456
2026-05-08 14:00:57 | INFO | Reading frame:  457
2026-05-08 14:00:57 | INFO | Reading frame:  458
2026-05-08 14:00:57 | INFO | Reading frame:  459
2026-05-08 14:00:57 | INFO | Reading frame:  460
2026-05-08 14:00:57 | INFO | Reading frame:  461
2026-05-08 14:00:57 | INFO | Reading frame:  462
2026-05-08 14:00:57 | INFO | Reading frame:  463
2026-05-08 14:00:57 | INFO | Reading frame:  464
2026-05-08 14:00:57 | INFO | Reading frame:  465
2026-05-08 14:00:57 | INFO | Reading frame:  466
2026-05-08 14:00:57 | INFO | Reading frame:  467
2026-05-08 14:00:57 | INFO | Reading frame:  468
2026-05-08 14:00:57 | INFO | Reading frame:  469
2026-05-08 14:00:57 | INFO | Reading frame:  470
2026-05-08 14:00:57 | INFO | Reading frame:  471
2026-05-08 14:00:57 | INFO | Reading frame:  472
2026-05-08 14:00:57 | INFO | Reading frame:  473
2026-05-08 14:00:57 | INFO | Reading frame:  474
2026-05-08 14:00:57 | INFO | Reading frame:  475
2026-05-08 14:00:57 | INFO | Reading frame:  476
2026-05-08 14:00:57 | INFO | Reading frame:  477
2026-05-08 14:00:57 | INFO | Reading frame:  478
2026-05-08 14:00:57 | INFO | Reading frame:  479
2026-05-08 14:00:57 | INFO | Reading frame:  480
2026-05-08 14:00:57 | INFO | Reading frame:  481
2026-05-08 14:00:57 | INFO | Reading frame:  482
2026-05-08 14:00:57 | INFO | Reading frame:  483
2026-05-08 14:00:57 | INFO | Reading frame:  484
2026-05-08 14:00:57 | INFO | Reading frame:  485
2026-05-08 14:00:57 | INFO | Reading frame:  486
2026-05-08 14:00:57 | INFO | Reading frame:  487
2026-05-08 14:00:57 | INFO | Reading frame:  488
2026-05-08 14:00:57 | INFO | Reading frame:  489
2026-05-08 14:00:57 | INFO | Reading frame:  490
2026-05-08 14:00:57 | INFO | Reading frame:  491
2026-05-08 14:00:57 | INFO | Reading frame:  492
2026-05-08 14:00:57 | INFO | Reading frame:  493
2026-05-08 14:00:57 | INFO | Reading frame:  494
2026-05-08 14:00:57 | INFO | Reading frame:  495
2026-05-08 14:00:57 | INFO | Reading frame:  496
2026-05-08 14:00:57 | INFO | Reading frame:  497
2026-05-08 14:00:57 | INFO | Reading frame:  498
2026-05-08 14:00:57 | INFO | Reading frame:  499
2026-05-08 14:00:57 | INFO | Reading frame:  500
2026-05-08 14:00:57 | INFO | Reading frame:  501
2026-05-08 14:00:57 | INFO | Reading frame:  502
2026-05-08 14:00:57 | INFO | Reading frame:  503
2026-05-08 14:00:57 | INFO | Reading frame:  504
2026-05-08 14:00:57 | INFO | Reading frame:  505
2026-05-08 14:00:57 | INFO | Reading frame:  506
2026-05-08 14:00:57 | INFO | Reading frame:  507
2026-05-08 14:00:57 | INFO | Reading frame:  508
2026-05-08 14:00:57 | INFO | Reading frame:  509
2026-05-08 14:00:57 | INFO | Reading frame:  510
2026-05-08 14:00:57 | INFO | Reading frame:  511
2026-05-08 14:00:57 | INFO | Reading frame:  512
2026-05-08 14:00:57 | INFO | Reading frame:  513
2026-05-08 14:00:57 | INFO | Reading frame:  514
2026-05-08 14:00:57 | INFO | Reading frame:  515
2026-05-08 14:00:57 | INFO | Reading frame:  516
2026-05-08 14:00:57 | INFO | Reading frame:  517
2026-05-08 14:00:57 | INFO | Reading frame:  518
2026-05-08 14:00:57 | INFO | Reading frame:  519
2026-05-08 14:00:57 | INFO | Reading frame:  520
2026-05-08 14:00:57 | INFO | Reading frame:  521
2026-05-08 14:00:57 | INFO | Reading frame:  522
2026-05-08 14:00:57 | INFO | Reading frame:  523
2026-05-08 14:00:57 | INFO | Reading frame:  524
2026-05-08 14:00:57 | INFO | Reading frame:  525
2026-05-08 14:00:57 | INFO | Reading frame:  526
2026-05-08 14:00:57 | INFO | Reading frame:  527
2026-05-08 14:00:57 | INFO | Reading frame:  528
2026-05-08 14:00:57 | INFO | Reading frame:  529
2026-05-08 14:00:57 | INFO | Reading frame:  530
2026-05-08 14:00:57 | INFO | Reading frame:  531
2026-05-08 14:00:57 | INFO | Reading frame:  532
2026-05-08 14:00:57 | INFO | Reading frame:  533
2026-05-08 14:00:57 | INFO | Reading frame:  534
2026-05-08 14:00:57 | INFO | Reading frame:  535
2026-05-08 14:00:57 | INFO | Reading frame:  536
2026-05-08 14:00:57 | INFO | Reading frame:  537
2026-05-08 14:00:57 | INFO | Reading frame:  538
2026-05-08 14:00:57 | INFO | Reading frame:  539
2026-05-08 14:00:57 | INFO | Reading frame:  540
2026-05-08 14:00:57 | INFO | Reading frame:  541
2026-05-08 14:00:57 | INFO | Reading frame:  542
2026-05-08 14:00:57 | INFO | Reading frame:  543
2026-05-08 14:00:57 | INFO | Reading frame:  544
2026-05-08 14:00:57 | INFO | Reading frame:  545
2026-05-08 14:00:57 | INFO | Reading frame:  546
2026-05-08 14:00:57 | INFO | Reading frame:  547
2026-05-08 14:00:57 | INFO | Reading frame:  548
2026-05-08 14:00:57 | INFO | Reading frame:  549
2026-05-08 14:00:57 | INFO | Reading frame:  550
2026-05-08 14:00:57 | INFO | Reading frame:  551
2026-05-08 14:00:57 | INFO | Reading frame:  552
2026-05-08 14:00:57 | INFO | Reading frame:  553
2026-05-08 14:00:57 | INFO | Reading frame:  554
2026-05-08 14:00:57 | INFO | Reading frame:  555
2026-05-08 14:00:57 | INFO | Reading frame:  556
2026-05-08 14:00:57 | INFO | Reading frame:  557
2026-05-08 14:00:57 | INFO | Reading frame:  558
2026-05-08 14:00:57 | INFO | Reading frame:  559
2026-05-08 14:00:57 | INFO | Reading frame:  560
2026-05-08 14:00:57 | INFO | Reading frame:  561
2026-05-08 14:00:57 | INFO | Reading frame:  562
2026-05-08 14:00:57 | INFO | Reading frame:  563
2026-05-08 14:00:57 | INFO | Reading frame:  564
2026-05-08 14:00:57 | INFO | Reading frame:  565
2026-05-08 14:00:57 | INFO | Reading frame:  566
2026-05-08 14:00:57 | INFO | Reading frame:  567
2026-05-08 14:00:57 | INFO | Reading frame:  568
2026-05-08 14:00:57 | INFO | Reading frame:  569
2026-05-08 14:00:57 | INFO | Reading frame:  570
2026-05-08 14:00:57 | INFO | Reading frame:  571
2026-05-08 14:00:57 | INFO | Reading frame:  572
2026-05-08 14:00:57 | INFO | Reading frame:  573
2026-05-08 14:00:57 | INFO | Reading frame:  574
2026-05-08 14:00:57 | INFO | Reading frame:  575
2026-05-08 14:00:57 | INFO | Reading frame:  576
2026-05-08 14:00:57 | INFO | Reading frame:  577
2026-05-08 14:00:57 | INFO | Reading frame:  578
2026-05-08 14:00:57 | INFO | Reading frame:  579
2026-05-08 14:00:57 | INFO | Reading frame:  580
2026-05-08 14:00:57 | INFO | Reading frame:  581
2026-05-08 14:00:57 | INFO | Reading frame:  582
2026-05-08 14:00:57 | INFO | Reading frame:  583
2026-05-08 14:00:57 | INFO | Reading frame:  584
2026-05-08 14:00:57 | INFO | Reading frame:  585
2026-05-08 14:00:57 | INFO | Reading frame:  586
2026-05-08 14:00:57 | INFO | Reading frame:  587
2026-05-08 14:00:57 | INFO | Reading frame:  588
2026-05-08 14:00:57 | INFO | Reading frame:  589
2026-05-08 14:00:57 | INFO | Reading frame:  590
2026-05-08 14:00:57 | INFO | Reading frame:  591
2026-05-08 14:00:57 | INFO | Reading frame:  592
2026-05-08 14:00:57 | INFO | Reading frame:  593
2026-05-08 14:00:57 | INFO | Reading frame:  594
2026-05-08 14:00:57 | INFO | Reading frame:  595
2026-05-08 14:00:57 | INFO | Reading frame:  596
2026-05-08 14:00:57 | INFO | Reading frame:  597
2026-05-08 14:00:57 | INFO | Reading frame:  598
2026-05-08 14:00:57 | INFO | Reading frame:  599
2026-05-08 14:00:57 | INFO | Reading frame:  600
2026-05-08 14:00:57 | INFO | Reading frame:  601
2026-05-08 14:00:57 | INFO | Reading frame:  602
2026-05-08 14:00:57 | INFO | Reading frame:  603
2026-05-08 14:00:57 | INFO | Reading frame:  604
2026-05-08 14:00:57 | INFO | Reading frame:  605
2026-05-08 14:00:57 | INFO | Reading frame:  606
2026-05-08 14:00:57 | INFO | Reading frame:  607
2026-05-08 14:00:57 | INFO | Reading frame:  608
2026-05-08 14:00:57 | INFO | Reading frame:  609
2026-05-08 14:00:57 | INFO | Reading frame:  610
2026-05-08 14:00:57 | INFO | Reading frame:  611
2026-05-08 14:00:57 | INFO | Reading frame:  612
2026-05-08 14:00:57 | INFO | Reading frame:  613
2026-05-08 14:00:57 | INFO | Reading frame:  614
2026-05-08 14:00:57 | INFO | Reading frame:  615
2026-05-08 14:00:57 | INFO | Reading frame:  616
2026-05-08 14:00:57 | INFO | Reading frame:  617
2026-05-08 14:00:57 | INFO | Reading frame:  618
2026-05-08 14:00:57 | INFO | Reading frame:  619
2026-05-08 14:00:57 | INFO | Reading frame:  620
2026-05-08 14:00:57 | INFO | Reading frame:  621
2026-05-08 14:00:57 | INFO | Reading frame:  622
2026-05-08 14:00:57 | INFO | Reading frame:  623
2026-05-08 14:00:57 | INFO | Reading frame:  624
2026-05-08 14:00:57 | INFO | Reading frame:  625
2026-05-08 14:00:57 | INFO | Reading frame:  626
2026-05-08 14:00:57 | INFO | Reading frame:  627
2026-05-08 14:00:57 | INFO | Reading frame:  628
2026-05-08 14:00:57 | INFO | Reading frame:  629
2026-05-08 14:00:57 | INFO | Reading frame:  630
2026-05-08 14:00:57 | INFO | Reading frame:  631
2026-05-08 14:00:57 | INFO | Reading frame:  632
2026-05-08 14:00:57 | INFO | Reading frame:  633
2026-05-08 14:00:57 | INFO | Reading frame:  634
2026-05-08 14:00:57 | INFO | Reading frame:  635
2026-05-08 14:00:57 | INFO | Reading frame:  636
2026-05-08 14:00:57 | INFO | Reading frame:  637
2026-05-08 14:00:57 | INFO | Reading frame:  638
2026-05-08 14:00:57 | INFO | Reading frame:  639
2026-05-08 14:00:57 | INFO | Reading frame:  640
2026-05-08 14:00:57 | INFO | Reading frame:  641
2026-05-08 14:00:57 | INFO | Reading frame:  642
2026-05-08 14:00:57 | INFO | Reading frame:  643
2026-05-08 14:00:57 | INFO | Reading frame:  644
2026-05-08 14:00:57 | INFO | Reading frame:  645
2026-05-08 14:00:57 | INFO | Reading frame:  646
2026-05-08 14:00:57 | INFO | Reading frame:  647
2026-05-08 14:00:57 | INFO | Reading frame:  648
2026-05-08 14:00:57 | INFO | Reading frame:  649
2026-05-08 14:00:57 | INFO | Reading frame:  650
2026-05-08 14:00:57 | INFO | Reading frame:  651
2026-05-08 14:00:57 | INFO | Reading frame:  652
2026-05-08 14:00:57 | INFO | Reading frame:  653
2026-05-08 14:00:57 | INFO | Reading frame:  654
2026-05-08 14:00:57 | INFO | Reading frame:  655
2026-05-08 14:00:57 | INFO | Reading frame:  656
2026-05-08 14:00:57 | INFO | Reading frame:  657
2026-05-08 14:00:57 | INFO | Reading frame:  658
2026-05-08 14:00:57 | INFO | Reading frame:  659
2026-05-08 14:00:57 | INFO | Reading frame:  660
2026-05-08 14:00:57 | INFO | Reading frame:  661
2026-05-08 14:00:57 | INFO | Reading frame:  662
2026-05-08 14:00:57 | INFO | Reading frame:  663
2026-05-08 14:00:57 | INFO | Reading frame:  664
2026-05-08 14:00:57 | INFO | Reading frame:  665
2026-05-08 14:00:57 | INFO | Reading frame:  666
2026-05-08 14:00:57 | INFO | Reading frame:  667
2026-05-08 14:00:57 | INFO | Reading frame:  668
2026-05-08 14:00:57 | INFO | Reading frame:  669
2026-05-08 14:00:57 | INFO | Reading frame:  670
2026-05-08 14:00:57 | INFO | Reading frame:  671
2026-05-08 14:00:57 | INFO | Reading frame:  672
2026-05-08 14:00:57 | INFO | Reading frame:  673
2026-05-08 14:00:57 | INFO | Reading frame:  674
2026-05-08 14:00:57 | INFO | Reading frame:  675
2026-05-08 14:00:57 | INFO | Reading frame:  676
2026-05-08 14:00:57 | INFO | Reading frame:  677
2026-05-08 14:00:57 | INFO | Reading frame:  678
2026-05-08 14:00:57 | INFO | Reading frame:  679
2026-05-08 14:00:57 | INFO | Reading frame:  680
2026-05-08 14:00:57 | INFO | Reading frame:  681
2026-05-08 14:00:57 | INFO | Reading frame:  682
2026-05-08 14:00:57 | INFO | Reading frame:  683
2026-05-08 14:00:57 | INFO | Reading frame:  684
2026-05-08 14:00:57 | INFO | Reading frame:  685
2026-05-08 14:00:57 | INFO | Reading frame:  686
2026-05-08 14:00:57 | INFO | Reading frame:  687
2026-05-08 14:00:57 | INFO | Reading frame:  688
2026-05-08 14:00:57 | INFO | Reading frame:  689
2026-05-08 14:00:57 | INFO | Reading frame:  690
2026-05-08 14:00:57 | INFO | Reading frame:  691
2026-05-08 14:00:57 | INFO | Reading frame:  692
2026-05-08 14:00:57 | INFO | Reading frame:  693
2026-05-08 14:00:57 | INFO | Reading frame:  694
2026-05-08 14:00:57 | INFO | Reading frame:  695
2026-05-08 14:00:57 | INFO | Reading frame:  696
2026-05-08 14:00:57 | INFO | Reading frame:  697
2026-05-08 14:00:57 | INFO | Reading frame:  698
2026-05-08 14:00:57 | INFO | Reading frame:  699
2026-05-08 14:00:57 | INFO | Reading frame:  700
2026-05-08 14:00:57 | INFO | Reading frame:  701
2026-05-08 14:00:57 | INFO | Reading frame:  702
2026-05-08 14:00:57 | INFO | Reading frame:  703
2026-05-08 14:00:57 | INFO | Reading frame:  704
2026-05-08 14:00:57 | INFO | Reading frame:  705
2026-05-08 14:00:57 | INFO | Reading frame:  706
2026-05-08 14:00:57 | INFO | Reading frame:  707
2026-05-08 14:00:57 | INFO | Reading frame:  708
2026-05-08 14:00:57 | INFO | Reading frame:  709
2026-05-08 14:00:57 | INFO | Reading frame:  710
2026-05-08 14:00:57 | INFO | Reading frame:  711
2026-05-08 14:00:57 | INFO | Reading frame:  712
2026-05-08 14:00:57 | INFO | Reading frame:  713
2026-05-08 14:00:57 | INFO | Reading frame:  714
2026-05-08 14:00:57 | INFO | Reading frame:  715
2026-05-08 14:00:57 | INFO | Reading frame:  716
2026-05-08 14:00:57 | INFO | Reading frame:  717
2026-05-08 14:00:57 | INFO | Reading frame:  718
2026-05-08 14:00:57 | INFO | Reading frame:  719
2026-05-08 14:00:57 | INFO | Reading frame:  720
2026-05-08 14:00:57 | INFO | Reading frame:  721
2026-05-08 14:00:57 | INFO | Reading frame:  722
2026-05-08 14:00:57 | INFO | Reading frame:  723
2026-05-08 14:00:57 | INFO | Reading frame:  724
2026-05-08 14:00:57 | INFO | Reading frame:  725
2026-05-08 14:00:57 | INFO | Reading frame:  726
2026-05-08 14:00:57 | INFO | Reading frame:  727
2026-05-08 14:00:57 | INFO | Reading frame:  728
2026-05-08 14:00:57 | INFO | Reading frame:  729
2026-05-08 14:00:57 | INFO | Reading frame:  730
2026-05-08 14:00:57 | INFO | Reading frame:  731
2026-05-08 14:00:57 | INFO | Reading frame:  732
2026-05-08 14:00:57 | INFO | Reading frame:  733
2026-05-08 14:00:57 | INFO | Reading frame:  734
2026-05-08 14:00:57 | INFO | Reading frame:  735
2026-05-08 14:00:57 | INFO | Reading frame:  736
2026-05-08 14:00:57 | INFO | Reading frame:  737
2026-05-08 14:00:57 | INFO | Reading frame:  738
2026-05-08 14:00:57 | INFO | Reading frame:  739
2026-05-08 14:00:57 | INFO | Reading frame:  740
2026-05-08 14:00:57 | INFO | Reading frame:  741
2026-05-08 14:00:57 | INFO | Reading frame:  742
2026-05-08 14:00:57 | INFO | Reading frame:  743
2026-05-08 14:00:57 | INFO | Reading frame:  744
2026-05-08 14:00:57 | INFO | Reading frame:  745
2026-05-08 14:00:57 | INFO | Reading frame:  746
2026-05-08 14:00:57 | INFO | Reading frame:  747
2026-05-08 14:00:57 | INFO | Reading frame:  748
2026-05-08 14:00:57 | INFO | Reading frame:  749
2026-05-08 14:00:57 | INFO | Reading frame:  750
2026-05-08 14:00:57 | INFO | Reading frame:  751
2026-05-08 14:00:57 | INFO | Reading frame:  752
2026-05-08 14:00:57 | INFO | Reading frame:  753
2026-05-08 14:00:57 | INFO | Reading frame:  754
2026-05-08 14:00:57 | INFO | Reading frame:  755
2026-05-08 14:00:57 | INFO | Reading frame:  756
2026-05-08 14:00:57 | INFO | Reading frame:  757
2026-05-08 14:00:57 | INFO | Reading frame:  758
2026-05-08 14:00:57 | INFO | Reading frame:  759
2026-05-08 14:00:57 | INFO | Reading frame:  760
2026-05-08 14:00:57 | INFO | Reading frame:  761
2026-05-08 14:00:57 | INFO | Reading frame:  762
2026-05-08 14:00:57 | INFO | Reading frame:  763
2026-05-08 14:00:57 | INFO | Reading frame:  764
2026-05-08 14:00:57 | INFO | Reading frame:  765
2026-05-08 14:00:57 | INFO | Reading frame:  766
2026-05-08 14:00:57 | INFO | Reading frame:  767
2026-05-08 14:00:57 | INFO | Reading frame:  768
2026-05-08 14:00:57 | INFO | Reading frame:  769
2026-05-08 14:00:57 | INFO | Reading frame:  770
2026-05-08 14:00:57 | INFO | Reading frame:  771
2026-05-08 14:00:57 | INFO | Reading frame:  772
2026-05-08 14:00:57 | INFO | Reading frame:  773
2026-05-08 14:00:57 | INFO | Reading frame:  774
2026-05-08 14:00:57 | INFO | Reading frame:  775
2026-05-08 14:00:57 | INFO | Reading frame:  776
2026-05-08 14:00:57 | INFO | Reading frame:  777
2026-05-08 14:00:57 | INFO | Reading frame:  778
2026-05-08 14:00:57 | INFO | Reading frame:  779
2026-05-08 14:00:57 | INFO | Reading frame:  780
2026-05-08 14:00:57 | INFO | Reading frame:  781
2026-05-08 14:00:57 | INFO | Reading frame:  782
2026-05-08 14:00:57 | INFO | Reading frame:  783
2026-05-08 14:00:57 | INFO | Reading frame:  784
2026-05-08 14:00:57 | INFO | Reading frame:  785
2026-05-08 14:00:57 | INFO | Reading frame:  786
2026-05-08 14:00:57 | INFO | Reading frame:  787
2026-05-08 14:00:57 | INFO | Reading frame:  788
2026-05-08 14:00:57 | INFO | Reading frame:  789
2026-05-08 14:00:57 | INFO | Reading frame:  790
2026-05-08 14:00:57 | INFO | Reading frame:  791
2026-05-08 14:00:57 | INFO | Reading frame:  792
2026-05-08 14:00:57 | INFO | Reading frame:  793
2026-05-08 14:00:57 | INFO | Reading frame:  794
2026-05-08 14:00:57 | INFO | Reading frame:  795
2026-05-08 14:00:57 | INFO | Reading frame:  796
2026-05-08 14:00:57 | INFO | Reading frame:  797
2026-05-08 14:00:57 | INFO | Reading frame:  798
2026-05-08 14:00:59 | INFO | Reading frame:  799
2026-05-08 14:00:59 | INFO | Reading frame:  800
2026-05-08 14:00:59 | INFO | Reading frame:  801
2026-05-08 14:00:59 | INFO | Reading frame:  802
2026-05-08 14:00:59 | INFO | Reading frame:  803
2026-05-08 14:00:59 | INFO | Reading frame:  804
2026-05-08 14:00:59 | INFO | Reading frame:  805
2026-05-08 14:00:59 | INFO | Reading frame:  806
2026-05-08 14:00:59 | INFO | Reading frame:  807
2026-05-08 14:00:59 | INFO | Reading frame:  808
2026-05-08 14:00:59 | INFO | Reading frame:  809
2026-05-08 14:00:59 | INFO | Reading frame:  810
2026-05-08 14:00:59 | INFO | Reading frame:  811
2026-05-08 14:00:59 | INFO | Reading frame:  812
2026-05-08 14:00:59 | INFO | Reading frame:  813
2026-05-08 14:00:59 | INFO | Reading frame:  814
2026-05-08 14:00:59 | INFO | Reading frame:  815
2026-05-08 14:00:59 | INFO | Reading frame:  816
2026-05-08 14:00:59 | INFO | Reading frame:  817
2026-05-08 14:00:59 | INFO | Reading frame:  818
2026-05-08 14:00:59 | INFO | Reading frame:  819
2026-05-08 14:00:59 | INFO | Reading frame:  820
2026-05-08 14:00:59 | INFO | Reading frame:  821
2026-05-08 14:00:59 | INFO | Reading frame:  822
2026-05-08 14:00:59 | INFO | Reading frame:  823
2026-05-08 14:00:59 | INFO | Reading frame:  824
2026-05-08 14:00:59 | INFO | Reading frame:  825
2026-05-08 14:00:59 | INFO | Reading frame:  826
2026-05-08 14:00:59 | INFO | Reading frame:  827
2026-05-08 14:00:59 | INFO | Reading frame:  828
2026-05-08 14:00:59 | INFO | Reading frame:  829
2026-05-08 14:00:59 | INFO | Reading frame:  830
2026-05-08 14:00:59 | INFO | Reading frame:  831
2026-05-08 14:00:59 | INFO | Reading frame:  832
2026-05-08 14:00:59 | INFO | Reading frame:  833
2026-05-08 14:00:59 | INFO | Reading frame:  834
2026-05-08 14:00:59 | INFO | Reading frame:  835
2026-05-08 14:00:59 | INFO | Reading frame:  836
2026-05-08 14:00:59 | INFO | Reading frame:  837
2026-05-08 14:00:59 | INFO | Reading frame:  838
2026-05-08 14:00:59 | INFO | Reading frame:  839
2026-05-08 14:00:59 | INFO | Reading frame:  840
2026-05-08 14:00:59 | INFO | Reading frame:  841
2026-05-08 14:00:59 | INFO | Reading frame:  842
2026-05-08 14:00:59 | INFO | Reading frame:  843
2026-05-08 14:00:59 | INFO | Reading frame:  844
2026-05-08 14:00:59 | INFO | Reading frame:  845
2026-05-08 14:00:59 | INFO | Reading frame:  846
2026-05-08 14:00:59 | INFO | Reading frame:  847
2026-05-08 14:00:59 | INFO | Reading frame:  848
2026-05-08 14:00:59 | INFO | Reading frame:  849
2026-05-08 14:00:59 | INFO | Reading frame:  850
2026-05-08 14:00:59 | INFO | Reading frame:  851
2026-05-08 14:00:59 | INFO | Reading frame:  852
2026-05-08 14:00:59 | INFO | Reading frame:  853
2026-05-08 14:00:59 | INFO | Reading frame:  854
2026-05-08 14:00:59 | INFO | Reading frame:  855
2026-05-08 14:00:59 | INFO | Reading frame:  856
2026-05-08 14:00:59 | INFO | Reading frame:  857
2026-05-08 14:00:59 | INFO | Reading frame:  858
2026-05-08 14:00:59 | INFO | Reading frame:  859
2026-05-08 14:00:59 | INFO | Reading frame:  860
2026-05-08 14:00:59 | INFO | Reading frame:  861
2026-05-08 14:00:59 | INFO | Reading frame:  862
2026-05-08 14:00:59 | INFO | Reading frame:  863
2026-05-08 14:00:59 | INFO | Reading frame:  864
2026-05-08 14:00:59 | INFO | Reading frame:  865
2026-05-08 14:00:59 | INFO | Reading frame:  866
2026-05-08 14:00:59 | INFO | Reading frame:  867
2026-05-08 14:00:59 | INFO | Reading frame:  868
2026-05-08 14:00:59 | INFO | Reading frame:  869
2026-05-08 14:00:59 | INFO | Reading frame:  870
2026-05-08 14:00:59 | INFO | Reading frame:  871
2026-05-08 14:00:59 | INFO | Reading frame:  872
2026-05-08 14:00:59 | INFO | Reading frame:  873
2026-05-08 14:00:59 | INFO | Reading frame:  874
2026-05-08 14:00:59 | INFO | Reading frame:  875
2026-05-08 14:00:59 | INFO | Reading frame:  876
2026-05-08 14:00:59 | INFO | Reading frame:  877
2026-05-08 14:00:59 | INFO | Reading frame:  878
2026-05-08 14:00:59 | INFO | Reading frame:  879
2026-05-08 14:00:59 | INFO | Reading frame:  880
2026-05-08 14:00:59 | INFO | Reading frame:  881
2026-05-08 14:00:59 | INFO | Reading frame:  882
2026-05-08 14:00:59 | INFO | Reading frame:  883
2026-05-08 14:00:59 | INFO | Reading frame:  884
2026-05-08 14:00:59 | INFO | Reading frame:  885
2026-05-08 14:00:59 | INFO | Reading frame:  886
2026-05-08 14:00:59 | INFO | Reading frame:  887
2026-05-08 14:00:59 | INFO | Reading frame:  888
2026-05-08 14:00:59 | INFO | Reading frame:  889
2026-05-08 14:00:59 | INFO | Reading frame:  890
2026-05-08 14:00:59 | INFO | Reading frame:  891
2026-05-08 14:00:59 | INFO | Reading frame:  892
2026-05-08 14:00:59 | INFO | Reading frame:  893
2026-05-08 14:00:59 | INFO | Reading frame:  894
2026-05-08 14:00:59 | INFO | Reading frame:  895
2026-05-08 14:00:59 | INFO | Reading frame:  896
2026-05-08 14:00:59 | INFO | Reading frame:  897
2026-05-08 14:00:59 | INFO | Reading frame:  898
2026-05-08 14:00:59 | INFO | Reading frame:  899
2026-05-08 14:00:59 | INFO | Reading frame:  900
2026-05-08 14:00:59 | INFO | Reading frame:  901
2026-05-08 14:00:59 | INFO | Reading frame:  902
2026-05-08 14:00:59 | INFO | Reading frame:  903
2026-05-08 14:00:59 | INFO | Reading frame:  904
2026-05-08 14:00:59 | INFO | Reading frame:  905
2026-05-08 14:00:59 | INFO | Reading frame:  906
2026-05-08 14:00:59 | INFO | Reading frame:  907
2026-05-08 14:00:59 | INFO | Reading frame:  908
2026-05-08 14:00:59 | INFO | Reading frame:  909
2026-05-08 14:00:59 | INFO | Reading frame:  910
2026-05-08 14:00:59 | INFO | Reading frame:  911
2026-05-08 14:00:59 | INFO | Reading frame:  912
2026-05-08 14:00:59 | INFO | Reading frame:  913
2026-05-08 14:00:59 | INFO | Reading frame:  914
2026-05-08 14:00:59 | INFO | Reading frame:  915
2026-05-08 14:00:59 | INFO | Reading frame:  916
2026-05-08 14:00:59 | INFO | Reading frame:  917
2026-05-08 14:00:59 | INFO | Reading frame:  918
2026-05-08 14:00:59 | INFO | Reading frame:  919
2026-05-08 14:00:59 | INFO | Reading frame:  920
2026-05-08 14:00:59 | INFO | Reading frame:  921
2026-05-08 14:00:59 | INFO | Reading frame:  922
2026-05-08 14:00:59 | INFO | Reading frame:  923
2026-05-08 14:00:59 | INFO | Reading frame:  924
2026-05-08 14:00:59 | INFO | Reading frame:  925
2026-05-08 14:00:59 | INFO | Reading frame:  926
2026-05-08 14:00:59 | INFO | Reading frame:  927
2026-05-08 14:00:59 | INFO | Reading frame:  928
2026-05-08 14:00:59 | INFO | Reading frame:  929
2026-05-08 14:00:59 | INFO | Reading frame:  930
2026-05-08 14:00:59 | INFO | Reading frame:  931
2026-05-08 14:00:59 | INFO | Reading frame:  932
2026-05-08 14:00:59 | INFO | Reading frame:  933
2026-05-08 14:00:59 | INFO | Reading frame:  934
2026-05-08 14:00:59 | INFO | Reading frame:  935
2026-05-08 14:00:59 | INFO | Reading frame:  936
2026-05-08 14:00:59 | INFO | Reading frame:  937
2026-05-08 14:00:59 | INFO | Reading frame:  938
2026-05-08 14:00:59 | INFO | Reading frame:  939
2026-05-08 14:00:59 | INFO | Reading frame:  940
2026-05-08 14:00:59 | INFO | Reading frame:  941
2026-05-08 14:00:59 | INFO | Reading frame:  942
2026-05-08 14:00:59 | INFO | Reading frame:  943
2026-05-08 14:00:59 | INFO | Reading frame:  944
2026-05-08 14:00:59 | INFO | Reading frame:  945
2026-05-08 14:00:59 | INFO | Reading frame:  946
2026-05-08 14:00:59 | INFO | Reading frame:  947
2026-05-08 14:00:59 | INFO | Reading frame:  948
2026-05-08 14:00:59 | INFO | Reading frame:  949
2026-05-08 14:00:59 | INFO | Reading frame:  950
2026-05-08 14:00:59 | INFO | Reading frame:  951
2026-05-08 14:00:59 | INFO | Reading frame:  952
2026-05-08 14:00:59 | INFO | Reading frame:  953
2026-05-08 14:00:59 | INFO | Reading frame:  954
2026-05-08 14:00:59 | INFO | Reading frame:  955
2026-05-08 14:00:59 | INFO | Reading frame:  956
2026-05-08 14:00:59 | INFO | Reading frame:  957
2026-05-08 14:00:59 | INFO | Reading frame:  958
2026-05-08 14:00:59 | INFO | Reading frame:  959
2026-05-08 14:00:59 | INFO | Reading frame:  960
2026-05-08 14:00:59 | INFO | Reading frame:  961
2026-05-08 14:00:59 | INFO | Reading frame:  962
2026-05-08 14:00:59 | INFO | Reading frame:  963
2026-05-08 14:00:59 | INFO | Reading frame:  964
2026-05-08 14:00:59 | INFO | Reading frame:  965
2026-05-08 14:00:59 | INFO | Reading frame:  966
2026-05-08 14:00:59 | INFO | Reading frame:  967
2026-05-08 14:00:59 | INFO | Reading frame:  968
2026-05-08 14:00:59 | INFO | Reading frame:  969
2026-05-08 14:00:59 | INFO | Reading frame:  970
2026-05-08 14:00:59 | INFO | Reading frame:  971
2026-05-08 14:00:59 | INFO | Reading frame:  972
2026-05-08 14:00:59 | INFO | Reading frame:  973
2026-05-08 14:00:59 | INFO | Reading frame:  974
2026-05-08 14:00:59 | INFO | Reading frame:  975
2026-05-08 14:00:59 | INFO | Reading frame:  976
2026-05-08 14:00:59 | INFO | Reading frame:  977
2026-05-08 14:00:59 | INFO | Reading frame:  978
2026-05-08 14:00:59 | INFO | Reading frame:  979
2026-05-08 14:00:59 | INFO | Reading frame:  980
2026-05-08 14:00:59 | INFO | Reading frame:  981
2026-05-08 14:00:59 | INFO | Reading frame:  982
2026-05-08 14:00:59 | INFO | Reading frame:  983
2026-05-08 14:00:59 | INFO | Reading frame:  984
2026-05-08 14:00:59 | INFO | Reading frame:  985
2026-05-08 14:00:59 | INFO | Reading frame:  986
2026-05-08 14:00:59 | INFO | Reading frame:  987
2026-05-08 14:00:59 | INFO | Reading frame:  988
2026-05-08 14:00:59 | INFO | Reading frame:  989
2026-05-08 14:00:59 | INFO | Reading frame:  990
2026-05-08 14:00:59 | INFO | Reading frame:  991
2026-05-08 14:00:59 | INFO | Reading frame:  992
2026-05-08 14:00:59 | INFO | Reading frame:  993
2026-05-08 14:00:59 | INFO | Reading frame:  994
2026-05-08 14:00:59 | INFO | Reading frame:  995
2026-05-08 14:00:59 | INFO | Reading frame:  996
2026-05-08 14:00:59 | INFO | Reading frame:  997
2026-05-08 14:00:59 | INFO | Reading frame:  998
2026-05-08 14:00:59 | INFO | Reading frame:  999
2026-05-08 14:00:59 | INFO | Reading frame:  1000
2026-05-08 14:00:59 | INFO | Reading frame:  1001
2026-05-08 14:00:59 | INFO | Reading frame:  1002
2026-05-08 14:00:59 | INFO | Reading frame:  1003
2026-05-08 14:00:59 | INFO | Reading frame:  1004
2026-05-08 14:00:59 | INFO | Reading frame:  1005
2026-05-08 14:00:59 | INFO | Reading frame:  1006
2026-05-08 14:00:59 | INFO | Reading frame:  1007
2026-05-08 14:00:59 | INFO | Reading frame:  1008
2026-05-08 14:00:59 | INFO | Reading frame:  1009
2026-05-08 14:00:59 | INFO | Reading frame:  1010
2026-05-08 14:00:59 | INFO | Reading frame:  1011
2026-05-08 14:00:59 | INFO | Reading frame:  1012
2026-05-08 14:00:59 | INFO | Reading frame:  1013
2026-05-08 14:00:59 | INFO | Reading frame:  1014
2026-05-08 14:00:59 | INFO | Reading frame:  1015
2026-05-08 14:00:59 | INFO | Reading frame:  1016
2026-05-08 14:00:59 | INFO | Reading frame:  1017
2026-05-08 14:00:59 | INFO | Reading frame:  1018
2026-05-08 14:00:59 | INFO | Reading frame:  1019
2026-05-08 14:00:59 | INFO | Reading frame:  1020
2026-05-08 14:00:59 | INFO | Reading frame:  1021
2026-05-08 14:00:59 | INFO | Reading frame:  1022
2026-05-08 14:00:59 | INFO | Reading frame:  1023
2026-05-08 14:00:59 | INFO | Reading frame:  1024
2026-05-08 14:00:59 | INFO | Reading frame:  1025
2026-05-08 14:00:59 | INFO | Reading frame:  1026
2026-05-08 14:00:59 | INFO | Reading frame:  1027
2026-05-08 14:00:59 | INFO | Reading frame:  1028
2026-05-08 14:00:59 | INFO | Reading frame:  1029
2026-05-08 14:00:59 | INFO | Reading frame:  1030
2026-05-08 14:00:59 | INFO | Reading frame:  1031
2026-05-08 14:00:59 | INFO | Reading frame:  1032
2026-05-08 14:00:59 | INFO | Reading frame:  1033
2026-05-08 14:00:59 | INFO | Reading frame:  1034
2026-05-08 14:00:59 | INFO | Reading frame:  1035
2026-05-08 14:00:59 | INFO | Reading frame:  1036
2026-05-08 14:00:59 | INFO | Reading frame:  1037
2026-05-08 14:00:59 | INFO | Reading frame:  1038
2026-05-08 14:00:59 | INFO | Reading frame:  1039
2026-05-08 14:00:59 | INFO | Reading frame:  1040
2026-05-08 14:00:59 | INFO | Reading frame:  1041
2026-05-08 14:00:59 | INFO | Reading frame:  1042
2026-05-08 14:00:59 | INFO | Reading frame:  1043
2026-05-08 14:00:59 | INFO | Reading frame:  1044
2026-05-08 14:00:59 | INFO | Reading frame:  1045
2026-05-08 14:00:59 | INFO | Reading frame:  1046
2026-05-08 14:00:59 | INFO | Reading frame:  1047
2026-05-08 14:00:59 | INFO | Reading frame:  1048
2026-05-08 14:00:59 | INFO | Reading frame:  1049
2026-05-08 14:00:59 | INFO | Reading frame:  1050
2026-05-08 14:00:59 | INFO | Reading frame:  1051
2026-05-08 14:00:59 | INFO | Reading frame:  1052
2026-05-08 14:00:59 | INFO | Reading frame:  1053
2026-05-08 14:00:59 | INFO | Reading frame:  1054
2026-05-08 14:00:59 | INFO | Reading frame:  1055
2026-05-08 14:00:59 | INFO | Reading frame:  1056
2026-05-08 14:00:59 | INFO | Reading frame:  1057
2026-05-08 14:00:59 | INFO | Reading frame:  1058
2026-05-08 14:00:59 | INFO | Reading frame:  1059
2026-05-08 14:00:59 | INFO | Reading frame:  1060
2026-05-08 14:00:59 | INFO | Reading frame:  1061
2026-05-08 14:00:59 | INFO | Reading frame:  1062
2026-05-08 14:00:59 | INFO | Reading frame:  1063
2026-05-08 14:00:59 | INFO | Reading frame:  1064
2026-05-08 14:00:59 | INFO | Reading frame:  1065
2026-05-08 14:00:59 | INFO | Reading frame:  1066
2026-05-08 14:00:59 | INFO | Reading frame:  1067
2026-05-08 14:00:59 | INFO | Reading frame:  1068
2026-05-08 14:00:59 | INFO | Reading frame:  1069
2026-05-08 14:00:59 | INFO | Reading frame:  1070
2026-05-08 14:00:59 | INFO | Reading frame:  1071
2026-05-08 14:00:59 | INFO | Reading frame:  1072
2026-05-08 14:00:59 | INFO | Reading frame:  1073
2026-05-08 14:00:59 | INFO | Reading frame:  1074
2026-05-08 14:00:59 | INFO | Reading frame:  1075
2026-05-08 14:00:59 | INFO | Reading frame:  1076
2026-05-08 14:00:59 | INFO | Reading frame:  1077
2026-05-08 14:00:59 | INFO | Reading frame:  1078
2026-05-08 14:00:59 | INFO | Reading frame:  1079
2026-05-08 14:00:59 | INFO | Reading frame:  1080
2026-05-08 14:00:59 | INFO | Reading frame:  1081
2026-05-08 14:00:59 | INFO | Reading frame:  1082
2026-05-08 14:00:59 | INFO | Reading frame:  1083
2026-05-08 14:00:59 | INFO | Reading frame:  1084
2026-05-08 14:00:59 | INFO | Reading frame:  1085
2026-05-08 14:00:59 | INFO | Reading frame:  1086
2026-05-08 14:00:59 | INFO | Reading frame:  1087
2026-05-08 14:00:59 | INFO | Reading frame:  1088
2026-05-08 14:00:59 | INFO | Reading frame:  1089
2026-05-08 14:00:59 | INFO | Reading frame:  1090
2026-05-08 14:00:59 | INFO | Reading frame:  1091
2026-05-08 14:00:59 | INFO | Reading frame:  1092
2026-05-08 14:00:59 | INFO | Reading frame:  1093
2026-05-08 14:00:59 | INFO | Reading frame:  1094
2026-05-08 14:00:59 | INFO | Reading frame:  1095
2026-05-08 14:00:59 | INFO | Reading frame:  1096
2026-05-08 14:00:59 | INFO | Reading frame:  1097
2026-05-08 14:00:59 | INFO | Reading frame:  1098
2026-05-08 14:00:59 | INFO | Reading frame:  1099
2026-05-08 14:00:59 | INFO | Reading frame:  1100
2026-05-08 14:00:59 | INFO | Reading frame:  1101
2026-05-08 14:00:59 | INFO | Reading frame:  1102
2026-05-08 14:00:59 | INFO | Reading frame:  1103
2026-05-08 14:00:59 | INFO | Reading frame:  1104
2026-05-08 14:00:59 | INFO | Reading frame:  1105
2026-05-08 14:00:59 | INFO | Reading frame:  1106
2026-05-08 14:00:59 | INFO | Reading frame:  1107
2026-05-08 14:00:59 | INFO | Reading frame:  1108
2026-05-08 14:00:59 | INFO | Reading frame:  1109
2026-05-08 14:00:59 | INFO | Reading frame:  1110
2026-05-08 14:00:59 | INFO | Reading frame:  1111
2026-05-08 14:00:59 | INFO | Reading frame:  1112
2026-05-08 14:00:59 | INFO | Reading frame:  1113
2026-05-08 14:00:59 | INFO | Reading frame:  1114
2026-05-08 14:00:59 | INFO | Reading frame:  1115
2026-05-08 14:00:59 | INFO | Reading frame:  1116
2026-05-08 14:00:59 | INFO | Reading frame:  1117
2026-05-08 14:00:59 | INFO | Reading frame:  1118
2026-05-08 14:00:59 | INFO | Reading frame:  1119
2026-05-08 14:00:59 | INFO | Reading frame:  1120
2026-05-08 14:00:59 | INFO | Reading frame:  1121
2026-05-08 14:00:59 | INFO | Reading frame:  1122
2026-05-08 14:00:59 | INFO | Reading frame:  1123
2026-05-08 14:00:59 | INFO | Reading frame:  1124
2026-05-08 14:00:59 | INFO | Reading frame:  1125
2026-05-08 14:00:59 | INFO | Reading frame:  1126
2026-05-08 14:00:59 | INFO | Reading frame:  1127
2026-05-08 14:00:59 | INFO | Reading frame:  1128
2026-05-08 14:00:59 | INFO | Reading frame:  1129
2026-05-08 14:00:59 | INFO | Reading frame:  1130
2026-05-08 14:00:59 | INFO | Reading frame:  1131
2026-05-08 14:00:59 | INFO | Reading frame:  1132
2026-05-08 14:00:59 | INFO | Reading frame:  1133
2026-05-08 14:00:59 | INFO | Reading frame:  1134
2026-05-08 14:00:59 | INFO | Reading frame:  1135
2026-05-08 14:00:59 | INFO | Reading frame:  1136
2026-05-08 14:00:59 | INFO | Reading frame:  1137
2026-05-08 14:00:59 | INFO | Reading frame:  1138
2026-05-08 14:00:59 | INFO | Reading frame:  1139
2026-05-08 14:00:59 | INFO | Reading frame:  1140
2026-05-08 14:00:59 | INFO | Reading frame:  1141
2026-05-08 14:00:59 | INFO | Reading frame:  1142
2026-05-08 14:00:59 | INFO | Reading frame:  1143
2026-05-08 14:00:59 | INFO | Reading frame:  1144
2026-05-08 14:00:59 | INFO | Reading frame:  1145
2026-05-08 14:00:59 | INFO | Reading frame:  1146
2026-05-08 14:00:59 | INFO | Reading frame:  1147
2026-05-08 14:00:59 | INFO | Reading frame:  1148
2026-05-08 14:00:59 | INFO | Reading frame:  1149
2026-05-08 14:00:59 | INFO | Reading frame:  1150
2026-05-08 14:00:59 | INFO | Reading frame:  1151
2026-05-08 14:00:59 | INFO | Reading frame:  1152
2026-05-08 14:00:59 | INFO | Reading frame:  1153
2026-05-08 14:00:59 | INFO | Reading frame:  1154
2026-05-08 14:00:59 | INFO | Reading frame:  1155
2026-05-08 14:00:59 | INFO | Reading frame:  1156
2026-05-08 14:00:59 | INFO | Reading frame:  1157
2026-05-08 14:00:59 | INFO | Reading frame:  1158
2026-05-08 14:00:59 | INFO | Reading frame:  1159
2026-05-08 14:00:59 | INFO | Reading frame:  1160
2026-05-08 14:00:59 | INFO | Reading frame:  1161
2026-05-08 14:00:59 | INFO | Reading frame:  1162
2026-05-08 14:00:59 | INFO | Reading frame:  1163
2026-05-08 14:00:59 | INFO | Reading frame:  1164
2026-05-08 14:00:59 | INFO | Reading frame:  1165
2026-05-08 14:00:59 | INFO | Reading frame:  1166
2026-05-08 14:00:59 | INFO | Reading frame:  1167
2026-05-08 14:00:59 | INFO | Reading frame:  1168
2026-05-08 14:00:59 | INFO | Reading frame:  1169
2026-05-08 14:00:59 | INFO | Reading frame:  1170
2026-05-08 14:00:59 | INFO | Reading frame:  1171
2026-05-08 14:00:59 | INFO | Reading frame:  1172
2026-05-08 14:00:59 | INFO | Reading frame:  1173
2026-05-08 14:00:59 | INFO | Reading frame:  1174
2026-05-08 14:00:59 | INFO | Reading frame:  1175
2026-05-08 14:00:59 | INFO | Reading frame:  1176
2026-05-08 14:00:59 | INFO | Reading frame:  1177
2026-05-08 14:00:59 | INFO | Reading frame:  1178
2026-05-08 14:00:59 | INFO | Reading frame:  1179
2026-05-08 14:00:59 | INFO | Reading frame:  1180
2026-05-08 14:00:59 | INFO | Reading frame:  1181
2026-05-08 14:00:59 | INFO | Reading frame:  1182
2026-05-08 14:00:59 | INFO | Reading frame:  1183
2026-05-08 14:00:59 | INFO | Reading frame:  1184
2026-05-08 14:00:59 | INFO | Reading frame:  1185
2026-05-08 14:00:59 | INFO | Reading frame:  1186
2026-05-08 14:00:59 | INFO | Reading frame:  1187
2026-05-08 14:00:59 | INFO | Reading frame:  1188
2026-05-08 14:00:59 | INFO | Reading frame:  1189
2026-05-08 14:00:59 | INFO | Reading frame:  1190
2026-05-08 14:00:59 | INFO | Reading frame:  1191
2026-05-08 14:00:59 | INFO | Reading frame:  1192
2026-05-08 14:00:59 | INFO | Reading frame:  1193
2026-05-08 14:00:59 | INFO | Reading frame:  1194
2026-05-08 14:00:59 | INFO | Reading frame:  1195
2026-05-08 14:00:59 | INFO | Reading frame:  1196
2026-05-08 14:00:59 | INFO | Reading frame:  1197
2026-05-08 14:00:59 | INFO | Reading frame:  1198
2026-05-08 14:00:59 | INFO | Reading frame:  1199
2026-05-08 14:00:59 | INFO | Reading frame:  1200
2026-05-08 14:00:59 | INFO | Reading frame:  1201
2026-05-08 14:00:59 | INFO | Reading frame:  1202
2026-05-08 14:00:59 | INFO | Reading frame:  1203
2026-05-08 14:00:59 | INFO | Reading frame:  1204
2026-05-08 14:00:59 | INFO | Reading frame:  1205
2026-05-08 14:00:59 | INFO | Reading frame:  1206
2026-05-08 14:00:59 | INFO | Reading frame:  1207
2026-05-08 14:00:59 | INFO | Reading frame:  1208
2026-05-08 14:00:59 | INFO | Reading frame:  1209
2026-05-08 14:00:59 | INFO | Reading frame:  1210
2026-05-08 14:00:59 | INFO | Reading frame:  1211
2026-05-08 14:00:59 | INFO | Reading frame:  1212
2026-05-08 14:00:59 | INFO | Reading frame:  1213
2026-05-08 14:00:59 | INFO | Reading frame:  1214
2026-05-08 14:00:59 | INFO | Reading frame:  1215
2026-05-08 14:00:59 | INFO | Reading frame:  1216
2026-05-08 14:00:59 | INFO | Reading frame:  1217
2026-05-08 14:00:59 | INFO | Reading frame:  1218
2026-05-08 14:00:59 | INFO | Reading frame:  1219
2026-05-08 14:00:59 | INFO | Reading frame:  1220
2026-05-08 14:00:59 | INFO | Reading frame:  1221
2026-05-08 14:00:59 | INFO | Reading frame:  1222
2026-05-08 14:00:59 | INFO | Reading frame:  1223
2026-05-08 14:00:59 | INFO | Reading frame:  1224
2026-05-08 14:00:59 | INFO | Reading frame:  1225
2026-05-08 14:00:59 | INFO | Reading frame:  1226
2026-05-08 14:00:59 | INFO | Reading frame:  1227
2026-05-08 14:00:59 | INFO | Reading frame:  1228
2026-05-08 14:00:59 | INFO | Reading frame:  1229
2026-05-08 14:00:59 | INFO | Reading frame:  1230
2026-05-08 14:00:59 | INFO | Reading frame:  1231
2026-05-08 14:00:59 | INFO | Reading frame:  1232
2026-05-08 14:00:59 | INFO | Reading frame:  1233
2026-05-08 14:00:59 | INFO | Reading frame:  1234
2026-05-08 14:00:59 | INFO | Reading frame:  1235
2026-05-08 14:00:59 | INFO | Reading frame:  1236
2026-05-08 14:00:59 | INFO | Reading frame:  1237
2026-05-08 14:00:59 | INFO | Reading frame:  1238
2026-05-08 14:00:59 | INFO | Reading frame:  1239
2026-05-08 14:00:59 | INFO | Reading frame:  1240
2026-05-08 14:00:59 | INFO | Reading frame:  1241
2026-05-08 14:00:59 | INFO | Reading frame:  1242
2026-05-08 14:00:59 | INFO | Reading frame:  1243
2026-05-08 14:00:59 | INFO | Reading frame:  1244
2026-05-08 14:00:59 | INFO | Reading frame:  1245
2026-05-08 14:00:59 | INFO | Reading frame:  1246
2026-05-08 14:00:59 | INFO | Reading frame:  1247
2026-05-08 14:00:59 | INFO | Reading frame:  1248
2026-05-08 14:00:59 | INFO | Reading frame:  1249
2026-05-08 14:00:59 | INFO | Reading frame:  1250
2026-05-08 14:00:59 | INFO | Reading frame:  1251
2026-05-08 14:00:59 | INFO | Reading frame:  1252
2026-05-08 14:00:59 | INFO | Reading frame:  1253
2026-05-08 14:00:59 | INFO | Reading frame:  1254
2026-05-08 14:00:59 | INFO | Reading frame:  1255
2026-05-08 14:00:59 | INFO | Reading frame:  1256
2026-05-08 14:00:59 | INFO | Reading frame:  1257
2026-05-08 14:00:59 | INFO | Reading frame:  1258
2026-05-08 14:00:59 | INFO | Reading frame:  1259
2026-05-08 14:00:59 | INFO | Reading frame:  1260
2026-05-08 14:00:59 | INFO | Reading frame:  1261
2026-05-08 14:00:59 | INFO | Reading frame:  1262
2026-05-08 14:00:59 | INFO | Reading frame:  1263
2026-05-08 14:00:59 | INFO | Reading frame:  1264
2026-05-08 14:00:59 | INFO | Reading frame:  1265
2026-05-08 14:00:59 | INFO | Reading frame:  1266
2026-05-08 14:00:59 | INFO | Reading frame:  1267
2026-05-08 14:00:59 | INFO | Reading frame:  1268
2026-05-08 14:00:59 | INFO | Reading frame:  1269
2026-05-08 14:00:59 | INFO | Reading frame:  1270
2026-05-08 14:00:59 | INFO | Reading frame:  1271
2026-05-08 14:00:59 | INFO | Reading frame:  1272
2026-05-08 14:00:59 | INFO | Reading frame:  1273
2026-05-08 14:00:59 | INFO | Reading frame:  1274
2026-05-08 14:00:59 | INFO | Reading frame:  1275
2026-05-08 14:00:59 | INFO | Reading frame:  1276
2026-05-08 14:00:59 | INFO | Reading frame:  1277
2026-05-08 14:00:59 | INFO | Reading frame:  1278
2026-05-08 14:00:59 | INFO | Reading frame:  1279
2026-05-08 14:00:59 | INFO | Reading frame:  1280
2026-05-08 14:00:59 | INFO | 🔍 Detecting stable segments...
2026-05-08 14:00:59 | INFO | 
2026-05-08 14:00:59 | INFO | Loading weights:   0%|          | 0/398 [00:00<?, ?it/s]
2026-05-08 14:00:59 | INFO | Loading weights: 100%|██████████| 398/398 [00:00<00:00, 66499.34it/s]
2026-05-08 14:00:59 | INFO | [1mCLIPModel LOAD REPORT[0m from: openai/clip-vit-base-patch32
2026-05-08 14:00:59 | INFO | Key                                  | Status     |  | 
2026-05-08 14:00:59 | INFO | -------------------------------------+------------+--+-
2026-05-08 14:00:59 | INFO | text_model.embeddings.position_ids   | UNEXPECTED |  | 
2026-05-08 14:00:59 | INFO | vision_model.embeddings.position_ids | UNEXPECTED |  | 
2026-05-08 14:00:59 | INFO | 
2026-05-08 14:00:59 | INFO | Notes:
2026-05-08 14:00:59 | INFO | - UNEXPECTED:	can be ignored when loading from different task/architecture; not ok if you expect identical arch.
2026-05-08 14:03:08 | INFO | Encoding frames with CLIP...
2026-05-08 14:03:08 | INFO |   Encoded 1/1280
2026-05-08 14:03:08 | INFO |   Encoded 2/1280
2026-05-08 14:03:08 | INFO |   Encoded 3/1280
2026-05-08 14:03:08 | INFO |   Encoded 4/1280
2026-05-08 14:03:08 | INFO |   Encoded 5/1280
2026-05-08 14:03:08 | INFO |   Encoded 6/1280
2026-05-08 14:03:08 | INFO |   Encoded 7/1280
2026-05-08 14:03:08 | INFO |   Encoded 8/1280
2026-05-08 14:03:08 | INFO |   Encoded 9/1280
2026-05-08 14:03:08 | INFO |   Encoded 10/1280
2026-05-08 14:03:08 | INFO |   Encoded 11/1280
2026-05-08 14:03:08 | INFO |   Encoded 12/1280
2026-05-08 14:03:08 | INFO |   Encoded 13/1280
2026-05-08 14:03:08 | INFO |   Encoded 14/1280
2026-05-08 14:03:08 | INFO |   Encoded 15/1280
2026-05-08 14:03:08 | INFO |   Encoded 16/1280
2026-05-08 14:03:08 | INFO |   Encoded 17/1280
2026-05-08 14:03:08 | INFO |   Encoded 18/1280
2026-05-08 14:03:08 | INFO |   Encoded 19/1280
2026-05-08 14:03:08 | INFO |   Encoded 20/1280
2026-05-08 14:03:08 | INFO |   Encoded 21/1280
2026-05-08 14:03:08 | INFO |   Encoded 22/1280
2026-05-08 14:03:08 | INFO |   Encoded 23/1280
2026-05-08 14:03:08 | INFO |   Encoded 24/1280
2026-05-08 14:03:08 | INFO |   Encoded 25/1280
2026-05-08 14:03:08 | INFO |   Encoded 26/1280
2026-05-08 14:03:08 | INFO |   Encoded 27/1280
2026-05-08 14:03:08 | INFO |   Encoded 28/1280
2026-05-08 14:03:08 | INFO |   Encoded 29/1280
2026-05-08 14:03:08 | INFO |   Encoded 30/1280
2026-05-08 14:03:08 | INFO |   Encoded 31/1280
2026-05-08 14:03:08 | INFO |   Encoded 32/1280
2026-05-08 14:03:08 | INFO |   Encoded 33/1280
2026-05-08 14:03:08 | INFO |   Encoded 34/1280
2026-05-08 14:03:08 | INFO |   Encoded 35/1280
2026-05-08 14:03:08 | INFO |   Encoded 36/1280
2026-05-08 14:03:08 | INFO |   Encoded 37/1280
2026-05-08 14:03:08 | INFO |   Encoded 38/1280
2026-05-08 14:03:08 | INFO |   Encoded 39/1280
2026-05-08 14:03:08 | INFO |   Encoded 40/1280
2026-05-08 14:03:08 | INFO |   Encoded 41/1280
2026-05-08 14:03:08 | INFO |   Encoded 42/1280
2026-05-08 14:03:08 | INFO |   Encoded 43/1280
2026-05-08 14:03:08 | INFO |   Encoded 44/1280
2026-05-08 14:03:08 | INFO |   Encoded 45/1280
2026-05-08 14:03:08 | INFO |   Encoded 46/1280
2026-05-08 14:03:08 | INFO |   Encoded 47/1280
2026-05-08 14:03:08 | INFO |   Encoded 48/1280
2026-05-08 14:03:08 | INFO |   Encoded 49/1280
2026-05-08 14:03:08 | INFO |   Encoded 50/1280
2026-05-08 14:03:08 | INFO |   Encoded 51/1280
2026-05-08 14:03:08 | INFO |   Encoded 52/1280
2026-05-08 14:03:08 | INFO |   Encoded 53/1280
2026-05-08 14:03:08 | INFO |   Encoded 54/1280
2026-05-08 14:03:08 | INFO |   Encoded 55/1280
2026-05-08 14:03:08 | INFO |   Encoded 56/1280
2026-05-08 14:03:08 | INFO |   Encoded 57/1280
2026-05-08 14:03:08 | INFO |   Encoded 58/1280
2026-05-08 14:03:08 | INFO |   Encoded 59/1280
2026-05-08 14:03:08 | INFO |   Encoded 60/1280
2026-05-08 14:03:08 | INFO |   Encoded 61/1280
2026-05-08 14:03:08 | INFO |   Encoded 62/1280
2026-05-08 14:03:08 | INFO |   Encoded 63/1280
2026-05-08 14:03:08 | INFO |   Encoded 64/1280
2026-05-08 14:03:08 | INFO |   Encoded 65/1280
2026-05-08 14:03:08 | INFO |   Encoded 66/1280
2026-05-08 14:03:08 | INFO |   Encoded 67/1280
2026-05-08 14:03:08 | INFO |   Encoded 68/1280
2026-05-08 14:03:08 | INFO |   Encoded 69/1280
2026-05-08 14:03:08 | INFO |   Encoded 70/1280
2026-05-08 14:03:08 | INFO |   Encoded 71/1280
2026-05-08 14:03:08 | INFO |   Encoded 72/1280
2026-05-08 14:03:08 | INFO |   Encoded 73/1280
2026-05-08 14:03:08 | INFO |   Encoded 74/1280
2026-05-08 14:03:08 | INFO |   Encoded 75/1280
2026-05-08 14:03:08 | INFO |   Encoded 76/1280
2026-05-08 14:03:08 | INFO |   Encoded 77/1280
2026-05-08 14:03:08 | INFO |   Encoded 78/1280
2026-05-08 14:03:08 | INFO |   Encoded 79/1280
2026-05-08 14:03:08 | INFO |   Encoded 80/1280
2026-05-08 14:03:08 | INFO |   Encoded 81/1280
2026-05-08 14:03:08 | INFO |   Encoded 82/1280
2026-05-08 14:03:08 | INFO |   Encoded 83/1280
2026-05-08 14:03:08 | INFO |   Encoded 84/1280
2026-05-08 14:03:08 | INFO |   Encoded 85/1280
2026-05-08 14:03:08 | INFO |   Encoded 86/1280
2026-05-08 14:03:08 | INFO |   Encoded 87/1280
2026-05-08 14:03:08 | INFO |   Encoded 88/1280
2026-05-08 14:03:08 | INFO |   Encoded 89/1280
2026-05-08 14:03:08 | INFO |   Encoded 90/1280
2026-05-08 14:03:08 | INFO |   Encoded 91/1280
2026-05-08 14:03:08 | INFO |   Encoded 92/1280
2026-05-08 14:03:08 | INFO |   Encoded 93/1280
2026-05-08 14:03:08 | INFO |   Encoded 94/1280
2026-05-08 14:03:08 | INFO |   Encoded 95/1280
2026-05-08 14:03:08 | INFO |   Encoded 96/1280
2026-05-08 14:03:08 | INFO |   Encoded 97/1280
2026-05-08 14:03:08 | INFO |   Encoded 98/1280
2026-05-08 14:03:08 | INFO |   Encoded 99/1280
2026-05-08 14:03:08 | INFO |   Encoded 100/1280
2026-05-08 14:03:08 | INFO |   Encoded 101/1280
2026-05-08 14:03:08 | INFO |   Encoded 102/1280
2026-05-08 14:03:08 | INFO |   Encoded 103/1280
2026-05-08 14:03:08 | INFO |   Encoded 104/1280
2026-05-08 14:03:08 | INFO |   Encoded 105/1280
2026-05-08 14:03:08 | INFO |   Encoded 106/1280
2026-05-08 14:03:08 | INFO |   Encoded 107/1280
2026-05-08 14:03:08 | INFO |   Encoded 108/1280
2026-05-08 14:03:08 | INFO |   Encoded 109/1280
2026-05-08 14:03:08 | INFO |   Encoded 110/1280
2026-05-08 14:03:08 | INFO |   Encoded 111/1280
2026-05-08 14:03:08 | INFO |   Encoded 112/1280
2026-05-08 14:03:08 | INFO |   Encoded 113/1280
2026-05-08 14:03:08 | INFO |   Encoded 114/1280
2026-05-08 14:03:08 | INFO |   Encoded 115/1280
2026-05-08 14:03:08 | INFO |   Encoded 116/1280
2026-05-08 14:03:08 | INFO |   Encoded 117/1280
2026-05-08 14:03:08 | INFO |   Encoded 118/1280
2026-05-08 14:03:08 | INFO |   Encoded 119/1280
2026-05-08 14:03:08 | INFO |   Encoded 120/1280
2026-05-08 14:03:08 | INFO |   Encoded 121/1280
2026-05-08 14:03:08 | INFO |   Encoded 122/1280
2026-05-08 14:03:08 | INFO |   Encoded 123/1280
2026-05-08 14:03:08 | INFO |   Encoded 124/1280
2026-05-08 14:03:08 | INFO |   Encoded 125/1280
2026-05-08 14:03:08 | INFO |   Encoded 126/1280
2026-05-08 14:03:08 | INFO |   Encoded 127/1280
2026-05-08 14:03:08 | INFO |   Encoded 128/1280
2026-05-08 14:03:08 | INFO |   Encoded 129/1280
2026-05-08 14:03:08 | INFO |   Encoded 130/1280
2026-05-08 14:03:08 | INFO |   Encoded 131/1280
2026-05-08 14:03:08 | INFO |   Encoded 132/1280
2026-05-08 14:03:08 | INFO |   Encoded 133/1280
2026-05-08 14:03:08 | INFO |   Encoded 134/1280
2026-05-08 14:03:08 | INFO |   Encoded 135/1280
2026-05-08 14:03:08 | INFO |   Encoded 136/1280
2026-05-08 14:03:08 | INFO |   Encoded 137/1280
2026-05-08 14:03:08 | INFO |   Encoded 138/1280
2026-05-08 14:03:08 | INFO |   Encoded 139/1280
2026-05-08 14:03:08 | INFO |   Encoded 140/1280
2026-05-08 14:03:08 | INFO |   Encoded 141/1280
2026-05-08 14:03:08 | INFO |   Encoded 142/1280
2026-05-08 14:03:08 | INFO |   Encoded 143/1280
2026-05-08 14:03:08 | INFO |   Encoded 144/1280
2026-05-08 14:03:08 | INFO |   Encoded 145/1280
2026-05-08 14:03:08 | INFO |   Encoded 146/1280
2026-05-08 14:03:08 | INFO |   Encoded 147/1280
2026-05-08 14:03:08 | INFO |   Encoded 148/1280
2026-05-08 14:03:08 | INFO |   Encoded 149/1280
2026-05-08 14:03:08 | INFO |   Encoded 150/1280
2026-05-08 14:03:08 | INFO |   Encoded 151/1280
2026-05-08 14:03:08 | INFO |   Encoded 152/1280
2026-05-08 14:03:08 | INFO |   Encoded 153/1280
2026-05-08 14:03:08 | INFO |   Encoded 154/1280
2026-05-08 14:03:08 | INFO |   Encoded 155/1280
2026-05-08 14:03:08 | INFO |   Encoded 156/1280
2026-05-08 14:03:08 | INFO |   Encoded 157/1280
2026-05-08 14:03:08 | INFO |   Encoded 158/1280
2026-05-08 14:03:08 | INFO |   Encoded 159/1280
2026-05-08 14:03:08 | INFO |   Encoded 160/1280
2026-05-08 14:03:08 | INFO |   Encoded 161/1280
2026-05-08 14:03:08 | INFO |   Encoded 162/1280
2026-05-08 14:03:08 | INFO |   Encoded 163/1280
2026-05-08 14:03:08 | INFO |   Encoded 164/1280
2026-05-08 14:03:08 | INFO |   Encoded 165/1280
2026-05-08 14:03:08 | INFO |   Encoded 166/1280
2026-05-08 14:03:08 | INFO |   Encoded 167/1280
2026-05-08 14:03:08 | INFO |   Encoded 168/1280
2026-05-08 14:03:08 | INFO |   Encoded 169/1280
2026-05-08 14:03:08 | INFO |   Encoded 170/1280
2026-05-08 14:03:08 | INFO |   Encoded 171/1280
2026-05-08 14:03:08 | INFO |   Encoded 172/1280
2026-05-08 14:03:08 | INFO |   Encoded 173/1280
2026-05-08 14:03:08 | INFO |   Encoded 174/1280
2026-05-08 14:03:08 | INFO |   Encoded 175/1280
2026-05-08 14:03:08 | INFO |   Encoded 176/1280
2026-05-08 14:03:08 | INFO |   Encoded 177/1280
2026-05-08 14:03:08 | INFO |   Encoded 178/1280
2026-05-08 14:03:08 | INFO |   Encoded 179/1280
2026-05-08 14:03:08 | INFO |   Encoded 180/1280
2026-05-08 14:03:08 | INFO |   Encoded 181/1280
2026-05-08 14:03:08 | INFO |   Encoded 182/1280
2026-05-08 14:03:08 | INFO |   Encoded 183/1280
2026-05-08 14:03:08 | INFO |   Encoded 184/1280
2026-05-08 14:03:08 | INFO |   Encoded 185/1280
2026-05-08 14:03:08 | INFO |   Encoded 186/1280
2026-05-08 14:03:08 | INFO |   Encoded 187/1280
2026-05-08 14:03:08 | INFO |   Encoded 188/1280
2026-05-08 14:03:08 | INFO |   Encoded 189/1280
2026-05-08 14:03:08 | INFO |   Encoded 190/1280
2026-05-08 14:03:08 | INFO |   Encoded 191/1280
2026-05-08 14:03:08 | INFO |   Encoded 192/1280
2026-05-08 14:03:08 | INFO |   Encoded 193/1280
2026-05-08 14:03:08 | INFO |   Encoded 194/1280
2026-05-08 14:03:08 | INFO |   Encoded 195/1280
2026-05-08 14:03:08 | INFO |   Encoded 196/1280
2026-05-08 14:03:08 | INFO |   Encoded 197/1280
2026-05-08 14:03:08 | INFO |   Encoded 198/1280
2026-05-08 14:03:08 | INFO |   Encoded 199/1280
2026-05-08 14:03:08 | INFO |   Encoded 200/1280
2026-05-08 14:03:08 | INFO |   Encoded 201/1280
2026-05-08 14:03:08 | INFO |   Encoded 202/1280
2026-05-08 14:03:08 | INFO |   Encoded 203/1280
2026-05-08 14:03:08 | INFO |   Encoded 204/1280
2026-05-08 14:03:08 | INFO |   Encoded 205/1280
2026-05-08 14:03:08 | INFO |   Encoded 206/1280
2026-05-08 14:03:08 | INFO |   Encoded 207/1280
2026-05-08 14:03:08 | INFO |   Encoded 208/1280
2026-05-08 14:03:08 | INFO |   Encoded 209/1280
2026-05-08 14:03:08 | INFO |   Encoded 210/1280
2026-05-08 14:03:08 | INFO |   Encoded 211/1280
2026-05-08 14:03:08 | INFO |   Encoded 212/1280
2026-05-08 14:03:08 | INFO |   Encoded 213/1280
2026-05-08 14:03:08 | INFO |   Encoded 214/1280
2026-05-08 14:03:08 | INFO |   Encoded 215/1280
2026-05-08 14:03:08 | INFO |   Encoded 216/1280
2026-05-08 14:03:08 | INFO |   Encoded 217/1280
2026-05-08 14:03:08 | INFO |   Encoded 218/1280
2026-05-08 14:03:08 | INFO |   Encoded 219/1280
2026-05-08 14:03:08 | INFO |   Encoded 220/1280
2026-05-08 14:03:08 | INFO |   Encoded 221/1280
2026-05-08 14:03:08 | INFO |   Encoded 222/1280
2026-05-08 14:03:08 | INFO |   Encoded 223/1280
2026-05-08 14:03:08 | INFO |   Encoded 224/1280
2026-05-08 14:03:08 | INFO |   Encoded 225/1280
2026-05-08 14:03:08 | INFO |   Encoded 226/1280
2026-05-08 14:03:08 | INFO |   Encoded 227/1280
2026-05-08 14:03:08 | INFO |   Encoded 228/1280
2026-05-08 14:03:08 | INFO |   Encoded 229/1280
2026-05-08 14:03:08 | INFO |   Encoded 230/1280
2026-05-08 14:03:08 | INFO |   Encoded 231/1280
2026-05-08 14:03:08 | INFO |   Encoded 232/1280
2026-05-08 14:03:08 | INFO |   Encoded 233/1280
2026-05-08 14:03:08 | INFO |   Encoded 234/1280
2026-05-08 14:03:08 | INFO |   Encoded 235/1280
2026-05-08 14:03:08 | INFO |   Encoded 236/1280
2026-05-08 14:03:08 | INFO |   Encoded 237/1280
2026-05-08 14:03:08 | INFO |   Encoded 238/1280
2026-05-08 14:03:08 | INFO |   Encoded 239/1280
2026-05-08 14:03:08 | INFO |   Encoded 240/1280
2026-05-08 14:03:08 | INFO |   Encoded 241/1280
2026-05-08 14:03:08 | INFO |   Encoded 242/1280
2026-05-08 14:03:08 | INFO |   Encoded 243/1280
2026-05-08 14:03:08 | INFO |   Encoded 244/1280
2026-05-08 14:03:08 | INFO |   Encoded 245/1280
2026-05-08 14:03:08 | INFO |   Encoded 246/1280
2026-05-08 14:03:08 | INFO |   Encoded 247/1280
2026-05-08 14:03:08 | INFO |   Encoded 248/1280
2026-05-08 14:03:08 | INFO |   Encoded 249/1280
2026-05-08 14:03:08 | INFO |   Encoded 250/1280
2026-05-08 14:03:08 | INFO |   Encoded 251/1280
2026-05-08 14:03:08 | INFO |   Encoded 252/1280
2026-05-08 14:03:08 | INFO |   Encoded 253/1280
2026-05-08 14:03:08 | INFO |   Encoded 254/1280
2026-05-08 14:03:08 | INFO |   Encoded 255/1280
2026-05-08 14:03:08 | INFO |   Encoded 256/1280
2026-05-08 14:03:08 | INFO |   Encoded 257/1280
2026-05-08 14:03:08 | INFO |   Encoded 258/1280
2026-05-08 14:03:08 | INFO |   Encoded 259/1280
2026-05-08 14:03:08 | INFO |   Encoded 260/1280
2026-05-08 14:03:08 | INFO |   Encoded 261/1280
2026-05-08 14:03:08 | INFO |   Encoded 262/1280
2026-05-08 14:03:08 | INFO |   Encoded 263/1280
2026-05-08 14:03:08 | INFO |   Encoded 264/1280
2026-05-08 14:03:08 | INFO |   Encoded 265/1280
2026-05-08 14:03:08 | INFO |   Encoded 266/1280
2026-05-08 14:03:08 | INFO |   Encoded 267/1280
2026-05-08 14:03:08 | INFO |   Encoded 268/1280
2026-05-08 14:03:08 | INFO |   Encoded 269/1280
2026-05-08 14:03:08 | INFO |   Encoded 270/1280
2026-05-08 14:03:08 | INFO |   Encoded 271/1280
2026-05-08 14:03:08 | INFO |   Encoded 272/1280
2026-05-08 14:03:08 | INFO |   Encoded 273/1280
2026-05-08 14:03:08 | INFO |   Encoded 274/1280
2026-05-08 14:03:08 | INFO |   Encoded 275/1280
2026-05-08 14:03:08 | INFO |   Encoded 276/1280
2026-05-08 14:03:08 | INFO |   Encoded 277/1280
2026-05-08 14:03:08 | INFO |   Encoded 278/1280
2026-05-08 14:03:08 | INFO |   Encoded 279/1280
2026-05-08 14:03:08 | INFO |   Encoded 280/1280
2026-05-08 14:03:08 | INFO |   Encoded 281/1280
2026-05-08 14:03:08 | INFO |   Encoded 282/1280
2026-05-08 14:03:08 | INFO |   Encoded 283/1280
2026-05-08 14:03:08 | INFO |   Encoded 284/1280
2026-05-08 14:03:08 | INFO |   Encoded 285/1280
2026-05-08 14:03:08 | INFO |   Encoded 286/1280
2026-05-08 14:03:08 | INFO |   Encoded 287/1280
2026-05-08 14:03:08 | INFO |   Encoded 288/1280
2026-05-08 14:03:08 | INFO |   Encoded 289/1280
2026-05-08 14:03:08 | INFO |   Encoded 290/1280
2026-05-08 14:03:08 | INFO |   Encoded 291/1280
2026-05-08 14:03:08 | INFO |   Encoded 292/1280
2026-05-08 14:03:08 | INFO |   Encoded 293/1280
2026-05-08 14:03:08 | INFO |   Encoded 294/1280
2026-05-08 14:03:08 | INFO |   Encoded 295/1280
2026-05-08 14:03:08 | INFO |   Encoded 296/1280
2026-05-08 14:03:08 | INFO |   Encoded 297/1280
2026-05-08 14:03:08 | INFO |   Encoded 298/1280
2026-05-08 14:03:08 | INFO |   Encoded 299/1280
2026-05-08 14:03:08 | INFO |   Encoded 300/1280
2026-05-08 14:03:08 | INFO |   Encoded 301/1280
2026-05-08 14:03:08 | INFO |   Encoded 302/1280
2026-05-08 14:03:08 | INFO |   Encoded 303/1280
2026-05-08 14:03:08 | INFO |   Encoded 304/1280
2026-05-08 14:03:08 | INFO |   Encoded 305/1280
2026-05-08 14:03:08 | INFO |   Encoded 306/1280
2026-05-08 14:03:08 | INFO |   Encoded 307/1280
2026-05-08 14:03:08 | INFO |   Encoded 308/1280
2026-05-08 14:03:08 | INFO |   Encoded 309/1280
2026-05-08 14:03:08 | INFO |   Encoded 310/1280
2026-05-08 14:03:08 | INFO |   Encoded 311/1280
2026-05-08 14:03:08 | INFO |   Encoded 312/1280
2026-05-08 14:03:08 | INFO |   Encoded 313/1280
2026-05-08 14:03:08 | INFO |   Encoded 314/1280
2026-05-08 14:03:08 | INFO |   Encoded 315/1280
2026-05-08 14:03:08 | INFO |   Encoded 316/1280
2026-05-08 14:03:08 | INFO |   Encoded 317/1280
2026-05-08 14:03:08 | INFO |   Encoded 318/1280
2026-05-08 14:03:08 | INFO |   Encoded 319/1280
2026-05-08 14:03:08 | INFO |   Encoded 320/1280
2026-05-08 14:03:08 | INFO |   Encoded 321/1280
2026-05-08 14:03:08 | INFO |   Encoded 322/1280
2026-05-08 14:03:08 | INFO |   Encoded 323/1280
2026-05-08 14:03:08 | INFO |   Encoded 324/1280
2026-05-08 14:03:08 | INFO |   Encoded 325/1280
2026-05-08 14:03:08 | INFO |   Encoded 326/1280
2026-05-08 14:03:08 | INFO |   Encoded 327/1280
2026-05-08 14:03:08 | INFO |   Encoded 328/1280
2026-05-08 14:03:08 | INFO |   Encoded 329/1280
2026-05-08 14:03:08 | INFO |   Encoded 330/1280
2026-05-08 14:03:08 | INFO |   Encoded 331/1280
2026-05-08 14:03:08 | INFO |   Encoded 332/1280
2026-05-08 14:03:08 | INFO |   Encoded 333/1280
2026-05-08 14:03:08 | INFO |   Encoded 334/1280
2026-05-08 14:03:08 | INFO |   Encoded 335/1280
2026-05-08 14:03:08 | INFO |   Encoded 336/1280
2026-05-08 14:03:08 | INFO |   Encoded 337/1280
2026-05-08 14:03:08 | INFO |   Encoded 338/1280
2026-05-08 14:03:08 | INFO |   Encoded 339/1280
2026-05-08 14:03:08 | INFO |   Encoded 340/1280
2026-05-08 14:03:08 | INFO |   Encoded 341/1280
2026-05-08 14:03:08 | INFO |   Encoded 342/1280
2026-05-08 14:03:08 | INFO |   Encoded 343/1280
2026-05-08 14:03:08 | INFO |   Encoded 344/1280
2026-05-08 14:03:08 | INFO |   Encoded 345/1280
2026-05-08 14:03:08 | INFO |   Encoded 346/1280
2026-05-08 14:03:08 | INFO |   Encoded 347/1280
2026-05-08 14:03:08 | INFO |   Encoded 348/1280
2026-05-08 14:03:08 | INFO |   Encoded 349/1280
2026-05-08 14:03:08 | INFO |   Encoded 350/1280
2026-05-08 14:03:08 | INFO |   Encoded 351/1280
2026-05-08 14:03:08 | INFO |   Encoded 352/1280
2026-05-08 14:03:08 | INFO |   Encoded 353/1280
2026-05-08 14:03:08 | INFO |   Encoded 354/1280
2026-05-08 14:03:08 | INFO |   Encoded 355/1280
2026-05-08 14:03:08 | INFO |   Encoded 356/1280
2026-05-08 14:03:08 | INFO |   Encoded 357/1280
2026-05-08 14:03:08 | INFO |   Encoded 358/1280
2026-05-08 14:03:08 | INFO |   Encoded 359/1280
2026-05-08 14:03:08 | INFO |   Encoded 360/1280
2026-05-08 14:03:08 | INFO |   Encoded 361/1280
2026-05-08 14:03:08 | INFO |   Encoded 362/1280
2026-05-08 14:03:08 | INFO |   Encoded 363/1280
2026-05-08 14:03:08 | INFO |   Encoded 364/1280
2026-05-08 14:03:08 | INFO |   Encoded 365/1280
2026-05-08 14:03:08 | INFO |   Encoded 366/1280
2026-05-08 14:03:08 | INFO |   Encoded 367/1280
2026-05-08 14:03:08 | INFO |   Encoded 368/1280
2026-05-08 14:03:08 | INFO |   Encoded 369/1280
2026-05-08 14:03:08 | INFO |   Encoded 370/1280
2026-05-08 14:03:08 | INFO |   Encoded 371/1280
2026-05-08 14:03:08 | INFO |   Encoded 372/1280
2026-05-08 14:03:08 | INFO |   Encoded 373/1280
2026-05-08 14:03:08 | INFO |   Encoded 374/1280
2026-05-08 14:03:08 | INFO |   Encoded 375/1280
2026-05-08 14:03:08 | INFO |   Encoded 376/1280
2026-05-08 14:03:08 | INFO |   Encoded 377/1280
2026-05-08 14:03:08 | INFO |   Encoded 378/1280
2026-05-08 14:03:08 | INFO |   Encoded 379/1280
2026-05-08 14:03:08 | INFO |   Encoded 380/1280
2026-05-08 14:03:08 | INFO |   Encoded 381/1280
2026-05-08 14:03:08 | INFO |   Encoded 382/1280
2026-05-08 14:03:08 | INFO |   Encoded 383/1280
2026-05-08 14:03:08 | INFO |   Encoded 384/1280
2026-05-08 14:03:08 | INFO |   Encoded 385/1280
2026-05-08 14:03:08 | INFO |   Encoded 386/1280
2026-05-08 14:03:08 | INFO |   Encoded 387/1280
2026-05-08 14:03:08 | INFO |   Encoded 388/1280
2026-05-08 14:03:08 | INFO |   Encoded 389/1280
2026-05-08 14:03:08 | INFO |   Encoded 390/1280
2026-05-08 14:03:08 | INFO |   Encoded 391/1280
2026-05-08 14:03:08 | INFO |   Encoded 392/1280
2026-05-08 14:03:08 | INFO |   Encoded 393/1280
2026-05-08 14:03:08 | INFO |   Encoded 394/1280
2026-05-08 14:03:08 | INFO |   Encoded 395/1280
2026-05-08 14:03:08 | INFO |   Encoded 396/1280
2026-05-08 14:03:08 | INFO |   Encoded 397/1280
2026-05-08 14:03:08 | INFO |   Encoded 398/1280
2026-05-08 14:03:08 | INFO |   Encoded 399/1280
2026-05-08 14:03:08 | INFO |   Encoded 400/1280
2026-05-08 14:03:08 | INFO |   Encoded 401/1280
2026-05-08 14:03:08 | INFO |   Encoded 402/1280
2026-05-08 14:03:08 | INFO |   Encoded 403/1280
2026-05-08 14:03:08 | INFO |   Encoded 404/1280
2026-05-08 14:03:08 | INFO |   Encoded 405/1280
2026-05-08 14:03:08 | INFO |   Encoded 406/1280
2026-05-08 14:03:08 | INFO |   Encoded 407/1280
2026-05-08 14:03:08 | INFO |   Encoded 408/1280
2026-05-08 14:03:08 | INFO |   Encoded 409/1280
2026-05-08 14:03:08 | INFO |   Encoded 410/1280
2026-05-08 14:03:08 | INFO |   Encoded 411/1280
2026-05-08 14:03:08 | INFO |   Encoded 412/1280
2026-05-08 14:03:08 | INFO |   Encoded 413/1280
2026-05-08 14:03:08 | INFO |   Encoded 414/1280
2026-05-08 14:03:08 | INFO |   Encoded 415/1280
2026-05-08 14:03:08 | INFO |   Encoded 416/1280
2026-05-08 14:03:08 | INFO |   Encoded 417/1280
2026-05-08 14:03:08 | INFO |   Encoded 418/1280
2026-05-08 14:03:08 | INFO |   Encoded 419/1280
2026-05-08 14:03:08 | INFO |   Encoded 420/1280
2026-05-08 14:03:08 | INFO |   Encoded 421/1280
2026-05-08 14:03:08 | INFO |   Encoded 422/1280
2026-05-08 14:03:08 | INFO |   Encoded 423/1280
2026-05-08 14:03:08 | INFO |   Encoded 424/1280
2026-05-08 14:03:08 | INFO |   Encoded 425/1280
2026-05-08 14:03:08 | INFO |   Encoded 426/1280
2026-05-08 14:03:08 | INFO |   Encoded 427/1280
2026-05-08 14:03:08 | INFO |   Encoded 428/1280
2026-05-08 14:03:08 | INFO |   Encoded 429/1280
2026-05-08 14:03:08 | INFO |   Encoded 430/1280
2026-05-08 14:03:08 | INFO |   Encoded 431/1280
2026-05-08 14:03:08 | INFO |   Encoded 432/1280
2026-05-08 14:03:08 | INFO |   Encoded 433/1280
2026-05-08 14:03:08 | INFO |   Encoded 434/1280
2026-05-08 14:03:08 | INFO |   Encoded 435/1280
2026-05-08 14:03:25 | INFO |   Encoded 436/1280
2026-05-08 14:03:25 | INFO |   Encoded 437/1280
2026-05-08 14:03:25 | INFO |   Encoded 438/1280
2026-05-08 14:03:25 | INFO |   Encoded 439/1280
2026-05-08 14:03:25 | INFO |   Encoded 440/1280
2026-05-08 14:03:25 | INFO |   Encoded 441/1280
2026-05-08 14:03:25 | INFO |   Encoded 442/1280
2026-05-08 14:03:25 | INFO |   Encoded 443/1280
2026-05-08 14:03:25 | INFO |   Encoded 444/1280
2026-05-08 14:03:25 | INFO |   Encoded 445/1280
2026-05-08 14:03:25 | INFO |   Encoded 446/1280
2026-05-08 14:03:25 | INFO |   Encoded 447/1280
2026-05-08 14:03:25 | INFO |   Encoded 448/1280
2026-05-08 14:03:25 | INFO |   Encoded 449/1280
2026-05-08 14:03:25 | INFO |   Encoded 450/1280
2026-05-08 14:03:25 | INFO |   Encoded 451/1280
2026-05-08 14:03:25 | INFO |   Encoded 452/1280
2026-05-08 14:03:25 | INFO |   Encoded 453/1280
2026-05-08 14:03:25 | INFO |   Encoded 454/1280
2026-05-08 14:03:25 | INFO |   Encoded 455/1280
2026-05-08 14:03:25 | INFO |   Encoded 456/1280
2026-05-08 14:03:25 | INFO |   Encoded 457/1280
2026-05-08 14:03:25 | INFO |   Encoded 458/1280
2026-05-08 14:03:25 | INFO |   Encoded 459/1280
2026-05-08 14:03:25 | INFO |   Encoded 460/1280
2026-05-08 14:03:25 | INFO |   Encoded 461/1280
2026-05-08 14:03:25 | INFO |   Encoded 462/1280
2026-05-08 14:03:25 | INFO |   Encoded 463/1280
2026-05-08 14:03:25 | INFO |   Encoded 464/1280
2026-05-08 14:03:25 | INFO |   Encoded 465/1280
2026-05-08 14:03:25 | INFO |   Encoded 466/1280
2026-05-08 14:03:25 | INFO |   Encoded 467/1280
2026-05-08 14:03:25 | INFO |   Encoded 468/1280
2026-05-08 14:03:25 | INFO |   Encoded 469/1280
2026-05-08 14:03:25 | INFO |   Encoded 470/1280
2026-05-08 14:03:25 | INFO |   Encoded 471/1280
2026-05-08 14:03:25 | INFO |   Encoded 472/1280
2026-05-08 14:03:25 | INFO |   Encoded 473/1280
2026-05-08 14:03:25 | INFO |   Encoded 474/1280
2026-05-08 14:03:25 | INFO |   Encoded 475/1280
2026-05-08 14:03:25 | INFO |   Encoded 476/1280
2026-05-08 14:03:25 | INFO |   Encoded 477/1280
2026-05-08 14:03:25 | INFO |   Encoded 478/1280
2026-05-08 14:03:25 | INFO |   Encoded 479/1280
2026-05-08 14:03:25 | INFO |   Encoded 480/1280
2026-05-08 14:03:25 | INFO |   Encoded 481/1280
2026-05-08 14:03:25 | INFO |   Encoded 482/1280
2026-05-08 14:03:25 | INFO |   Encoded 483/1280
2026-05-08 14:03:25 | INFO |   Encoded 484/1280
2026-05-08 14:03:25 | INFO |   Encoded 485/1280
2026-05-08 14:03:25 | INFO |   Encoded 486/1280
2026-05-08 14:03:25 | INFO |   Encoded 487/1280
2026-05-08 14:03:25 | INFO |   Encoded 488/1280
2026-05-08 14:03:25 | INFO |   Encoded 489/1280
2026-05-08 14:03:25 | INFO |   Encoded 490/1280
2026-05-08 14:03:25 | INFO |   Encoded 491/1280
2026-05-08 14:03:25 | INFO |   Encoded 492/1280
2026-05-08 14:03:25 | INFO |   Encoded 493/1280
2026-05-08 14:03:25 | INFO |   Encoded 494/1280
2026-05-08 14:03:25 | INFO |   Encoded 495/1280
2026-05-08 14:03:25 | INFO |   Encoded 496/1280
2026-05-08 14:03:25 | INFO |   Encoded 497/1280
2026-05-08 14:03:25 | INFO |   Encoded 498/1280
2026-05-08 14:03:25 | INFO |   Encoded 499/1280
2026-05-08 14:03:25 | INFO |   Encoded 500/1280
2026-05-08 14:03:25 | INFO |   Encoded 501/1280
2026-05-08 14:03:25 | INFO |   Encoded 502/1280
2026-05-08 14:03:25 | INFO |   Encoded 503/1280
2026-05-08 14:03:25 | INFO |   Encoded 504/1280
2026-05-08 14:03:25 | INFO |   Encoded 505/1280
2026-05-08 14:03:25 | INFO |   Encoded 506/1280
2026-05-08 14:03:25 | INFO |   Encoded 507/1280
2026-05-08 14:03:25 | INFO |   Encoded 508/1280
2026-05-08 14:03:25 | INFO |   Encoded 509/1280
2026-05-08 14:03:25 | INFO |   Encoded 510/1280
2026-05-08 14:03:25 | INFO |   Encoded 511/1280
2026-05-08 14:03:25 | INFO |   Encoded 512/1280
2026-05-08 14:03:25 | INFO |   Encoded 513/1280
2026-05-08 14:03:25 | INFO |   Encoded 514/1280
2026-05-08 14:03:25 | INFO |   Encoded 515/1280
2026-05-08 14:03:25 | INFO |   Encoded 516/1280
2026-05-08 14:03:25 | INFO |   Encoded 517/1280
2026-05-08 14:03:25 | INFO |   Encoded 518/1280
2026-05-08 14:03:25 | INFO |   Encoded 519/1280
2026-05-08 14:03:25 | INFO |   Encoded 520/1280
2026-05-08 14:03:25 | INFO |   Encoded 521/1280
2026-05-08 14:03:25 | INFO |   Encoded 522/1280
2026-05-08 14:03:25 | INFO |   Encoded 523/1280
2026-05-08 14:03:25 | INFO |   Encoded 524/1280
2026-05-08 14:03:25 | INFO |   Encoded 525/1280
2026-05-08 14:03:25 | INFO |   Encoded 526/1280
2026-05-08 14:03:25 | INFO |   Encoded 527/1280
2026-05-08 14:03:25 | INFO |   Encoded 528/1280
2026-05-08 14:03:25 | INFO |   Encoded 529/1280
2026-05-08 14:03:25 | INFO |   Encoded 530/1280
2026-05-08 14:03:25 | INFO |   Encoded 531/1280
2026-05-08 14:03:25 | INFO |   Encoded 532/1280
2026-05-08 14:03:25 | INFO |   Encoded 533/1280
2026-05-08 14:03:25 | INFO |   Encoded 534/1280
2026-05-08 14:03:25 | INFO |   Encoded 535/1280
2026-05-08 14:03:25 | INFO |   Encoded 536/1280
2026-05-08 14:03:25 | INFO |   Encoded 537/1280
2026-05-08 14:03:25 | INFO |   Encoded 538/1280
2026-05-08 14:03:25 | INFO |   Encoded 539/1280
2026-05-08 14:03:25 | INFO |   Encoded 540/1280
2026-05-08 14:03:25 | INFO |   Encoded 541/1280
2026-05-08 14:03:25 | INFO |   Encoded 542/1280
2026-05-08 14:03:25 | INFO |   Encoded 543/1280
2026-05-08 14:03:25 | INFO |   Encoded 544/1280
2026-05-08 14:03:25 | INFO |   Encoded 545/1280
2026-05-08 14:03:25 | INFO |   Encoded 546/1280
2026-05-08 14:03:25 | INFO |   Encoded 547/1280
2026-05-08 14:03:25 | INFO |   Encoded 548/1280
2026-05-08 14:03:25 | INFO |   Encoded 549/1280
2026-05-08 14:03:25 | INFO |   Encoded 550/1280
2026-05-08 14:03:25 | INFO |   Encoded 551/1280
2026-05-08 14:03:25 | INFO |   Encoded 552/1280
2026-05-08 14:03:25 | INFO |   Encoded 553/1280
2026-05-08 14:03:25 | INFO |   Encoded 554/1280
2026-05-08 14:03:25 | INFO |   Encoded 555/1280
2026-05-08 14:03:25 | INFO |   Encoded 556/1280
2026-05-08 14:03:25 | INFO |   Encoded 557/1280
2026-05-08 14:03:25 | INFO |   Encoded 558/1280
2026-05-08 14:03:25 | INFO |   Encoded 559/1280
2026-05-08 14:03:25 | INFO |   Encoded 560/1280
2026-05-08 14:03:25 | INFO |   Encoded 561/1280
2026-05-08 14:03:25 | INFO |   Encoded 562/1280
2026-05-08 14:03:25 | INFO |   Encoded 563/1280
2026-05-08 14:03:25 | INFO |   Encoded 564/1280
2026-05-08 14:03:25 | INFO |   Encoded 565/1280
2026-05-08 14:03:25 | INFO |   Encoded 566/1280
2026-05-08 14:03:25 | INFO |   Encoded 567/1280
2026-05-08 14:03:25 | INFO |   Encoded 568/1280
2026-05-08 14:03:25 | INFO |   Encoded 569/1280
2026-05-08 14:03:25 | INFO |   Encoded 570/1280
2026-05-08 14:03:25 | INFO |   Encoded 571/1280
2026-05-08 14:03:25 | INFO |   Encoded 572/1280
2026-05-08 14:03:25 | INFO |   Encoded 573/1280
2026-05-08 14:03:25 | INFO |   Encoded 574/1280
2026-05-08 14:03:25 | INFO |   Encoded 575/1280
2026-05-08 14:03:25 | INFO |   Encoded 576/1280
2026-05-08 14:03:25 | INFO |   Encoded 577/1280
2026-05-08 14:03:25 | INFO |   Encoded 578/1280
2026-05-08 14:03:25 | INFO |   Encoded 579/1280
2026-05-08 14:03:25 | INFO |   Encoded 580/1280
2026-05-08 14:03:25 | INFO |   Encoded 581/1280
2026-05-08 14:03:25 | INFO |   Encoded 582/1280
2026-05-08 14:03:25 | INFO |   Encoded 583/1280
2026-05-08 14:03:25 | INFO |   Encoded 584/1280
2026-05-08 14:03:25 | INFO |   Encoded 585/1280
2026-05-08 14:03:25 | INFO |   Encoded 586/1280
2026-05-08 14:03:25 | INFO |   Encoded 587/1280
2026-05-08 14:03:25 | INFO |   Encoded 588/1280
2026-05-08 14:03:25 | INFO |   Encoded 589/1280
2026-05-08 14:03:25 | INFO |   Encoded 590/1280
2026-05-08 14:03:25 | INFO |   Encoded 591/1280
2026-05-08 14:03:25 | INFO |   Encoded 592/1280
2026-05-08 14:03:25 | INFO |   Encoded 593/1280
2026-05-08 14:03:25 | INFO |   Encoded 594/1280
2026-05-08 14:03:25 | INFO |   Encoded 595/1280
2026-05-08 14:03:25 | INFO |   Encoded 596/1280
2026-05-08 14:03:25 | INFO |   Encoded 597/1280
2026-05-08 14:03:25 | INFO |   Encoded 598/1280
2026-05-08 14:03:25 | INFO |   Encoded 599/1280
2026-05-08 14:03:25 | INFO |   Encoded 600/1280
2026-05-08 14:03:25 | INFO |   Encoded 601/1280
2026-05-08 14:03:25 | INFO |   Encoded 602/1280
2026-05-08 14:03:25 | INFO |   Encoded 603/1280
2026-05-08 14:03:25 | INFO |   Encoded 604/1280
2026-05-08 14:03:25 | INFO |   Encoded 605/1280
2026-05-08 14:03:25 | INFO |   Encoded 606/1280
2026-05-08 14:03:25 | INFO |   Encoded 607/1280
2026-05-08 14:03:25 | INFO |   Encoded 608/1280
2026-05-08 14:03:25 | INFO |   Encoded 609/1280
2026-05-08 14:03:25 | INFO |   Encoded 610/1280
2026-05-08 14:03:25 | INFO |   Encoded 611/1280
2026-05-08 14:03:25 | INFO |   Encoded 612/1280
2026-05-08 14:03:25 | INFO |   Encoded 613/1280
2026-05-08 14:03:25 | INFO |   Encoded 614/1280
2026-05-08 14:03:25 | INFO |   Encoded 615/1280
2026-05-08 14:03:25 | INFO |   Encoded 616/1280
2026-05-08 14:03:25 | INFO |   Encoded 617/1280
2026-05-08 14:03:25 | INFO |   Encoded 618/1280
2026-05-08 14:03:25 | INFO |   Encoded 619/1280
2026-05-08 14:03:25 | INFO |   Encoded 620/1280
2026-05-08 14:03:25 | INFO |   Encoded 621/1280
2026-05-08 14:03:25 | INFO |   Encoded 622/1280
2026-05-08 14:03:25 | INFO |   Encoded 623/1280
2026-05-08 14:03:25 | INFO |   Encoded 624/1280
2026-05-08 14:03:25 | INFO |   Encoded 625/1280
2026-05-08 14:03:25 | INFO |   Encoded 626/1280
2026-05-08 14:03:25 | INFO |   Encoded 627/1280
2026-05-08 14:03:25 | INFO |   Encoded 628/1280
2026-05-08 14:03:25 | INFO |   Encoded 629/1280
2026-05-08 14:03:25 | INFO |   Encoded 630/1280
2026-05-08 14:03:25 | INFO |   Encoded 631/1280
2026-05-08 14:03:25 | INFO |   Encoded 632/1280
2026-05-08 14:03:25 | INFO |   Encoded 633/1280
2026-05-08 14:03:25 | INFO |   Encoded 634/1280
2026-05-08 14:03:25 | INFO |   Encoded 635/1280
2026-05-08 14:03:25 | INFO |   Encoded 636/1280
2026-05-08 14:03:25 | INFO |   Encoded 637/1280
2026-05-08 14:03:25 | INFO |   Encoded 638/1280
2026-05-08 14:03:25 | INFO |   Encoded 639/1280
2026-05-08 14:03:25 | INFO |   Encoded 640/1280
2026-05-08 14:03:25 | INFO |   Encoded 641/1280
2026-05-08 14:03:25 | INFO |   Encoded 642/1280
2026-05-08 14:03:25 | INFO |   Encoded 643/1280
2026-05-08 14:03:25 | INFO |   Encoded 644/1280
2026-05-08 14:03:25 | INFO |   Encoded 645/1280
2026-05-08 14:03:25 | INFO |   Encoded 646/1280
2026-05-08 14:03:25 | INFO |   Encoded 647/1280
2026-05-08 14:03:25 | INFO |   Encoded 648/1280
2026-05-08 14:03:25 | INFO |   Encoded 649/1280
2026-05-08 14:03:25 | INFO |   Encoded 650/1280
2026-05-08 14:03:25 | INFO |   Encoded 651/1280
2026-05-08 14:03:25 | INFO |   Encoded 652/1280
2026-05-08 14:03:25 | INFO |   Encoded 653/1280
2026-05-08 14:03:25 | INFO |   Encoded 654/1280
2026-05-08 14:03:25 | INFO |   Encoded 655/1280
2026-05-08 14:03:25 | INFO |   Encoded 656/1280
2026-05-08 14:03:25 | INFO |   Encoded 657/1280
2026-05-08 14:03:25 | INFO |   Encoded 658/1280
2026-05-08 14:03:25 | INFO |   Encoded 659/1280
2026-05-08 14:03:25 | INFO |   Encoded 660/1280
2026-05-08 14:03:25 | INFO |   Encoded 661/1280
2026-05-08 14:03:25 | INFO |   Encoded 662/1280
2026-05-08 14:03:25 | INFO |   Encoded 663/1280
2026-05-08 14:03:25 | INFO |   Encoded 664/1280
2026-05-08 14:03:25 | INFO |   Encoded 665/1280
2026-05-08 14:03:25 | INFO |   Encoded 666/1280
2026-05-08 14:03:25 | INFO |   Encoded 667/1280
2026-05-08 14:03:25 | INFO |   Encoded 668/1280
2026-05-08 14:03:25 | INFO |   Encoded 669/1280
2026-05-08 14:03:25 | INFO |   Encoded 670/1280
2026-05-08 14:03:25 | INFO |   Encoded 671/1280
2026-05-08 14:03:25 | INFO |   Encoded 672/1280
2026-05-08 14:03:25 | INFO |   Encoded 673/1280
2026-05-08 14:03:25 | INFO |   Encoded 674/1280
2026-05-08 14:03:25 | INFO |   Encoded 675/1280
2026-05-08 14:03:25 | INFO |   Encoded 676/1280
2026-05-08 14:03:25 | INFO |   Encoded 677/1280
2026-05-08 14:03:25 | INFO |   Encoded 678/1280
2026-05-08 14:03:25 | INFO |   Encoded 679/1280
2026-05-08 14:03:25 | INFO |   Encoded 680/1280
2026-05-08 14:03:25 | INFO |   Encoded 681/1280
2026-05-08 14:03:25 | INFO |   Encoded 682/1280
2026-05-08 14:03:25 | INFO |   Encoded 683/1280
2026-05-08 14:03:25 | INFO |   Encoded 684/1280
2026-05-08 14:03:25 | INFO |   Encoded 685/1280
2026-05-08 14:03:25 | INFO |   Encoded 686/1280
2026-05-08 14:03:25 | INFO |   Encoded 687/1280
2026-05-08 14:03:25 | INFO |   Encoded 688/1280
2026-05-08 14:03:25 | INFO |   Encoded 689/1280
2026-05-08 14:03:25 | INFO |   Encoded 690/1280
2026-05-08 14:03:25 | INFO |   Encoded 691/1280
2026-05-08 14:03:25 | INFO |   Encoded 692/1280
2026-05-08 14:03:25 | INFO |   Encoded 693/1280
2026-05-08 14:03:25 | INFO |   Encoded 694/1280
2026-05-08 14:03:25 | INFO |   Encoded 695/1280
2026-05-08 14:03:25 | INFO |   Encoded 696/1280
2026-05-08 14:03:25 | INFO |   Encoded 697/1280
2026-05-08 14:03:25 | INFO |   Encoded 698/1280
2026-05-08 14:03:25 | INFO |   Encoded 699/1280
2026-05-08 14:03:25 | INFO |   Encoded 700/1280
2026-05-08 14:03:25 | INFO |   Encoded 701/1280
2026-05-08 14:03:25 | INFO |   Encoded 702/1280
2026-05-08 14:03:25 | INFO |   Encoded 703/1280
2026-05-08 14:03:25 | INFO |   Encoded 704/1280
2026-05-08 14:03:25 | INFO |   Encoded 705/1280
2026-05-08 14:03:25 | INFO |   Encoded 706/1280
2026-05-08 14:03:25 | INFO |   Encoded 707/1280
2026-05-08 14:03:25 | INFO |   Encoded 708/1280
2026-05-08 14:03:25 | INFO |   Encoded 709/1280
2026-05-08 14:03:25 | INFO |   Encoded 710/1280
2026-05-08 14:03:25 | INFO |   Encoded 711/1280
2026-05-08 14:03:25 | INFO |   Encoded 712/1280
2026-05-08 14:03:25 | INFO |   Encoded 713/1280
2026-05-08 14:03:25 | INFO |   Encoded 714/1280
2026-05-08 14:03:25 | INFO |   Encoded 715/1280
2026-05-08 14:03:25 | INFO |   Encoded 716/1280
2026-05-08 14:03:25 | INFO |   Encoded 717/1280
2026-05-08 14:03:25 | INFO |   Encoded 718/1280
2026-05-08 14:03:25 | INFO |   Encoded 719/1280
2026-05-08 14:03:25 | INFO |   Encoded 720/1280
2026-05-08 14:03:25 | INFO |   Encoded 721/1280
2026-05-08 14:03:25 | INFO |   Encoded 722/1280
2026-05-08 14:03:25 | INFO |   Encoded 723/1280
2026-05-08 14:03:25 | INFO |   Encoded 724/1280
2026-05-08 14:03:25 | INFO |   Encoded 725/1280
2026-05-08 14:03:25 | INFO |   Encoded 726/1280
2026-05-08 14:03:25 | INFO |   Encoded 727/1280
2026-05-08 14:03:25 | INFO |   Encoded 728/1280
2026-05-08 14:03:25 | INFO |   Encoded 729/1280
2026-05-08 14:03:25 | INFO |   Encoded 730/1280
2026-05-08 14:03:25 | INFO |   Encoded 731/1280
2026-05-08 14:03:25 | INFO |   Encoded 732/1280
2026-05-08 14:03:25 | INFO |   Encoded 733/1280
2026-05-08 14:03:25 | INFO |   Encoded 734/1280
2026-05-08 14:03:25 | INFO |   Encoded 735/1280
2026-05-08 14:03:25 | INFO |   Encoded 736/1280
2026-05-08 14:03:25 | INFO |   Encoded 737/1280
2026-05-08 14:03:25 | INFO |   Encoded 738/1280
2026-05-08 14:03:25 | INFO |   Encoded 739/1280
2026-05-08 14:03:25 | INFO |   Encoded 740/1280
2026-05-08 14:03:25 | INFO |   Encoded 741/1280
2026-05-08 14:03:25 | INFO |   Encoded 742/1280
2026-05-08 14:03:25 | INFO |   Encoded 743/1280
2026-05-08 14:03:25 | INFO |   Encoded 744/1280
2026-05-08 14:03:25 | INFO |   Encoded 745/1280
2026-05-08 14:03:25 | INFO |   Encoded 746/1280
2026-05-08 14:03:25 | INFO |   Encoded 747/1280
2026-05-08 14:03:25 | INFO |   Encoded 748/1280
2026-05-08 14:03:25 | INFO |   Encoded 749/1280
2026-05-08 14:03:25 | INFO |   Encoded 750/1280
2026-05-08 14:03:25 | INFO |   Encoded 751/1280
2026-05-08 14:03:25 | INFO |   Encoded 752/1280
2026-05-08 14:03:25 | INFO |   Encoded 753/1280
2026-05-08 14:03:25 | INFO |   Encoded 754/1280
2026-05-08 14:03:25 | INFO |   Encoded 755/1280
2026-05-08 14:03:25 | INFO |   Encoded 756/1280
2026-05-08 14:03:25 | INFO |   Encoded 757/1280
2026-05-08 14:03:25 | INFO |   Encoded 758/1280
2026-05-08 14:03:25 | INFO |   Encoded 759/1280
2026-05-08 14:03:25 | INFO |   Encoded 760/1280
2026-05-08 14:03:25 | INFO |   Encoded 761/1280
2026-05-08 14:03:25 | INFO |   Encoded 762/1280
2026-05-08 14:03:25 | INFO |   Encoded 763/1280
2026-05-08 14:03:25 | INFO |   Encoded 764/1280
2026-05-08 14:03:25 | INFO |   Encoded 765/1280
2026-05-08 14:03:25 | INFO |   Encoded 766/1280
2026-05-08 14:03:25 | INFO |   Encoded 767/1280
2026-05-08 14:03:25 | INFO |   Encoded 768/1280
2026-05-08 14:03:25 | INFO |   Encoded 769/1280
2026-05-08 14:03:25 | INFO |   Encoded 770/1280
2026-05-08 14:03:25 | INFO |   Encoded 771/1280
2026-05-08 14:03:25 | INFO |   Encoded 772/1280
2026-05-08 14:03:25 | INFO |   Encoded 773/1280
2026-05-08 14:03:25 | INFO |   Encoded 774/1280
2026-05-08 14:03:25 | INFO |   Encoded 775/1280
2026-05-08 14:03:25 | INFO |   Encoded 776/1280
2026-05-08 14:03:25 | INFO |   Encoded 777/1280
2026-05-08 14:03:25 | INFO |   Encoded 778/1280
2026-05-08 14:03:25 | INFO |   Encoded 779/1280
2026-05-08 14:03:25 | INFO |   Encoded 780/1280
2026-05-08 14:03:25 | INFO |   Encoded 781/1280
2026-05-08 14:03:25 | INFO |   Encoded 782/1280
2026-05-08 14:03:25 | INFO |   Encoded 783/1280
2026-05-08 14:03:25 | INFO |   Encoded 784/1280
2026-05-08 14:03:25 | INFO |   Encoded 785/1280
2026-05-08 14:03:25 | INFO |   Encoded 786/1280
2026-05-08 14:03:25 | INFO |   Encoded 787/1280
2026-05-08 14:03:25 | INFO |   Encoded 788/1280
2026-05-08 14:03:25 | INFO |   Encoded 789/1280
2026-05-08 14:03:25 | INFO |   Encoded 790/1280
2026-05-08 14:03:25 | INFO |   Encoded 791/1280
2026-05-08 14:03:25 | INFO |   Encoded 792/1280
2026-05-08 14:03:25 | INFO |   Encoded 793/1280
2026-05-08 14:03:25 | INFO |   Encoded 794/1280
2026-05-08 14:03:25 | INFO |   Encoded 795/1280
2026-05-08 14:03:25 | INFO |   Encoded 796/1280
2026-05-08 14:03:25 | INFO |   Encoded 797/1280
2026-05-08 14:03:25 | INFO |   Encoded 798/1280
2026-05-08 14:03:25 | INFO |   Encoded 799/1280
2026-05-08 14:03:25 | INFO |   Encoded 800/1280
2026-05-08 14:03:25 | INFO |   Encoded 801/1280
2026-05-08 14:03:25 | INFO |   Encoded 802/1280
2026-05-08 14:03:25 | INFO |   Encoded 803/1280
2026-05-08 14:03:25 | INFO |   Encoded 804/1280
2026-05-08 14:03:25 | INFO |   Encoded 805/1280
2026-05-08 14:03:25 | INFO |   Encoded 806/1280
2026-05-08 14:03:25 | INFO |   Encoded 807/1280
2026-05-08 14:03:25 | INFO |   Encoded 808/1280
2026-05-08 14:03:25 | INFO |   Encoded 809/1280
2026-05-08 14:03:25 | INFO |   Encoded 810/1280
2026-05-08 14:03:25 | INFO |   Encoded 811/1280
2026-05-08 14:03:25 | INFO |   Encoded 812/1280
2026-05-08 14:03:25 | INFO |   Encoded 813/1280
2026-05-08 14:03:25 | INFO |   Encoded 814/1280
2026-05-08 14:03:25 | INFO |   Encoded 815/1280
2026-05-08 14:03:25 | INFO |   Encoded 816/1280
2026-05-08 14:03:25 | INFO |   Encoded 817/1280
2026-05-08 14:03:25 | INFO |   Encoded 818/1280
2026-05-08 14:03:25 | INFO |   Encoded 819/1280
2026-05-08 14:03:25 | INFO |   Encoded 820/1280
2026-05-08 14:03:25 | INFO |   Encoded 821/1280
2026-05-08 14:03:25 | INFO |   Encoded 822/1280
2026-05-08 14:03:25 | INFO |   Encoded 823/1280
2026-05-08 14:03:25 | INFO |   Encoded 824/1280
2026-05-08 14:03:25 | INFO |   Encoded 825/1280
2026-05-08 14:03:25 | INFO |   Encoded 826/1280
2026-05-08 14:03:25 | INFO |   Encoded 827/1280
2026-05-08 14:03:25 | INFO |   Encoded 828/1280
2026-05-08 14:03:25 | INFO |   Encoded 829/1280
2026-05-08 14:03:25 | INFO |   Encoded 830/1280
2026-05-08 14:03:25 | INFO |   Encoded 831/1280
2026-05-08 14:03:25 | INFO |   Encoded 832/1280
2026-05-08 14:03:25 | INFO |   Encoded 833/1280
2026-05-08 14:03:25 | INFO |   Encoded 834/1280
2026-05-08 14:03:25 | INFO |   Encoded 835/1280
2026-05-08 14:03:25 | INFO |   Encoded 836/1280
2026-05-08 14:03:25 | INFO |   Encoded 837/1280
2026-05-08 14:03:25 | INFO |   Encoded 838/1280
2026-05-08 14:03:25 | INFO |   Encoded 839/1280
2026-05-08 14:03:25 | INFO |   Encoded 840/1280
2026-05-08 14:03:25 | INFO |   Encoded 841/1280
2026-05-08 14:03:25 | INFO |   Encoded 842/1280
2026-05-08 14:03:25 | INFO |   Encoded 843/1280
2026-05-08 14:03:25 | INFO |   Encoded 844/1280
2026-05-08 14:03:25 | INFO |   Encoded 845/1280
2026-05-08 14:03:25 | INFO |   Encoded 846/1280
2026-05-08 14:03:25 | INFO |   Encoded 847/1280
2026-05-08 14:03:25 | INFO |   Encoded 848/1280
2026-05-08 14:03:25 | INFO |   Encoded 849/1280
2026-05-08 14:03:25 | INFO |   Encoded 850/1280
2026-05-08 14:03:25 | INFO |   Encoded 851/1280
2026-05-08 14:03:25 | INFO |   Encoded 852/1280
2026-05-08 14:03:25 | INFO |   Encoded 853/1280
2026-05-08 14:03:25 | INFO |   Encoded 854/1280
2026-05-08 14:03:25 | INFO |   Encoded 855/1280
2026-05-08 14:03:25 | INFO |   Encoded 856/1280
2026-05-08 14:03:25 | INFO |   Encoded 857/1280
2026-05-08 14:03:25 | INFO |   Encoded 858/1280
2026-05-08 14:03:25 | INFO |   Encoded 859/1280
2026-05-08 14:03:25 | INFO |   Encoded 860/1280
2026-05-08 14:03:25 | INFO |   Encoded 861/1280
2026-05-08 14:03:25 | INFO |   Encoded 862/1280
2026-05-08 14:03:25 | INFO |   Encoded 863/1280
2026-05-08 14:03:25 | INFO |   Encoded 864/1280
2026-05-08 14:03:25 | INFO |   Encoded 865/1280
2026-05-08 14:03:25 | INFO |   Encoded 866/1280
2026-05-08 14:03:25 | INFO |   Encoded 867/1280
2026-05-08 14:03:32 | INFO |   Encoded 868/1280`use_return_dict` is deprecated! Use `return_dict` instead!
2026-05-08 14:03:33 | INFO | UserWarning: torch.utils.checkpoint: the use_reentrant parameter should be passed explicitly. Starting in PyTorch 2.9, calling checkpoint without use_reentrant will raise an exception. use_reentrant=False is recommended, but if you need to preserve the current default behavior, you can pass use_reentrant=True. Refer to docs for more details on the differences between the two variants.
2026-05-08 14:03:33 | INFO | UserWarning: None of the inputs have requires_grad=True. Gradients will be None
2026-05-08 14:03:39 | INFO | FutureWarning: `torch.cuda.amp.autocast(args...)` is deprecated. Please use `torch.amp.autocast('cuda', args...)` instead.
2026-05-08 14:04:56 | INFO | UserWarning: torch.utils.checkpoint: the use_reentrant parameter should be passed explicitly. Starting in PyTorch 2.9, calling checkpoint without use_reentrant will raise an exception. use_reentrant=False is recommended, but if you need to preserve the current default behavior, you can pass use_reentrant=True. Refer to docs for more details on the differences between the two variants.
2026-05-08 14:04:56 | INFO | UserWarning: None of the inputs have requires_grad=True. Gradients will be None
2026-05-08 14:05:00 | INFO | FutureWarning: `torch.cuda.amp.autocast(args...)` is deprecated. Please use `torch.amp.autocast('cuda', args...)` instead.
2026-05-08 14:09:17 | INFO | 
2026-05-08 14:09:17 | INFO |   Encoded 869/1280
2026-05-08 14:09:17 | INFO |   Encoded 870/1280
2026-05-08 14:09:17 | INFO |   Encoded 871/1280
2026-05-08 14:09:17 | INFO |   Encoded 872/1280
2026-05-08 14:09:17 | INFO |   Encoded 873/1280
2026-05-08 14:09:17 | INFO |   Encoded 874/1280
2026-05-08 14:09:17 | INFO |   Encoded 875/1280
2026-05-08 14:09:17 | INFO |   Encoded 876/1280
2026-05-08 14:09:17 | INFO |   Encoded 877/1280
2026-05-08 14:09:17 | INFO |   Encoded 878/1280
2026-05-08 14:09:17 | INFO |   Encoded 879/1280
2026-05-08 14:09:17 | INFO |   Encoded 880/1280
2026-05-08 14:09:17 | INFO |   Encoded 881/1280
2026-05-08 14:09:17 | INFO |   Encoded 882/1280
2026-05-08 14:09:17 | INFO |   Encoded 883/1280
2026-05-08 14:09:17 | INFO |   Encoded 884/1280
2026-05-08 14:09:17 | INFO |   Encoded 885/1280
2026-05-08 14:09:17 | INFO |   Encoded 886/1280
2026-05-08 14:09:17 | INFO |   Encoded 887/1280
2026-05-08 14:09:17 | INFO |   Encoded 888/1280
2026-05-08 14:09:17 | INFO |   Encoded 889/1280
2026-05-08 14:09:17 | INFO |   Encoded 890/1280
2026-05-08 14:09:17 | INFO |   Encoded 891/1280
2026-05-08 14:09:17 | INFO |   Encoded 892/1280
2026-05-08 14:09:17 | INFO |   Encoded 893/1280
2026-05-08 14:09:17 | INFO |   Encoded 894/1280
2026-05-08 14:09:17 | INFO |   Encoded 895/1280
2026-05-08 14:09:17 | INFO |   Encoded 896/1280
2026-05-08 14:09:17 | INFO |   Encoded 897/1280
2026-05-08 14:09:17 | INFO |   Encoded 898/1280
2026-05-08 14:09:17 | INFO |   Encoded 899/1280
2026-05-08 14:09:17 | INFO |   Encoded 900/1280
2026-05-08 14:09:17 | INFO |   Encoded 901/1280
2026-05-08 14:09:17 | INFO |   Encoded 902/1280
2026-05-08 14:09:17 | INFO |   Encoded 903/1280
2026-05-08 14:09:17 | INFO |   Encoded 904/1280
2026-05-08 14:09:17 | INFO |   Encoded 905/1280
2026-05-08 14:09:17 | INFO |   Encoded 906/1280
2026-05-08 14:09:17 | INFO |   Encoded 907/1280
2026-05-08 14:09:17 | INFO |   Encoded 908/1280
2026-05-08 14:09:17 | INFO |   Encoded 909/1280
2026-05-08 14:09:17 | INFO |   Encoded 910/1280
2026-05-08 14:09:17 | INFO |   Encoded 911/1280
2026-05-08 14:09:17 | INFO |   Encoded 912/1280
2026-05-08 14:09:17 | INFO |   Encoded 913/1280
2026-05-08 14:09:17 | INFO |   Encoded 914/1280
2026-05-08 14:09:17 | INFO |   Encoded 915/1280
2026-05-08 14:09:17 | INFO |   Encoded 916/1280
2026-05-08 14:09:17 | INFO |   Encoded 917/1280
2026-05-08 14:09:17 | INFO |   Encoded 918/1280
2026-05-08 14:09:17 | INFO |   Encoded 919/1280
2026-05-08 14:09:17 | INFO |   Encoded 920/1280
2026-05-08 14:09:17 | INFO |   Encoded 921/1280
2026-05-08 14:09:17 | INFO |   Encoded 922/1280
2026-05-08 14:09:17 | INFO |   Encoded 923/1280
2026-05-08 14:09:17 | INFO |   Encoded 924/1280
2026-05-08 14:09:17 | INFO |   Encoded 925/1280
2026-05-08 14:09:17 | INFO |   Encoded 926/1280
2026-05-08 14:09:17 | INFO |   Encoded 927/1280
2026-05-08 14:09:17 | INFO |   Encoded 928/1280
2026-05-08 14:09:17 | INFO |   Encoded 929/1280
2026-05-08 14:09:17 | INFO |   Encoded 930/1280
2026-05-08 14:09:17 | INFO |   Encoded 931/1280
2026-05-08 14:09:17 | INFO |   Encoded 932/1280
2026-05-08 14:09:17 | INFO |   Encoded 933/1280
2026-05-08 14:09:17 | INFO |   Encoded 934/1280
2026-05-08 14:09:17 | INFO |   Encoded 935/1280
2026-05-08 14:09:17 | INFO |   Encoded 936/1280
2026-05-08 14:09:17 | INFO |   Encoded 937/1280
2026-05-08 14:09:17 | INFO |   Encoded 938/1280
2026-05-08 14:09:17 | INFO |   Encoded 939/1280
2026-05-08 14:09:17 | INFO |   Encoded 940/1280
2026-05-08 14:09:17 | INFO |   Encoded 941/1280
2026-05-08 14:09:17 | INFO |   Encoded 942/1280
2026-05-08 14:09:17 | INFO |   Encoded 943/1280
2026-05-08 14:09:17 | INFO |   Encoded 944/1280
2026-05-08 14:09:17 | INFO |   Encoded 945/1280
2026-05-08 14:09:17 | INFO |   Encoded 946/1280
2026-05-08 14:09:17 | INFO |   Encoded 947/1280
2026-05-08 14:09:17 | INFO |   Encoded 948/1280
2026-05-08 14:09:17 | INFO |   Encoded 949/1280
2026-05-08 14:09:17 | INFO |   Encoded 950/1280
2026-05-08 14:09:17 | INFO |   Encoded 951/1280
2026-05-08 14:09:17 | INFO |   Encoded 952/1280
2026-05-08 14:09:17 | INFO |   Encoded 953/1280
2026-05-08 14:09:17 | INFO |   Encoded 954/1280
2026-05-08 14:09:17 | INFO |   Encoded 955/1280
2026-05-08 14:09:17 | INFO |   Encoded 956/1280
2026-05-08 14:09:17 | INFO |   Encoded 957/1280
2026-05-08 14:09:17 | INFO |   Encoded 958/1280
2026-05-08 14:09:17 | INFO |   Encoded 959/1280
2026-05-08 14:09:17 | INFO |   Encoded 960/1280
2026-05-08 14:09:17 | INFO |   Encoded 961/1280
2026-05-08 14:09:17 | INFO |   Encoded 962/1280
2026-05-08 14:09:17 | INFO |   Encoded 963/1280
2026-05-08 14:09:17 | INFO |   Encoded 964/1280
2026-05-08 14:09:17 | INFO |   Encoded 965/1280
2026-05-08 14:09:17 | INFO |   Encoded 966/1280
2026-05-08 14:09:17 | INFO |   Encoded 967/1280
2026-05-08 14:09:17 | INFO |   Encoded 968/1280
2026-05-08 14:09:17 | INFO |   Encoded 969/1280
2026-05-08 14:09:17 | INFO |   Encoded 970/1280
2026-05-08 14:09:17 | INFO |   Encoded 971/1280
2026-05-08 14:09:17 | INFO |   Encoded 972/1280
2026-05-08 14:09:17 | INFO |   Encoded 973/1280
2026-05-08 14:09:17 | INFO |   Encoded 974/1280
2026-05-08 14:09:17 | INFO |   Encoded 975/1280
2026-05-08 14:09:17 | INFO |   Encoded 976/1280
2026-05-08 14:09:17 | INFO |   Encoded 977/1280
2026-05-08 14:09:17 | INFO |   Encoded 978/1280
2026-05-08 14:09:17 | INFO |   Encoded 979/1280
2026-05-08 14:09:17 | INFO |   Encoded 980/1280
2026-05-08 14:09:17 | INFO |   Encoded 981/1280
2026-05-08 14:09:17 | INFO |   Encoded 982/1280
2026-05-08 14:09:17 | INFO |   Encoded 983/1280
2026-05-08 14:09:17 | INFO |   Encoded 984/1280
2026-05-08 14:09:17 | INFO |   Encoded 985/1280
2026-05-08 14:09:17 | INFO |   Encoded 986/1280
2026-05-08 14:09:17 | INFO |   Encoded 987/1280
2026-05-08 14:09:17 | INFO |   Encoded 988/1280
2026-05-08 14:09:17 | INFO |   Encoded 989/1280
2026-05-08 14:09:17 | INFO |   Encoded 990/1280
2026-05-08 14:09:17 | INFO |   Encoded 991/1280
2026-05-08 14:09:17 | INFO |   Encoded 992/1280
2026-05-08 14:09:17 | INFO |   Encoded 993/1280
2026-05-08 14:09:17 | INFO |   Encoded 994/1280
2026-05-08 14:09:17 | INFO |   Encoded 995/1280
2026-05-08 14:09:17 | INFO |   Encoded 996/1280
2026-05-08 14:09:17 | INFO |   Encoded 997/1280
2026-05-08 14:09:17 | INFO |   Encoded 998/1280
2026-05-08 14:09:17 | INFO |   Encoded 999/1280
2026-05-08 14:09:17 | INFO |   Encoded 1000/1280
2026-05-08 14:09:17 | INFO |   Encoded 1001/1280
2026-05-08 14:09:17 | INFO |   Encoded 1002/1280
2026-05-08 14:09:17 | INFO |   Encoded 1003/1280
2026-05-08 14:09:17 | INFO |   Encoded 1004/1280
2026-05-08 14:09:17 | INFO |   Encoded 1005/1280
2026-05-08 14:09:17 | INFO |   Encoded 1006/1280
2026-05-08 14:09:17 | INFO |   Encoded 1007/1280
2026-05-08 14:09:17 | INFO |   Encoded 1008/1280
2026-05-08 14:09:17 | INFO |   Encoded 1009/1280
2026-05-08 14:09:17 | INFO |   Encoded 1010/1280
2026-05-08 14:09:17 | INFO |   Encoded 1011/1280
2026-05-08 14:09:17 | INFO |   Encoded 1012/1280
2026-05-08 14:09:17 | INFO |   Encoded 1013/1280
2026-05-08 14:09:17 | INFO |   Encoded 1014/1280
2026-05-08 14:09:17 | INFO |   Encoded 1015/1280
2026-05-08 14:09:17 | INFO |   Encoded 1016/1280
2026-05-08 14:09:17 | INFO |   Encoded 1017/1280
2026-05-08 14:09:17 | INFO |   Encoded 1018/1280
2026-05-08 14:09:17 | INFO |   Encoded 1019/1280
2026-05-08 14:09:17 | INFO |   Encoded 1020/1280
2026-05-08 14:09:17 | INFO |   Encoded 1021/1280
2026-05-08 14:09:17 | INFO |   Encoded 1022/1280
2026-05-08 14:09:17 | INFO |   Encoded 1023/1280
2026-05-08 14:09:17 | INFO |   Encoded 1024/1280
2026-05-08 14:09:17 | INFO |   Encoded 1025/1280
2026-05-08 14:09:17 | INFO |   Encoded 1026/1280
2026-05-08 14:09:17 | INFO |   Encoded 1027/1280
2026-05-08 14:09:17 | INFO |   Encoded 1028/1280
2026-05-08 14:09:17 | INFO |   Encoded 1029/1280
2026-05-08 14:09:17 | INFO |   Encoded 1030/1280
2026-05-08 14:09:17 | INFO |   Encoded 1031/1280
2026-05-08 14:09:17 | INFO |   Encoded 1032/1280
2026-05-08 14:09:17 | INFO |   Encoded 1033/1280
2026-05-08 14:09:17 | INFO |   Encoded 1034/1280
2026-05-08 14:09:17 | INFO |   Encoded 1035/1280
2026-05-08 14:09:17 | INFO |   Encoded 1036/1280
2026-05-08 14:09:17 | INFO |   Encoded 1037/1280
2026-05-08 14:09:17 | INFO |   Encoded 1038/1280
2026-05-08 14:09:17 | INFO |   Encoded 1039/1280
2026-05-08 14:09:17 | INFO |   Encoded 1040/1280
2026-05-08 14:09:17 | INFO |   Encoded 1041/1280
2026-05-08 14:09:17 | INFO |   Encoded 1042/1280
2026-05-08 14:09:17 | INFO |   Encoded 1043/1280
2026-05-08 14:09:17 | INFO |   Encoded 1044/1280
2026-05-08 14:09:17 | INFO |   Encoded 1045/1280
2026-05-08 14:09:17 | INFO |   Encoded 1046/1280
2026-05-08 14:09:17 | INFO |   Encoded 1047/1280
2026-05-08 14:09:17 | INFO |   Encoded 1048/1280
2026-05-08 14:09:17 | INFO |   Encoded 1049/1280
2026-05-08 14:09:17 | INFO |   Encoded 1050/1280
2026-05-08 14:09:17 | INFO |   Encoded 1051/1280
2026-05-08 14:09:17 | INFO |   Encoded 1052/1280
2026-05-08 14:09:17 | INFO |   Encoded 1053/1280
2026-05-08 14:09:17 | INFO |   Encoded 1054/1280
2026-05-08 14:09:17 | INFO |   Encoded 1055/1280
2026-05-08 14:09:17 | INFO |   Encoded 1056/1280
2026-05-08 14:09:17 | INFO |   Encoded 1057/1280
2026-05-08 14:09:17 | INFO |   Encoded 1058/1280
2026-05-08 14:09:17 | INFO |   Encoded 1059/1280
2026-05-08 14:09:17 | INFO |   Encoded 1060/1280
2026-05-08 14:09:17 | INFO |   Encoded 1061/1280
2026-05-08 14:09:17 | INFO |   Encoded 1062/1280
2026-05-08 14:09:17 | INFO |   Encoded 1063/1280
2026-05-08 14:09:17 | INFO |   Encoded 1064/1280
2026-05-08 14:09:17 | INFO |   Encoded 1065/1280
2026-05-08 14:09:17 | INFO |   Encoded 1066/1280
2026-05-08 14:09:17 | INFO |   Encoded 1067/1280
2026-05-08 14:09:17 | INFO |   Encoded 1068/1280
2026-05-08 14:09:17 | INFO |   Encoded 1069/1280
2026-05-08 14:09:17 | INFO |   Encoded 1070/1280
2026-05-08 14:09:17 | INFO |   Encoded 1071/1280
2026-05-08 14:09:17 | INFO |   Encoded 1072/1280
2026-05-08 14:09:17 | INFO |   Encoded 1073/1280
2026-05-08 14:09:17 | INFO |   Encoded 1074/1280
2026-05-08 14:09:17 | INFO |   Encoded 1075/1280
2026-05-08 14:09:17 | INFO |   Encoded 1076/1280
2026-05-08 14:09:17 | INFO |   Encoded 1077/1280
2026-05-08 14:09:17 | INFO |   Encoded 1078/1280
2026-05-08 14:09:17 | INFO |   Encoded 1079/1280
2026-05-08 14:09:17 | INFO |   Encoded 1080/1280
2026-05-08 14:09:17 | INFO |   Encoded 1081/1280
2026-05-08 14:09:17 | INFO |   Encoded 1082/1280
2026-05-08 14:09:17 | INFO |   Encoded 1083/1280
2026-05-08 14:09:17 | INFO |   Encoded 1084/1280
2026-05-08 14:09:17 | INFO |   Encoded 1085/1280
2026-05-08 14:09:17 | INFO |   Encoded 1086/1280
2026-05-08 14:09:17 | INFO |   Encoded 1087/1280
2026-05-08 14:09:17 | INFO |   Encoded 1088/1280
2026-05-08 14:09:17 | INFO |   Encoded 1089/1280
2026-05-08 14:09:17 | INFO |   Encoded 1090/1280
2026-05-08 14:09:17 | INFO |   Encoded 1091/1280
2026-05-08 14:09:17 | INFO |   Encoded 1092/1280
2026-05-08 14:09:17 | INFO |   Encoded 1093/1280
2026-05-08 14:09:17 | INFO |   Encoded 1094/1280
2026-05-08 14:09:17 | INFO |   Encoded 1095/1280
2026-05-08 14:09:17 | INFO |   Encoded 1096/1280
2026-05-08 14:09:17 | INFO |   Encoded 1097/1280
2026-05-08 14:09:17 | INFO |   Encoded 1098/1280
2026-05-08 14:09:17 | INFO |   Encoded 1099/1280
2026-05-08 14:09:17 | INFO |   Encoded 1100/1280
2026-05-08 14:09:17 | INFO |   Encoded 1101/1280
2026-05-08 14:09:17 | INFO |   Encoded 1102/1280
2026-05-08 14:09:17 | INFO |   Encoded 1103/1280
2026-05-08 14:09:17 | INFO |   Encoded 1104/1280
2026-05-08 14:09:17 | INFO |   Encoded 1105/1280
2026-05-08 14:09:17 | INFO |   Encoded 1106/1280
2026-05-08 14:09:17 | INFO |   Encoded 1107/1280
2026-05-08 14:09:17 | INFO |   Encoded 1108/1280
2026-05-08 14:09:17 | INFO |   Encoded 1109/1280
2026-05-08 14:09:17 | INFO |   Encoded 1110/1280
2026-05-08 14:09:17 | INFO |   Encoded 1111/1280
2026-05-08 14:09:17 | INFO |   Encoded 1112/1280
2026-05-08 14:09:17 | INFO |   Encoded 1113/1280
2026-05-08 14:09:17 | INFO |   Encoded 1114/1280
2026-05-08 14:09:17 | INFO |   Encoded 1115/1280
2026-05-08 14:09:17 | INFO |   Encoded 1116/1280
2026-05-08 14:09:17 | INFO |   Encoded 1117/1280
2026-05-08 14:09:17 | INFO |   Encoded 1118/1280
2026-05-08 14:09:17 | INFO |   Encoded 1119/1280
2026-05-08 14:09:17 | INFO |   Encoded 1120/1280
2026-05-08 14:09:17 | INFO |   Encoded 1121/1280
2026-05-08 14:09:17 | INFO |   Encoded 1122/1280
2026-05-08 14:09:17 | INFO |   Encoded 1123/1280
2026-05-08 14:09:17 | INFO |   Encoded 1124/1280
2026-05-08 14:09:17 | INFO |   Encoded 1125/1280
2026-05-08 14:09:17 | INFO |   Encoded 1126/1280
2026-05-08 14:09:17 | INFO |   Encoded 1127/1280
2026-05-08 14:09:17 | INFO |   Encoded 1128/1280
2026-05-08 14:09:17 | INFO |   Encoded 1129/1280
2026-05-08 14:09:17 | INFO |   Encoded 1130/1280
2026-05-08 14:09:17 | INFO |   Encoded 1131/1280
2026-05-08 14:09:17 | INFO |   Encoded 1132/1280
2026-05-08 14:09:17 | INFO |   Encoded 1133/1280
2026-05-08 14:09:17 | INFO |   Encoded 1134/1280
2026-05-08 14:09:17 | INFO |   Encoded 1135/1280
2026-05-08 14:09:17 | INFO |   Encoded 1136/1280
2026-05-08 14:09:17 | INFO |   Encoded 1137/1280
2026-05-08 14:09:17 | INFO |   Encoded 1138/1280
2026-05-08 14:09:17 | INFO |   Encoded 1139/1280
2026-05-08 14:09:17 | INFO |   Encoded 1140/1280
2026-05-08 14:09:17 | INFO |   Encoded 1141/1280
2026-05-08 14:09:17 | INFO |   Encoded 1142/1280
2026-05-08 14:09:17 | INFO |   Encoded 1143/1280
2026-05-08 14:09:17 | INFO |   Encoded 1144/1280
2026-05-08 14:09:17 | INFO |   Encoded 1145/1280
2026-05-08 14:09:17 | INFO |   Encoded 1146/1280
2026-05-08 14:09:17 | INFO |   Encoded 1147/1280
2026-05-08 14:09:17 | INFO |   Encoded 1148/1280
2026-05-08 14:09:17 | INFO |   Encoded 1149/1280
2026-05-08 14:09:17 | INFO |   Encoded 1150/1280
2026-05-08 14:09:17 | INFO |   Encoded 1151/1280
2026-05-08 14:09:17 | INFO |   Encoded 1152/1280
2026-05-08 14:09:17 | INFO |   Encoded 1153/1280
2026-05-08 14:09:17 | INFO |   Encoded 1154/1280
2026-05-08 14:09:17 | INFO |   Encoded 1155/1280
2026-05-08 14:09:17 | INFO |   Encoded 1156/1280
2026-05-08 14:09:17 | INFO |   Encoded 1157/1280
2026-05-08 14:09:17 | INFO |   Encoded 1158/1280
2026-05-08 14:09:17 | INFO |   Encoded 1159/1280
2026-05-08 14:09:17 | INFO |   Encoded 1160/1280
2026-05-08 14:09:17 | INFO |   Encoded 1161/1280
2026-05-08 14:09:17 | INFO |   Encoded 1162/1280
2026-05-08 14:09:17 | INFO |   Encoded 1163/1280
2026-05-08 14:09:17 | INFO |   Encoded 1164/1280
2026-05-08 14:09:17 | INFO |   Encoded 1165/1280
2026-05-08 14:09:17 | INFO |   Encoded 1166/1280
2026-05-08 14:09:17 | INFO |   Encoded 1167/1280
2026-05-08 14:09:17 | INFO |   Encoded 1168/1280
2026-05-08 14:09:17 | INFO |   Encoded 1169/1280
2026-05-08 14:09:17 | INFO |   Encoded 1170/1280
2026-05-08 14:09:17 | INFO |   Encoded 1171/1280
2026-05-08 14:09:17 | INFO |   Encoded 1172/1280
2026-05-08 14:09:17 | INFO |   Encoded 1173/1280
2026-05-08 14:09:17 | INFO |   Encoded 1174/1280
2026-05-08 14:09:17 | INFO |   Encoded 1175/1280
2026-05-08 14:09:17 | INFO |   Encoded 1176/1280
2026-05-08 14:09:17 | INFO |   Encoded 1177/1280
2026-05-08 14:09:17 | INFO |   Encoded 1178/1280
2026-05-08 14:09:17 | INFO |   Encoded 1179/1280
2026-05-08 14:09:17 | INFO |   Encoded 1180/1280
2026-05-08 14:09:17 | INFO |   Encoded 1181/1280
2026-05-08 14:09:17 | INFO |   Encoded 1182/1280
2026-05-08 14:09:17 | INFO |   Encoded 1183/1280
2026-05-08 14:09:17 | INFO |   Encoded 1184/1280
2026-05-08 14:09:17 | INFO |   Encoded 1185/1280
2026-05-08 14:09:17 | INFO |   Encoded 1186/1280
2026-05-08 14:09:17 | INFO |   Encoded 1187/1280
2026-05-08 14:09:17 | INFO |   Encoded 1188/1280
2026-05-08 14:09:17 | INFO |   Encoded 1189/1280
2026-05-08 14:09:17 | INFO |   Encoded 1190/1280
2026-05-08 14:09:17 | INFO |   Encoded 1191/1280
2026-05-08 14:09:17 | INFO |   Encoded 1192/1280
2026-05-08 14:09:17 | INFO |   Encoded 1193/1280
2026-05-08 14:09:17 | INFO |   Encoded 1194/1280
2026-05-08 14:09:17 | INFO |   Encoded 1195/1280
2026-05-08 14:09:17 | INFO |   Encoded 1196/1280
2026-05-08 14:09:17 | INFO |   Encoded 1197/1280
2026-05-08 14:09:17 | INFO |   Encoded 1198/1280
2026-05-08 14:09:17 | INFO |   Encoded 1199/1280
2026-05-08 14:09:17 | INFO |   Encoded 1200/1280
2026-05-08 14:09:17 | INFO |   Encoded 1201/1280
2026-05-08 14:09:17 | INFO |   Encoded 1202/1280
2026-05-08 14:09:17 | INFO |   Encoded 1203/1280
2026-05-08 14:09:17 | INFO |   Encoded 1204/1280
2026-05-08 14:09:17 | INFO |   Encoded 1205/1280
2026-05-08 14:09:17 | INFO |   Encoded 1206/1280
2026-05-08 14:09:17 | INFO |   Encoded 1207/1280
2026-05-08 14:09:17 | INFO |   Encoded 1208/1280
2026-05-08 14:09:17 | INFO |   Encoded 1209/1280
2026-05-08 14:09:17 | INFO |   Encoded 1210/1280
2026-05-08 14:09:17 | INFO |   Encoded 1211/1280
2026-05-08 14:09:17 | INFO |   Encoded 1212/1280
2026-05-08 14:09:17 | INFO |   Encoded 1213/1280
2026-05-08 14:09:17 | INFO |   Encoded 1214/1280
2026-05-08 14:09:17 | INFO |   Encoded 1215/1280
2026-05-08 14:09:17 | INFO |   Encoded 1216/1280
2026-05-08 14:09:17 | INFO |   Encoded 1217/1280
2026-05-08 14:09:17 | INFO |   Encoded 1218/1280
2026-05-08 14:09:17 | INFO |   Encoded 1219/1280
2026-05-08 14:09:17 | INFO |   Encoded 1220/1280
2026-05-08 14:09:17 | INFO |   Encoded 1221/1280
2026-05-08 14:09:17 | INFO |   Encoded 1222/1280
2026-05-08 14:09:17 | INFO |   Encoded 1223/1280
2026-05-08 14:09:17 | INFO |   Encoded 1224/1280
2026-05-08 14:09:17 | INFO |   Encoded 1225/1280
2026-05-08 14:09:17 | INFO |   Encoded 1226/1280
2026-05-08 14:09:17 | INFO |   Encoded 1227/1280
2026-05-08 14:09:17 | INFO |   Encoded 1228/1280
2026-05-08 14:09:17 | INFO |   Encoded 1229/1280
2026-05-08 14:09:17 | INFO |   Encoded 1230/1280
2026-05-08 14:09:17 | INFO |   Encoded 1231/1280
2026-05-08 14:09:17 | INFO |   Encoded 1232/1280
2026-05-08 14:09:17 | INFO |   Encoded 1233/1280
2026-05-08 14:09:17 | INFO |   Encoded 1234/1280
2026-05-08 14:09:17 | INFO |   Encoded 1235/1280
2026-05-08 14:09:17 | INFO |   Encoded 1236/1280
2026-05-08 14:09:17 | INFO |   Encoded 1237/1280
2026-05-08 14:09:17 | INFO |   Encoded 1238/1280
2026-05-08 14:09:17 | INFO |   Encoded 1239/1280
2026-05-08 14:09:17 | INFO |   Encoded 1240/1280
2026-05-08 14:09:17 | INFO |   Encoded 1241/1280
2026-05-08 14:09:17 | INFO |   Encoded 1242/1280
2026-05-08 14:09:17 | INFO |   Encoded 1243/1280
2026-05-08 14:09:17 | INFO |   Encoded 1244/1280
2026-05-08 14:09:17 | INFO |   Encoded 1245/1280
2026-05-08 14:09:17 | INFO |   Encoded 1246/1280
2026-05-08 14:09:17 | INFO |   Encoded 1247/1280
2026-05-08 14:09:17 | INFO |   Encoded 1248/1280
2026-05-08 14:09:17 | INFO |   Encoded 1249/1280
2026-05-08 14:09:17 | INFO |   Encoded 1250/1280
2026-05-08 14:09:17 | INFO |   Encoded 1251/1280
2026-05-08 14:09:17 | INFO |   Encoded 1252/1280
2026-05-08 14:09:17 | INFO |   Encoded 1253/1280
2026-05-08 14:09:17 | INFO |   Encoded 1254/1280
2026-05-08 14:09:17 | INFO |   Encoded 1255/1280
2026-05-08 14:09:17 | INFO |   Encoded 1256/1280
2026-05-08 14:09:17 | INFO |   Encoded 1257/1280
2026-05-08 14:09:17 | INFO |   Encoded 1258/1280
2026-05-08 14:09:17 | INFO |   Encoded 1259/1280
2026-05-08 14:09:17 | INFO |   Encoded 1260/1280
2026-05-08 14:09:17 | INFO |   Encoded 1261/1280
2026-05-08 14:09:17 | INFO |   Encoded 1262/1280
2026-05-08 14:09:17 | INFO |   Encoded 1263/1280
2026-05-08 14:09:17 | INFO |   Encoded 1264/1280
2026-05-08 14:09:17 | INFO |   Encoded 1265/1280
2026-05-08 14:09:17 | INFO |   Encoded 1266/1280
2026-05-08 14:09:17 | INFO |   Encoded 1267/1280
2026-05-08 14:09:17 | INFO |   Encoded 1268/1280
2026-05-08 14:09:17 | INFO |   Encoded 1269/1280
2026-05-08 14:09:17 | INFO |   Encoded 1270/1280
2026-05-08 14:09:17 | INFO |   Encoded 1271/1280
2026-05-08 14:09:17 | INFO |   Encoded 1272/1280
2026-05-08 14:09:17 | INFO |   Encoded 1273/1280
2026-05-08 14:09:17 | INFO |   Encoded 1274/1280
2026-05-08 14:09:17 | INFO |   Encoded 1275/1280
2026-05-08 14:09:17 | INFO |   Encoded 1276/1280
2026-05-08 14:09:17 | INFO |   Encoded 1277/1280
2026-05-08 14:09:17 | INFO |   Encoded 1278/1280
2026-05-08 14:09:17 | INFO |   Encoded 1279/1280
2026-05-08 14:09:17 | INFO |   Encoded 1280/1280
2026-05-08 14:09:17 | INFO | Computing similarity sequence...
2026-05-08 14:09:17 | INFO | 📼 CLIP similarity list calculated and saved.
2026-05-08 14:10:15 | INFO | UserWarning: torch.utils.checkpoint: the use_reentrant parameter should be passed explicitly. Starting in PyTorch 2.9, calling checkpoint without use_reentrant will raise an exception. use_reentrant=False is recommended, but if you need to preserve the current default behavior, you can pass use_reentrant=True. Refer to docs for more details on the differences between the two variants.
2026-05-08 14:10:15 | INFO | UserWarning: None of the inputs have requires_grad=True. Gradients will be None
2026-05-08 14:10:20 | INFO | FutureWarning: `torch.cuda.amp.autocast(args...)` is deprecated. Please use `torch.amp.autocast('cuda', args...)` instead.
2026-05-08 14:12:03 | INFO | 
2026-05-08 14:12:03 | INFO | 📂 Processing segment 0...
2026-05-08 14:12:03 | INFO | Taking screenshot: /sdcard/screenshot-0.png -> /Users/tanmaybhuskute/Documents/gifdroid-reproduction/apps/antennapod/llm/ViBR_gemini/handheld/run-008/artifacts/hhv-002/step_0_screenshot-0.png
2026-05-08 14:12:03 | INFO | 🔍 Annotated DINO output saved to /Users/tanmaybhuskute/Documents/gifdroid-reproduction/apps/antennapod/llm/ViBR_gemini/handheld/run-008/artifacts/hhv-002/step_0_dino.png
2026-05-08 14:12:03 | INFO | /Users/tanmaybhuskute/Documents/gifdroid-reproduction/apps/antennapod/llm/ViBR_gemini/handheld/run-008/artifacts/hhv-002/step_0_dino.png
2026-05-08 14:12:03 | INFO | /Users/tanmaybhuskute/Documents/gifdroid-reproduction/apps/antennapod/llm/ViBR_gemini/handheld/run-008/artifacts/hhv-002/step_0_tmp_stop.png
2026-05-08 14:12:03 | INFO | Relevant Region Response from Gemini: ```json
2026-05-08 14:12:03 | INFO | {
2026-05-08 14:12:03 | INFO |   "target_regions": [
2026-05-08 14:12:03 | INFO |     4
2026-05-08 14:12:03 | INFO |   ],
2026-05-08 14:12:03 | INFO |   "predicted_action": "tap"
2026-05-08 14:12:03 | INFO | }
2026-05-08 14:12:03 | INFO | ```
2026-05-08 14:12:03 | INFO | 🔍 Relevant regions: {'target_regions': [4], 'predicted_action': 'tap'}
2026-05-08 14:12:03 | INFO | 🧠 GPT selected regions: [4]
2026-05-08 14:12:03 | INFO | ✅ Relevant-only annotation saved to /Users/tanmaybhuskute/Documents/gifdroid-reproduction/apps/antennapod/llm/ViBR_gemini/handheld/run-008/artifacts/hhv-002/step_0_relevant_regions.png
2026-05-08 14:12:03 | INFO | /Users/tanmaybhuskute/Documents/gifdroid-reproduction/apps/antennapod/llm/ViBR_gemini/handheld/run-008/artifacts/hhv-002/step_0_relevant_regions.png
2026-05-08 14:12:03 | INFO | /Users/tanmaybhuskute/Documents/gifdroid-reproduction/apps/antennapod/llm/ViBR_gemini/handheld/run-008/artifacts/hhv-002/step_0_screenshot-0.png
2026-05-08 14:12:03 | INFO | Consistency Response from Gemini: ```json
2026-05-08 14:12:03 | INFO | {
2026-05-08 14:12:03 | INFO |   "same_state": "no",
2026-05-08 14:12:03 | INFO |   "description": "The reference screen is the 'Subscriptions' page, which features a prominent '+' button in the bottom navigation bar to add a new subscription. The current screen is the 'Home' page, which has a different bottom navigation bar without the '+' button. Therefore, the action of tapping the '+' button cannot be performed from the current screen."
2026-05-08 14:12:03 | INFO | }
2026-05-08 14:12:03 | INFO | ```
2026-05-08 14:12:03 | INFO | 🔄 Attempting to align state (try 1/3)...
2026-05-08 14:12:03 | INFO | /Users/tanmaybhuskute/Documents/gifdroid-reproduction/apps/antennapod/llm/ViBR_gemini/handheld/run-008/artifacts/hhv-002/step_0_tmp_start.png
2026-05-08 14:12:03 | INFO | /Users/tanmaybhuskute/Documents/gifdroid-reproduction/apps/antennapod/llm/ViBR_gemini/handheld/run-008/artifacts/hhv-002/step_0_tmp_stop.png
2026-05-08 14:12:03 | INFO | /Users/tanmaybhuskute/Documents/gifdroid-reproduction/apps/antennapod/llm/ViBR_gemini/handheld/run-008/artifacts/hhv-002/step_0_labeled.png
2026-05-08 14:12:03 | INFO | Region Action Response from Gemini: ```json
2026-05-08 14:12:03 | INFO | {
2026-05-08 14:12:03 | INFO |     "action": "tap",
2026-05-08 14:12:03 | INFO |     "region": 4,
2026-05-08 14:12:03 | INFO |     "description": "Tap on the Subscriptions tab in the bottom navigation bar."
2026-05-08 14:12:03 | INFO | }
2026-05-08 14:12:03 | INFO | ```
2026-05-08 14:12:03 | INFO | 🎯 Recovery using region index: 4 at (756, 1773)
2026-05-08 14:12:03 | INFO | [1] Tap on the Subscriptions tab in the bottom navigation bar. -> tap
2026-05-08 14:12:03 | INFO | Taking screenshot: /sdcard/screenshot-0.png -> /Users/tanmaybhuskute/Documents/gifdroid-reproduction/apps/antennapod/llm/ViBR_gemini/handheld/run-008/artifacts/hhv-002/step_0_screenshot-0.png
2026-05-08 14:12:03 | INFO | /Users/tanmaybhuskute/Documents/gifdroid-reproduction/apps/antennapod/llm/ViBR_gemini/handheld/run-008/artifacts/hhv-002/step_0_tmp_start.png
2026-05-08 14:12:03 | INFO | /Users/tanmaybhuskute/Documents/gifdroid-reproduction/apps/antennapod/llm/ViBR_gemini/handheld/run-008/artifacts/hhv-002/step_0_screenshot-0.png
2026-05-08 14:12:03 | INFO | Consistency Response from Gemini: ```json
2026-05-08 14:12:03 | INFO | {
2026-05-08 14:12:03 | INFO |   "same_state": "yes"
2026-05-08 14:12:03 | INFO | }
2026-05-08 14:12:03 | INFO | ```
2026-05-08 14:12:03 | INFO | /Users/tanmaybhuskute/Documents/gifdroid-reproduction/apps/antennapod/llm/ViBR_gemini/handheld/run-008/artifacts/hhv-002/step_0_relevant_regions.png
2026-05-08 14:12:03 | INFO | /Users/tanmaybhuskute/Documents/gifdroid-reproduction/apps/antennapod/llm/ViBR_gemini/handheld/run-008/artifacts/hhv-002/step_0_tmp_stop.png
2026-05-08 14:12:03 | INFO | /Users/tanmaybhuskute/Documents/gifdroid-reproduction/apps/antennapod/llm/ViBR_gemini/handheld/run-008/artifacts/hhv-002/step_0_labeled.png
2026-05-08 14:12:03 | INFO | Region Action Response from Gemini: ```json
2026-05-08 14:12:03 | INFO | {
2026-05-08 14:12:03 | INFO |   "action": "tap",
2026-05-08 14:12:03 | INFO |   "region": 1,
2026-05-08 14:12:03 | INFO |   "description": "Tap the menu icon in the top right corner to add a podcast."
2026-05-08 14:12:03 | INFO | }
2026-05-08 14:12:03 | INFO | ```
2026-05-08 14:12:03 | INFO | 🎯 Using region index: 1 at (1027, 146)
2026-05-08 14:12:03 | INFO | [1] Tap the menu icon in the top right corner to add a podcast. -> tap
2026-05-08 14:12:03 | INFO | ✅ Action executed.
2026-05-08 14:12:03 | INFO | 
2026-05-08 14:12:03 | INFO | 
2026-05-08 14:12:03 | INFO | 📂 Processing segment 1...
2026-05-08 14:12:03 | INFO | Taking screenshot: /sdcard/screenshot-0.png -> /Users/tanmaybhuskute/Documents/gifdroid-reproduction/apps/antennapod/llm/ViBR_gemini/handheld/run-008/artifacts/hhv-002/step_1_screenshot-0.png
2026-05-08 14:12:03 | INFO | 🔍 Annotated DINO output saved to /Users/tanmaybhuskute/Documents/gifdroid-reproduction/apps/antennapod/llm/ViBR_gemini/handheld/run-008/artifacts/hhv-002/step_1_dino.png
2026-05-08 14:12:03 | INFO | /Users/tanmaybhuskute/Documents/gifdroid-reproduction/apps/antennapod/llm/ViBR_gemini/handheld/run-008/artifacts/hhv-002/step_1_dino.png
2026-05-08 14:12:03 | INFO | /Users/tanmaybhuskute/Documents/gifdroid-reproduction/apps/antennapod/llm/ViBR_gemini/handheld/run-008/artifacts/hhv-002/step_1_tmp_stop.png
2026-05-08 14:12:03 | INFO | Relevant Region Response from Gemini: ```json
2026-05-08 14:12:03 | INFO | {
2026-05-08 14:12:03 | INFO |   "target_regions": [
2026-05-08 14:12:03 | INFO |     1
2026-05-08 14:12:03 | INFO |   ],
2026-05-08 14:12:03 | INFO |   "predicted_action": "tap"
2026-05-08 14:12:03 | INFO | }
2026-05-08 14:12:03 | INFO | ```
2026-05-08 14:12:03 | INFO | 🔍 Relevant regions: {'target_regions': [1], 'predicted_action': 'tap'}
2026-05-08 14:12:03 | INFO | 🧠 GPT selected regions: [1]
2026-05-08 14:12:03 | INFO | ✅ Relevant-only annotation saved to /Users/tanmaybhuskute/Documents/gifdroid-reproduction/apps/antennapod/llm/ViBR_gemini/handheld/run-008/artifacts/hhv-002/step_1_relevant_regions.png
2026-05-08 14:12:03 | INFO | /Users/tanmaybhuskute/Documents/gifdroid-reproduction/apps/antennapod/llm/ViBR_gemini/handheld/run-008/artifacts/hhv-002/step_1_relevant_regions.png
2026-05-08 14:12:03 | INFO | /Users/tanmaybhuskute/Documents/gifdroid-reproduction/apps/antennapod/llm/ViBR_gemini/handheld/run-008/artifacts/hhv-002/step_1_screenshot-0.png
2026-05-08 14:12:03 | INFO | Consistency Response from Gemini: ```json
2026-05-08 14:12:03 | INFO | {
2026-05-08 14:12:03 | INFO |   "same_state": "no",
2026-05-08 14:12:03 | INFO |   "description": "The reference screen is the 'Add podcast' page, which allows searching for and selecting podcasts. The current screen is the 'Subscriptions' page, which displays a list of subscribed podcasts (currently empty) and has a menu for filtering and sorting them. The user needs to take another step (likely tapping the '+' button) to get to a state similar to the reference screen."
2026-05-08 14:12:03 | INFO | }
2026-05-08 14:12:03 | INFO | ```
2026-05-08 14:12:03 | INFO | 🔄 Attempting to align state (try 1/3)...
2026-05-08 14:12:03 | INFO | /Users/tanmaybhuskute/Documents/gifdroid-reproduction/apps/antennapod/llm/ViBR_gemini/handheld/run-008/artifacts/hhv-002/step_1_tmp_start.png
2026-05-08 14:12:03 | INFO | /Users/tanmaybhuskute/Documents/gifdroid-reproduction/apps/antennapod/llm/ViBR_gemini/handheld/run-008/artifacts/hhv-002/step_1_tmp_stop.png
2026-05-08 14:12:03 | INFO | /Users/tanmaybhuskute/Documents/gifdroid-reproduction/apps/antennapod/llm/ViBR_gemini/handheld/run-008/artifacts/hhv-002/step_1_labeled.png
2026-05-08 14:12:03 | INFO | Region Action Response from Gemini: ```json
2026-05-08 14:12:03 | INFO | {
2026-05-08 14:12:03 | INFO |     "action": "tap",
2026-05-08 14:12:03 | INFO |     "region": 4,
2026-05-08 14:12:03 | INFO |     "description": "Tap the plus icon to add a new podcast subscription."
2026-05-08 14:12:03 | INFO | }
2026-05-08 14:12:03 | INFO | ```
2026-05-08 14:12:03 | INFO | 🎯 Recovery using region index: 4 at (748, 545)
2026-05-08 14:12:03 | INFO | [1] Tap the plus icon to add a new podcast subscription. -> tap
2026-05-08 14:12:03 | INFO | Taking screenshot: /sdcard/screenshot-0.png -> /Users/tanmaybhuskute/Documents/gifdroid-reproduction/apps/antennapod/llm/ViBR_gemini/handheld/run-008/artifacts/hhv-002/step_1_screenshot-0.png
2026-05-08 14:12:03 | INFO | /Users/tanmaybhuskute/Documents/gifdroid-reproduction/apps/antennapod/llm/ViBR_gemini/handheld/run-008/artifacts/hhv-002/step_1_tmp_start.png
2026-05-08 14:12:03 | INFO | /Users/tanmaybhuskute/Documents/gifdroid-reproduction/apps/antennapod/llm/ViBR_gemini/handheld/run-008/artifacts/hhv-002/step_1_screenshot-0.png
2026-05-08 14:12:03 | INFO | Consistency Response from Gemini: ```json
2026-05-08 14:12:03 | INFO | {
2026-05-08 14:12:03 | INFO |   "same_state": "no",
2026-05-08 14:12:03 | INFO |   "description": "The reference screen is the 'Add podcast' page, which includes a search bar and a grid of suggested podcasts. The current screen is the 'Subscriptions' page, which is empty and displays a pop-up menu for adjusting the number of columns. These are two completely different screens with different functionalities."
2026-05-08 14:12:03 | INFO | }
2026-05-08 14:12:03 | INFO | ```
2026-05-08 14:12:03 | INFO | 🔄 Attempting to align state (try 2/3)...
2026-05-08 14:12:03 | INFO | /Users/tanmaybhuskute/Documents/gifdroid-reproduction/apps/antennapod/llm/ViBR_gemini/handheld/run-008/artifacts/hhv-002/step_1_tmp_start.png
2026-05-08 14:12:03 | INFO | /Users/tanmaybhuskute/Documents/gifdroid-reproduction/apps/antennapod/llm/ViBR_gemini/handheld/run-008/artifacts/hhv-002/step_1_tmp_stop.png
2026-05-08 14:12:03 | INFO | /Users/tanmaybhuskute/Documents/gifdroid-reproduction/apps/antennapod/llm/ViBR_gemini/handheld/run-008/artifacts/hhv-002/step_1_labeled.png
2026-05-08 14:12:03 | INFO | Region Action Response from Gemini: ```json
2026-05-08 14:12:03 | INFO | {
2026-05-08 14:12:03 | INFO |   "action": "tap",
2026-05-08 14:12:03 | INFO |   "region": 10,
2026-05-08 14:12:03 | INFO |   "description": "Tap the grid icon in the center of the screen. This is likely a button to add the first subscription, which is the necessary step to get to the 'Add podcast' screen from the recording."
2026-05-08 14:12:03 | INFO | }
2026-05-08 14:12:03 | INFO | ```
2026-05-08 14:12:03 | INFO | 🎯 Recovery using region index: 10 at (790, 924)
2026-05-08 14:12:21 | INFO | [1] Tap the grid icon in the center of the screen. This is likely a button to add the first subscription, which is the necessary step to get to the 'Add podcast' screen from the recording. -> tapUserWarning: torch.utils.checkpoint: the use_reentrant parameter should be passed explicitly. Starting in PyTorch 2.9, calling checkpoint without use_reentrant will raise an exception. use_reentrant=False is recommended, but if you need to preserve the current default behavior, you can pass use_reentrant=True. Refer to docs for more details on the differences between the two variants.
2026-05-08 14:12:21 | INFO | UserWarning: None of the inputs have requires_grad=True. Gradients will be None
2026-05-08 14:12:25 | INFO | FutureWarning: `torch.cuda.amp.autocast(args...)` is deprecated. Please use `torch.amp.autocast('cuda', args...)` instead.
2026-05-08 14:14:18 | INFO | 
2026-05-08 14:14:18 | INFO | Taking screenshot: /sdcard/screenshot-0.png -> /Users/tanmaybhuskute/Documents/gifdroid-reproduction/apps/antennapod/llm/ViBR_gemini/handheld/run-008/artifacts/hhv-002/step_1_screenshot-0.png
2026-05-08 14:14:18 | INFO | /Users/tanmaybhuskute/Documents/gifdroid-reproduction/apps/antennapod/llm/ViBR_gemini/handheld/run-008/artifacts/hhv-002/step_1_tmp_start.png
2026-05-08 14:14:18 | INFO | /Users/tanmaybhuskute/Documents/gifdroid-reproduction/apps/antennapod/llm/ViBR_gemini/handheld/run-008/artifacts/hhv-002/step_1_screenshot-0.png
2026-05-08 14:14:18 | INFO | Consistency Response from Gemini: ```json
2026-05-08 14:14:18 | INFO | {
2026-05-08 14:14:18 | INFO |   "same_state": "no",
2026-05-08 14:14:18 | INFO |   "description": "The reference screen is the 'Add podcast' screen, which allows searching for and adding new podcasts. The current screen is the 'Subscriptions' screen, which is empty and prompts the user to add a subscription. These are two different screens with different functionalities."
2026-05-08 14:14:18 | INFO | }
2026-05-08 14:14:18 | INFO | ```
2026-05-08 14:14:18 | INFO | 🔄 Attempting to align state (try 3/3)...
2026-05-08 14:14:18 | INFO | /Users/tanmaybhuskute/Documents/gifdroid-reproduction/apps/antennapod/llm/ViBR_gemini/handheld/run-008/artifacts/hhv-002/step_1_tmp_start.png
2026-05-08 14:14:18 | INFO | /Users/tanmaybhuskute/Documents/gifdroid-reproduction/apps/antennapod/llm/ViBR_gemini/handheld/run-008/artifacts/hhv-002/step_1_tmp_stop.png
2026-05-08 14:14:18 | INFO | /Users/tanmaybhuskute/Documents/gifdroid-reproduction/apps/antennapod/llm/ViBR_gemini/handheld/run-008/artifacts/hhv-002/step_1_labeled.png
2026-05-08 14:14:18 | INFO | Region Action Response from Gemini: ```json
2026-05-08 14:14:18 | INFO | {
2026-05-08 14:14:18 | INFO |     "action": "tap",
2026-05-08 14:14:18 | INFO |     "region": 0,
2026-05-08 14:14:18 | INFO |     "description": "Tap the search icon to initiate a search, which is analogous to tapping the search bar in the original recording."
2026-05-08 14:14:18 | INFO | }
2026-05-08 14:14:18 | INFO | ```
2026-05-08 14:14:18 | INFO | 🎯 Recovery using region index: 0 at (790, 168)
2026-05-08 14:14:18 | INFO | [1] Tap the search icon to initiate a search, which is analogous to tapping the search bar in the original recording. -> tap
2026-05-08 14:14:18 | INFO | Taking screenshot: /sdcard/screenshot-0.png -> /Users/tanmaybhuskute/Documents/gifdroid-reproduction/apps/antennapod/llm/ViBR_gemini/handheld/run-008/artifacts/hhv-002/step_1_screenshot-0.png
2026-05-08 14:14:18 | INFO | /Users/tanmaybhuskute/Documents/gifdroid-reproduction/apps/antennapod/llm/ViBR_gemini/handheld/run-008/artifacts/hhv-002/step_1_tmp_start.png
2026-05-08 14:14:18 | INFO | /Users/tanmaybhuskute/Documents/gifdroid-reproduction/apps/antennapod/llm/ViBR_gemini/handheld/run-008/artifacts/hhv-002/step_1_screenshot-0.png
2026-05-08 14:14:18 | INFO | Consistency Response from Gemini: ```json
2026-05-08 14:14:18 | INFO | {
2026-05-08 14:14:18 | INFO |   "same_state": "no",
2026-05-08 14:14:18 | INFO |   "description": "The reference screen is an 'Add podcast' page with a search bar, podcast suggestions, and other options for adding podcasts. The current screen is a blank search page, likely within the 'Subscriptions' section. The UI elements, context, and available actions are fundamentally different."
2026-05-08 14:14:18 | INFO | }
2026-05-08 14:14:18 | INFO | ```
2026-05-08 14:14:18 | INFO | ⚠️ Skipping action: current GUI state does not match start state.
2026-05-08 14:14:18 | INFO | Mismatch reason: the reference screen is an 'add podcast' page with a search bar, podcast suggestions, and other options for adding podcasts. the current screen is a blank search page, likely within the 'subscriptions' section. the ui elements, context, and available actions are fundamentally different.
2026-05-08 14:14:18 | INFO | 
2026-05-08 14:14:18 | INFO | 📂 Processing segment 2...
2026-05-08 14:14:18 | INFO | Taking screenshot: /sdcard/screenshot-0.png -> /Users/tanmaybhuskute/Documents/gifdroid-reproduction/apps/antennapod/llm/ViBR_gemini/handheld/run-008/artifacts/hhv-002/step_2_screenshot-0.png
2026-05-08 14:14:18 | INFO | 🔍 Annotated DINO output saved to /Users/tanmaybhuskute/Documents/gifdroid-reproduction/apps/antennapod/llm/ViBR_gemini/handheld/run-008/artifacts/hhv-002/step_2_dino.png
2026-05-08 14:14:18 | INFO | /Users/tanmaybhuskute/Documents/gifdroid-reproduction/apps/antennapod/llm/ViBR_gemini/handheld/run-008/artifacts/hhv-002/step_2_dino.png
2026-05-08 14:14:18 | INFO | /Users/tanmaybhuskute/Documents/gifdroid-reproduction/apps/antennapod/llm/ViBR_gemini/handheld/run-008/artifacts/hhv-002/step_2_tmp_stop.png
2026-05-08 14:14:18 | INFO | Relevant Region Response from Gemini: ```json
2026-05-08 14:14:18 | INFO | {
2026-05-08 14:14:18 | INFO |   "target_regions": [
2026-05-08 14:14:18 | INFO |     9
2026-05-08 14:14:18 | INFO |   ],
2026-05-08 14:14:18 | INFO |   "predicted_action": "input_text"
2026-05-08 14:14:18 | INFO | }
2026-05-08 14:14:18 | INFO | ```
2026-05-08 14:14:18 | INFO | 🔍 Relevant regions: {'target_regions': [9], 'predicted_action': 'input_text'}
2026-05-08 14:14:18 | INFO | 🧠 GPT selected regions: [9]
2026-05-08 14:14:18 | INFO | ✅ Relevant-only annotation saved to /Users/tanmaybhuskute/Documents/gifdroid-reproduction/apps/antennapod/llm/ViBR_gemini/handheld/run-008/artifacts/hhv-002/step_2_relevant_regions.png
2026-05-08 14:14:18 | INFO | /Users/tanmaybhuskute/Documents/gifdroid-reproduction/apps/antennapod/llm/ViBR_gemini/handheld/run-008/artifacts/hhv-002/step_2_relevant_regions.png
2026-05-08 14:14:18 | INFO | /Users/tanmaybhuskute/Documents/gifdroid-reproduction/apps/antennapod/llm/ViBR_gemini/handheld/run-008/artifacts/hhv-002/step_2_screenshot-0.png
2026-05-08 14:14:18 | INFO | Consistency Response from Gemini: ```json
2026-05-08 14:14:18 | INFO | {
2026-05-08 14:14:18 | INFO |   "same_state": "no",
2026-05-08 14:14:18 | INFO |   "description": "The reference screen is for \"Add podcast\", as indicated by the title. The current screen is a general \"Search\" page. The context and purpose of the two screens are different, even though both contain a search input field."
2026-05-08 14:14:18 | INFO | }
2026-05-08 14:14:18 | INFO | ```
2026-05-08 14:14:18 | INFO | 🔄 Attempting to align state (try 1/3)...
2026-05-08 14:14:18 | INFO | /Users/tanmaybhuskute/Documents/gifdroid-reproduction/apps/antennapod/llm/ViBR_gemini/handheld/run-008/artifacts/hhv-002/step_2_tmp_start.png
2026-05-08 14:14:18 | INFO | /Users/tanmaybhuskute/Documents/gifdroid-reproduction/apps/antennapod/llm/ViBR_gemini/handheld/run-008/artifacts/hhv-002/step_2_tmp_stop.png
2026-05-08 14:14:18 | INFO | /Users/tanmaybhuskute/Documents/gifdroid-reproduction/apps/antennapod/llm/ViBR_gemini/handheld/run-008/artifacts/hhv-002/step_2_labeled.png
2026-05-08 14:14:18 | INFO | Region Action Response from Gemini: ```json
2026-05-08 14:14:18 | INFO | {
2026-05-08 14:14:18 | INFO |   "action": "input_text",
2026-05-08 14:14:18 | INFO |   "text": "The Daily",
2026-05-08 14:14:18 | INFO |   "description": "Type 'The Daily' into the search bar."
2026-05-08 14:14:18 | INFO | }
2026-05-08 14:14:18 | INFO | ```
2026-05-08 14:14:18 | INFO | [1] Type 'The Daily' into the search bar. -> input_text
2026-05-08 14:14:18 | INFO | Taking screenshot: /sdcard/screenshot-0.png -> /Users/tanmaybhuskute/Documents/gifdroid-reproduction/apps/antennapod/llm/ViBR_gemini/handheld/run-008/artifacts/hhv-002/step_2_screenshot-0.png
2026-05-08 14:14:18 | INFO | /Users/tanmaybhuskute/Documents/gifdroid-reproduction/apps/antennapod/llm/ViBR_gemini/handheld/run-008/artifacts/hhv-002/step_2_tmp_start.png
2026-05-08 14:14:18 | INFO | /Users/tanmaybhuskute/Documents/gifdroid-reproduction/apps/antennapod/llm/ViBR_gemini/handheld/run-008/artifacts/hhv-002/step_2_screenshot-0.png
2026-05-08 14:14:18 | INFO | Consistency Response from Gemini: ```json
2026-05-08 14:14:18 | INFO | {
2026-05-08 14:14:18 | INFO |   "same_state": "no",
2026-05-08 14:14:18 | INFO |   "description": "The reference image shows the initial 'Add podcast' screen, which is a pre-search state. The current image shows the results of a search for 'The Daily', which is a post-search state. These are two different functional states in the user flow."
2026-05-08 14:14:18 | INFO | }
2026-05-08 14:14:18 | INFO | ```
2026-05-08 14:14:18 | INFO | 🔄 Attempting to align state (try 2/3)...
2026-05-08 14:14:18 | INFO | /Users/tanmaybhuskute/Documents/gifdroid-reproduction/apps/antennapod/llm/ViBR_gemini/handheld/run-008/artifacts/hhv-002/step_2_tmp_start.png
2026-05-08 14:14:18 | INFO | /Users/tanmaybhuskute/Documents/gifdroid-reproduction/apps/antennapod/llm/ViBR_gemini/handheld/run-008/artifacts/hhv-002/step_2_tmp_stop.png
2026-05-08 14:14:18 | INFO | /Users/tanmaybhuskute/Documents/gifdroid-reproduction/apps/antennapod/llm/ViBR_gemini/handheld/run-008/artifacts/hhv-002/step_2_labeled.png
2026-05-08 14:14:18 | INFO | Region Action Response from Gemini: ```json
2026-05-08 14:14:18 | INFO | {
2026-05-08 14:14:18 | INFO |   "action": "input_text",
2026-05-08 14:14:18 | INFO |   "text": "The Daily",
2026-05-08 14:14:18 | INFO |   "description": "Type 'The Daily' into the search field."
2026-05-08 14:14:18 | INFO | }
2026-05-08 14:14:18 | INFO | ```
2026-05-08 14:14:18 | INFO | [1] Type 'The Daily' into the search field. -> input_text
2026-05-08 14:14:18 | INFO | Taking screenshot: /sdcard/screenshot-0.png -> /Users/tanmaybhuskute/Documents/gifdroid-reproduction/apps/antennapod/llm/ViBR_gemini/handheld/run-008/artifacts/hhv-002/step_2_screenshot-0.png
2026-05-08 14:14:18 | INFO | /Users/tanmaybhuskute/Documents/gifdroid-reproduction/apps/antennapod/llm/ViBR_gemini/handheld/run-008/artifacts/hhv-002/step_2_tmp_start.png
2026-05-08 14:14:18 | INFO | /Users/tanmaybhuskute/Documents/gifdroid-reproduction/apps/antennapod/llm/ViBR_gemini/handheld/run-008/artifacts/hhv-002/step_2_screenshot-0.png
2026-05-08 14:14:18 | INFO | Consistency Response from Gemini: ```json
2026-05-08 14:14:18 | INFO | {
2026-05-08 14:14:18 | INFO |   "same_state": "no",
2026-05-08 14:14:18 | INFO |   "description": "The reference image shows the initial 'Add podcast' screen, which is a starting point for searching. The current image shows the result of a search that has already been performed and yielded no results. These are two different states in the search workflow."
2026-05-08 14:14:18 | INFO | }
2026-05-08 14:14:18 | INFO | ```
2026-05-08 14:14:18 | INFO | 🔄 Attempting to align state (try 3/3)...
2026-05-08 14:14:18 | INFO | /Users/tanmaybhuskute/Documents/gifdroid-reproduction/apps/antennapod/llm/ViBR_gemini/handheld/run-008/artifacts/hhv-002/step_2_tmp_start.png
2026-05-08 14:14:18 | INFO | /Users/tanmaybhuskute/Documents/gifdroid-reproduction/apps/antennapod/llm/ViBR_gemini/handheld/run-008/artifacts/hhv-002/step_2_tmp_stop.png
2026-05-08 14:14:18 | INFO | /Users/tanmaybhuskute/Documents/gifdroid-reproduction/apps/antennapod/llm/ViBR_gemini/handheld/run-008/artifacts/hhv-002/step_2_labeled.png
2026-05-08 14:14:18 | INFO | Region Action Response from Gemini: ```json
2026-05-08 14:14:18 | INFO | {
2026-05-08 14:14:18 | INFO |   "action": "input_text",
2026-05-08 14:14:18 | INFO |   "text": "The Daily",
2026-05-08 14:14:18 | INFO |   "description": "Type 'The Daily' into the search bar."
2026-05-08 14:14:18 | INFO | }
2026-05-08 14:14:18 | INFO | ```
2026-05-08 14:14:18 | INFO | [1] Type 'The Daily' into the search bar. -> input_text
2026-05-08 14:14:18 | INFO | Taking screenshot: /sdcard/screenshot-0.png -> /Users/tanmaybhuskute/Documents/gifdroid-reproduction/apps/antennapod/llm/ViBR_gemini/handheld/run-008/artifacts/hhv-002/step_2_screenshot-0.png
2026-05-08 14:14:18 | INFO | /Users/tanmaybhuskute/Documents/gifdroid-reproduction/apps/antennapod/llm/ViBR_gemini/handheld/run-008/artifacts/hhv-002/step_2_tmp_start.png
2026-05-08 14:14:18 | INFO | /Users/tanmaybhuskute/Documents/gifdroid-reproduction/apps/antennapod/llm/ViBR_gemini/handheld/run-008/artifacts/hhv-002/step_2_screenshot-0.png
2026-05-08 14:14:18 | INFO | Consistency Response from Gemini: ```json
2026-05-08 14:14:18 | INFO | {
2026-05-08 14:14:18 | INFO |   "same_state": "no",
2026-05-08 14:14:18 | INFO |   "description": "The reference image shows the initial 'Add podcast' screen, which is a starting point for a search. The current image shows a 'No results found' screen after a specific search has already been performed. These are two different functional states in the search workflow."
2026-05-08 14:14:18 | INFO | }
2026-05-08 14:14:18 | INFO | ```
2026-05-08 14:14:18 | INFO | ⚠️ Skipping action: current GUI state does not match start state.
2026-05-08 14:14:18 | INFO | Mismatch reason: the reference image shows the initial 'add podcast' screen, which is a starting point for a search. the current image shows a 'no results found' screen after a specific search has already been performed. these are two different functional states in the search workflow.
2026-05-08 14:14:18 | INFO | 
2026-05-08 14:14:18 | INFO | 📂 Processing segment 3...
2026-05-08 14:14:18 | INFO | Taking screenshot: /sdcard/screenshot-0.png -> /Users/tanmaybhuskute/Documents/gifdroid-reproduction/apps/antennapod/llm/ViBR_gemini/handheld/run-008/artifacts/hhv-002/step_3_screenshot-0.png
2026-05-08 14:14:18 | INFO | 🔍 Annotated DINO output saved to /Users/tanmaybhuskute/Documents/gifdroid-reproduction/apps/antennapod/llm/ViBR_gemini/handheld/run-008/artifacts/hhv-002/step_3_dino.png
2026-05-08 14:14:18 | INFO | /Users/tanmaybhuskute/Documents/gifdroid-reproduction/apps/antennapod/llm/ViBR_gemini/handheld/run-008/artifacts/hhv-002/step_3_dino.png
2026-05-08 14:14:18 | INFO | /Users/tanmaybhuskute/Documents/gifdroid-reproduction/apps/antennapod/llm/ViBR_gemini/handheld/run-008/artifacts/hhv-002/step_3_tmp_stop.png
2026-05-08 14:14:18 | INFO | Relevant Region Response from Gemini: ```json
2026-05-08 14:14:18 | INFO | {
2026-05-08 14:14:18 | INFO |   "target_regions": [
2026-05-08 14:14:18 | INFO |     10
2026-05-08 14:14:18 | INFO |   ],
2026-05-08 14:14:18 | INFO |   "predicted_action": "tap"
2026-05-08 14:14:18 | INFO | }
2026-05-08 14:14:18 | INFO | ```
2026-05-08 14:14:18 | INFO | 🔍 Relevant regions: {'target_regions': [10], 'predicted_action': 'tap'}
2026-05-08 14:14:18 | INFO | 🧠 GPT selected regions: [10]
2026-05-08 14:14:18 | INFO | ✅ Relevant-only annotation saved to /Users/tanmaybhuskute/Documents/gifdroid-reproduction/apps/antennapod/llm/ViBR_gemini/handheld/run-008/artifacts/hhv-002/step_3_relevant_regions.png
2026-05-08 14:14:18 | INFO | /Users/tanmaybhuskute/Documents/gifdroid-reproduction/apps/antennapod/llm/ViBR_gemini/handheld/run-008/artifacts/hhv-002/step_3_relevant_regions.png
2026-05-08 14:14:18 | INFO | /Users/tanmaybhuskute/Documents/gifdroid-reproduction/apps/antennapod/llm/ViBR_gemini/handheld/run-008/artifacts/hhv-002/step_3_screenshot-0.png
2026-05-08 14:14:18 | INFO | Consistency Response from Gemini: ```json
2026-05-08 14:14:18 | INFO | {
2026-05-08 14:14:18 | INFO |   "same_state": "no",
2026-05-08 14:14:18 | INFO |   "description": "The reference screen displays the details of 'The Daily' podcast, allowing the user to subscribe or view episodes. The current screen shows a 'No results were found' message for a search. The podcast from the reference screen is not present, so the same actions cannot be performed."
2026-05-08 14:14:18 | INFO | }
2026-05-08 14:14:18 | INFO | ```
2026-05-08 14:14:18 | INFO | 🔄 Attempting to align state (try 1/3)...
2026-05-08 14:14:18 | INFO | /Users/tanmaybhuskute/Documents/gifdroid-reproduction/apps/antennapod/llm/ViBR_gemini/handheld/run-008/artifacts/hhv-002/step_3_tmp_start.png
2026-05-08 14:14:18 | INFO | /Users/tanmaybhuskute/Documents/gifdroid-reproduction/apps/antennapod/llm/ViBR_gemini/handheld/run-008/artifacts/hhv-002/step_3_tmp_stop.png
2026-05-08 14:14:18 | INFO | /Users/tanmaybhuskute/Documents/gifdroid-reproduction/apps/antennapod/llm/ViBR_gemini/handheld/run-008/artifacts/hhv-002/step_3_labeled.png
2026-05-08 14:14:18 | INFO | Region Action Response from Gemini: ```json
2026-05-08 14:14:18 | INFO | {
2026-05-08 14:14:18 | INFO |   "action": "tap",
2026-05-08 14:14:18 | INFO |   "region": 3,
2026-05-08 14:14:18 | INFO |   "description": "Tap the 'Search online' button."
2026-05-08 14:14:18 | INFO | }
2026-05-08 14:14:18 | INFO | ```
2026-05-08 14:14:18 | INFO | 🎯 Recovery using region index: 3 at (220, 305)
2026-05-08 14:14:18 | INFO | [1] Tap the 'Search online' button. -> tap
2026-05-08 14:14:18 | INFO | Taking screenshot: /sdcard/screenshot-0.png -> /Users/tanmaybhuskute/Documents/gifdroid-reproduction/apps/antennapod/llm/ViBR_gemini/handheld/run-008/artifacts/hhv-002/step_3_screenshot-0.png
2026-05-08 14:14:18 | INFO | /Users/tanmaybhuskute/Documents/gifdroid-reproduction/apps/antennapod/llm/ViBR_gemini/handheld/run-008/artifacts/hhv-002/step_3_tmp_start.png
2026-05-08 14:14:18 | INFO | /Users/tanmaybhuskute/Documents/gifdroid-reproduction/apps/antennapod/llm/ViBR_gemini/handheld/run-008/artifacts/hhv-002/step_3_screenshot-0.png
2026-05-08 14:14:18 | INFO | Consistency Response from Gemini: ```json
2026-05-08 14:14:18 | INFO | {
2026-05-08 14:14:18 | INFO |   "same_state": "no",
2026-05-08 14:14:18 | INFO |   "description": "The reference screen shows the details and episode list for the podcast \"The Daily\". The current screen shows a \"No results were found\" message for a different, garbled search query. The two screens are functionally different."
2026-05-08 14:14:18 | INFO | }
2026-05-08 14:14:18 | INFO | ```
2026-05-08 14:14:18 | INFO | 🔄 Attempting to align state (try 2/3)...
2026-05-08 14:14:18 | INFO | /Users/tanmaybhuskute/Documents/gifdroid-reproduction/apps/antennapod/llm/ViBR_gemini/handheld/run-008/artifacts/hhv-002/step_3_tmp_start.png
2026-05-08 14:14:18 | INFO | /Users/tanmaybhuskute/Documents/gifdroid-reproduction/apps/antennapod/llm/ViBR_gemini/handheld/run-008/artifacts/hhv-002/step_3_tmp_stop.png
2026-05-08 14:14:18 | INFO | /Users/tanmaybhuskute/Documents/gifdroid-reproduction/apps/antennapod/llm/ViBR_gemini/handheld/run-008/artifacts/hhv-002/step_3_labeled.png
2026-05-08 14:14:18 | INFO | Region Action Response from Gemini: ```json
2026-05-08 14:14:18 | INFO | {
2026-05-08 14:14:18 | INFO |   "action": "tap",
2026-05-08 14:14:18 | INFO |   "region": 2,
2026-05-08 14:14:18 | INFO |   "description": "Tap the 'x' button to clear the incorrect search query."
2026-05-08 14:14:18 | INFO | }
2026-05-08 14:14:18 | INFO | ```
2026-05-08 14:14:18 | INFO | 🎯 Recovery using region index: 2 at (1006, 147)
2026-05-08 14:14:18 | INFO | [1] Tap the 'x' button to clear the incorrect search query. -> tap
2026-05-08 14:14:18 | INFO | Taking screenshot: /sdcard/screenshot-0.png -> /Users/tanmaybhuskute/Documents/gifdroid-reproduction/apps/antennapod/llm/ViBR_gemini/handheld/run-008/artifacts/hhv-002/step_3_screenshot-0.png
2026-05-08 14:14:18 | INFO | /Users/tanmaybhuskute/Documents/gifdroid-reproduction/apps/antennapod/llm/ViBR_gemini/handheld/run-008/artifacts/hhv-002/step_3_tmp_start.png
2026-05-08 14:14:18 | INFO | /Users/tanmaybhuskute/Documents/gifdroid-reproduction/apps/antennapod/llm/ViBR_gemini/handheld/run-008/artifacts/hhv-002/step_3_screenshot-0.png
2026-05-08 14:14:18 | INFO | Consistency Response from Gemini: ```json
2026-05-08 14:14:18 | INFO | {
2026-05-08 14:14:18 | INFO |   "same_state": "no",
2026-05-08 14:14:18 | INFO |   "description": "The reference screen displays the details of a specific podcast ('The Daily'), showing its description, a subscribe button, and a list of episodes. The current screen is a search results page indicating that no results were found for a search query. These are two different functional states."
2026-05-08 14:14:18 | INFO | }
2026-05-08 14:14:18 | INFO | ```
2026-05-08 14:14:18 | INFO | 🔄 Attempting to align state (try 3/3)...
2026-05-08 14:14:18 | INFO | /Users/tanmaybhuskute/Documents/gifdroid-reproduction/apps/antennapod/llm/ViBR_gemini/handheld/run-008/artifacts/hhv-002/step_3_tmp_start.png
2026-05-08 14:14:18 | INFO | /Users/tanmaybhuskute/Documents/gifdroid-reproduction/apps/antennapod/llm/ViBR_gemini/handheld/run-008/artifacts/hhv-002/step_3_tmp_stop.png
2026-05-08 14:14:18 | INFO | /Users/tanmaybhuskute/Documents/gifdroid-reproduction/apps/antennapod/llm/ViBR_gemini/handheld/run-008/artifacts/hhv-002/step_3_labeled.png
2026-05-08 14:14:18 | INFO | Region Action Response from Gemini: ```json
2026-05-08 14:14:18 | INFO | {
2026-05-08 14:14:18 | INFO |   "action": "tap",
2026-05-08 14:14:18 | INFO |   "region": 1,
2026-05-08 14:14:18 | INFO |   "description": "Tap the search bar to edit the search query."
2026-05-08 14:14:18 | INFO | }
2026-05-08 14:14:18 | INFO | ```
2026-05-08 14:14:18 | INFO | 🎯 Recovery using region index: 1 at (613, 146)
2026-05-08 14:14:18 | INFO | [1] Tap the search bar to edit the search query. -> tap
2026-05-08 14:14:18 | INFO | Taking screenshot: /sdcard/screenshot-0.png -> /Users/tanmaybhuskute/Documents/gifdroid-reproduction/apps/antennapod/llm/ViBR_gemini/handheld/run-008/artifacts/hhv-002/step_3_screenshot-0.png
2026-05-08 14:14:18 | INFO | /Users/tanmaybhuskute/Documents/gifdroid-reproduction/apps/antennapod/llm/ViBR_gemini/handheld/run-008/artifacts/hhv-002/step_3_tmp_start.png
2026-05-08 14:14:18 | INFO | /Users/tanmaybhuskute/Documents/gifdroid-reproduction/apps/antennapod/llm/ViBR_gemini/handheld/run-008/artifacts/hhv-002/step_3_screenshot-0.png
2026-05-08 14:14:18 | INFO | Consistency Response from Gemini: ```json
2026-05-08 14:14:18 | INFO | {
2026-05-08 14:14:18 | INFO |   "same_state": "no",
2026-05-08 14:14:18 | INFO |   "description": "The reference screen displays the details of a specific podcast ('The Daily'), including a subscribe button and a list of episodes. The current screen shows a 'No results were found' message after a search. These are two different functional states."
2026-05-08 14:14:18 | INFO | }
2026-05-08 14:14:18 | INFO | ```
2026-05-08 14:14:18 | INFO | ⚠️ Skipping action: current GUI state does not match start state.
2026-05-08 14:14:18 | INFO | Mismatch reason: the reference screen displays the details of a specific podcast ('the daily'), including a subscribe button and a list of episodes. the current screen shows a 'no results were found' message after a search. these are two different functional states.
2026-05-08 14:14:18 | INFO | ✅ Video processing completed.
2026-05-08 14:14:18 | INFO | 📝 Summary saved to /Users/tanmaybhuskute/Documents/gifdroid-reproduction/apps/antennapod/llm/ViBR_gemini/handheld/run-008/artifacts/hhv-002/memory.md
2026-05-08 14:14:20 | INFO | ========================================================================
RUN SUMMARY
  App         : antennapod
  Video type  : handheld
  Status      : success
  Scenes      : 4/4
  Actions     : unknown=4
  LLM calls   : action_inference=11  region_detection=4  state_comparison=14
  LLM latency : min=7.7s  max=136.4s  avg=19.9s  total=577.7s
  Tokens used : prompt=28,312  output=1,669  total=29,981
  Wall time   : 13m 41s
========================================================================

```
