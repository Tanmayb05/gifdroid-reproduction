# ViBR Run Log

**Status**: SUCCESS

## Full Log

```
2026-05-08 16:51:14 | INFO | === src_vibr.2026-05-08T20-51-14__run-001__pipeline__started ===
2026-05-08 16:51:14 | INFO | Starting ViBR run
2026-05-08 16:51:14 | INFO | App: batterytemperaturedisplay
2026-05-08 16:51:14 | INFO | Video: /Users/tanmaybhuskute/Documents/gifdroid-reproduction/apps/batterytemperaturedisplay/videos/hhv-001.mp4
2026-05-08 16:51:14 | INFO | Algorithm: clip
2026-05-08 16:51:14 | INFO | LLM: gemini (gemini-2.5-pro)
2026-05-08 16:51:14 | INFO | Output: /Users/tanmaybhuskute/Documents/gifdroid-reproduction/apps/batterytemperaturedisplay/llm/ViBR_gemini/handheld/run-001
2026-05-08 16:51:19 | INFO | FutureWarning: Importing from timm.models.layers is deprecated, please import via timm.layers
2026-05-08 16:51:19 | INFO | UserWarning: Failed to load custom C++ ops. Running on CPU mode Only!
2026-05-08 16:51:19 | INFO | UserWarning: torch.meshgrid: in an upcoming release, it will be required to pass the indexing argument. (Triggered internally at /Users/runner/work/pytorch/pytorch/pytorch/aten/src/ATen/native/TensorShape.cpp:4383.)
2026-05-08 16:51:21 | INFO | final text_encoder_type: bert-base-uncased
2026-05-08 16:51:21 | INFO | 
2026-05-08 16:51:21 | INFO | Loading weights:   0%|          | 0/199 [00:00<?, ?it/s]
2026-05-08 16:51:21 | INFO | Loading weights: 100%|██████████| 199/199 [00:00<00:00, 7326.39it/s]
2026-05-08 16:51:21 | INFO | [1mBertModel LOAD REPORT[0m from: bert-base-uncased
2026-05-08 16:51:21 | INFO | Key                                        | Status     |  | 
2026-05-08 16:51:21 | INFO | -------------------------------------------+------------+--+-
2026-05-08 16:51:21 | INFO | cls.predictions.transform.dense.weight     | UNEXPECTED |  | 
2026-05-08 16:51:21 | INFO | cls.seq_relationship.bias                  | UNEXPECTED |  | 
2026-05-08 16:51:21 | INFO | cls.predictions.bias                       | UNEXPECTED |  | 
2026-05-08 16:51:21 | INFO | cls.seq_relationship.weight                | UNEXPECTED |  | 
2026-05-08 16:51:21 | INFO | cls.predictions.transform.LayerNorm.bias   | UNEXPECTED |  | 
2026-05-08 16:51:21 | INFO | cls.predictions.transform.dense.bias       | UNEXPECTED |  | 
2026-05-08 16:51:21 | INFO | cls.predictions.transform.LayerNorm.weight | UNEXPECTED |  | 
2026-05-08 16:51:21 | INFO | 
2026-05-08 16:51:21 | INFO | Notes:
2026-05-08 16:51:21 | INFO | - UNEXPECTED:	can be ignored when loading from different task/architecture; not ok if you expect identical arch.
2026-05-08 16:51:36 | INFO | 🔹 Starting video processing (algorithm=clip, llm=gemini, model=gemini-2.5-pro)...
2026-05-08 16:51:36 | INFO | Initializing ADB device controller...
2026-05-08 16:51:36 | INFO | 📱 Preparing device for app: batterytemperaturedisplay
2026-05-08 16:51:36 | INFO | 🏠 Going to home screen...
2026-05-08 16:51:36 | INFO | 🚀 Opening app 'batterytemperaturedisplay' with command: am start -n barilyuk.batterytemperature/.MainActivity
2026-05-08 16:51:36 | INFO | ✅ App 'batterytemperaturedisplay' opened and ready
2026-05-08 16:51:36 | INFO | Taking screenshot: /sdcard/screenshot-0.png -> /Users/tanmaybhuskute/Documents/gifdroid-reproduction/apps/batterytemperaturedisplay/llm/ViBR_gemini/handheld/run-001/artifacts/hhv-001/screenshot-0.png
2026-05-08 16:51:36 | INFO | Reading frames from video...
2026-05-08 16:51:36 | INFO | Reading frame:  2
2026-05-08 16:51:36 | INFO | Reading frame:  3
2026-05-08 16:51:36 | INFO | Reading frame:  4
2026-05-08 16:51:36 | INFO | Reading frame:  5
2026-05-08 16:51:36 | INFO | Reading frame:  6
2026-05-08 16:51:36 | INFO | Reading frame:  7
2026-05-08 16:51:36 | INFO | Reading frame:  8
2026-05-08 16:51:36 | INFO | Reading frame:  9
2026-05-08 16:51:36 | INFO | Reading frame:  10
2026-05-08 16:51:36 | INFO | Reading frame:  11
2026-05-08 16:51:36 | INFO | Reading frame:  12
2026-05-08 16:51:36 | INFO | Reading frame:  13
2026-05-08 16:51:36 | INFO | Reading frame:  14
2026-05-08 16:51:36 | INFO | Reading frame:  15
2026-05-08 16:51:36 | INFO | Reading frame:  16
2026-05-08 16:51:36 | INFO | Reading frame:  17
2026-05-08 16:51:36 | INFO | Reading frame:  18
2026-05-08 16:51:36 | INFO | Reading frame:  19
2026-05-08 16:51:36 | INFO | Reading frame:  20
2026-05-08 16:51:36 | INFO | Reading frame:  21
2026-05-08 16:51:36 | INFO | Reading frame:  22
2026-05-08 16:51:36 | INFO | Reading frame:  23
2026-05-08 16:51:36 | INFO | Reading frame:  24
2026-05-08 16:51:36 | INFO | Reading frame:  25
2026-05-08 16:51:36 | INFO | Reading frame:  26
2026-05-08 16:51:36 | INFO | Reading frame:  27
2026-05-08 16:51:36 | INFO | Reading frame:  28
2026-05-08 16:51:36 | INFO | Reading frame:  29
2026-05-08 16:51:36 | INFO | Reading frame:  30
2026-05-08 16:51:36 | INFO | Reading frame:  31
2026-05-08 16:51:36 | INFO | Reading frame:  32
2026-05-08 16:51:36 | INFO | Reading frame:  33
2026-05-08 16:51:36 | INFO | Reading frame:  34
2026-05-08 16:51:36 | INFO | Reading frame:  35
2026-05-08 16:51:36 | INFO | Reading frame:  36
2026-05-08 16:51:36 | INFO | Reading frame:  37
2026-05-08 16:51:36 | INFO | Reading frame:  38
2026-05-08 16:51:36 | INFO | Reading frame:  39
2026-05-08 16:51:36 | INFO | Reading frame:  40
2026-05-08 16:51:36 | INFO | Reading frame:  41
2026-05-08 16:51:36 | INFO | Reading frame:  42
2026-05-08 16:51:36 | INFO | Reading frame:  43
2026-05-08 16:51:36 | INFO | Reading frame:  44
2026-05-08 16:51:36 | INFO | Reading frame:  45
2026-05-08 16:51:36 | INFO | Reading frame:  46
2026-05-08 16:51:36 | INFO | Reading frame:  47
2026-05-08 16:51:36 | INFO | Reading frame:  48
2026-05-08 16:51:36 | INFO | Reading frame:  49
2026-05-08 16:51:36 | INFO | Reading frame:  50
2026-05-08 16:51:36 | INFO | Reading frame:  51
2026-05-08 16:51:36 | INFO | Reading frame:  52
2026-05-08 16:51:36 | INFO | Reading frame:  53
2026-05-08 16:51:36 | INFO | Reading frame:  54
2026-05-08 16:51:36 | INFO | Reading frame:  55
2026-05-08 16:51:36 | INFO | Reading frame:  56
2026-05-08 16:51:36 | INFO | Reading frame:  57
2026-05-08 16:51:36 | INFO | Reading frame:  58
2026-05-08 16:51:36 | INFO | Reading frame:  59
2026-05-08 16:51:36 | INFO | Reading frame:  60
2026-05-08 16:51:36 | INFO | Reading frame:  61
2026-05-08 16:51:36 | INFO | Reading frame:  62
2026-05-08 16:51:36 | INFO | Reading frame:  63
2026-05-08 16:51:36 | INFO | Reading frame:  64
2026-05-08 16:51:36 | INFO | Reading frame:  65
2026-05-08 16:51:36 | INFO | Reading frame:  66
2026-05-08 16:51:36 | INFO | Reading frame:  67
2026-05-08 16:51:36 | INFO | Reading frame:  68
2026-05-08 16:51:36 | INFO | Reading frame:  69
2026-05-08 16:51:36 | INFO | Reading frame:  70
2026-05-08 16:51:36 | INFO | Reading frame:  71
2026-05-08 16:51:36 | INFO | Reading frame:  72
2026-05-08 16:51:36 | INFO | Reading frame:  73
2026-05-08 16:51:36 | INFO | Reading frame:  74
2026-05-08 16:51:36 | INFO | Reading frame:  75
2026-05-08 16:51:36 | INFO | Reading frame:  76
2026-05-08 16:51:36 | INFO | Reading frame:  77
2026-05-08 16:51:36 | INFO | Reading frame:  78
2026-05-08 16:51:36 | INFO | Reading frame:  79
2026-05-08 16:51:36 | INFO | Reading frame:  80
2026-05-08 16:51:36 | INFO | Reading frame:  81
2026-05-08 16:51:36 | INFO | Reading frame:  82
2026-05-08 16:51:36 | INFO | Reading frame:  83
2026-05-08 16:51:36 | INFO | Reading frame:  84
2026-05-08 16:51:36 | INFO | Reading frame:  85
2026-05-08 16:51:36 | INFO | Reading frame:  86
2026-05-08 16:51:36 | INFO | Reading frame:  87
2026-05-08 16:51:36 | INFO | Reading frame:  88
2026-05-08 16:51:36 | INFO | Reading frame:  89
2026-05-08 16:51:36 | INFO | Reading frame:  90
2026-05-08 16:51:36 | INFO | Reading frame:  91
2026-05-08 16:51:36 | INFO | Reading frame:  92
2026-05-08 16:51:36 | INFO | Reading frame:  93
2026-05-08 16:51:36 | INFO | Reading frame:  94
2026-05-08 16:51:36 | INFO | Reading frame:  95
2026-05-08 16:51:36 | INFO | Reading frame:  96
2026-05-08 16:51:36 | INFO | Reading frame:  97
2026-05-08 16:51:36 | INFO | Reading frame:  98
2026-05-08 16:51:36 | INFO | Reading frame:  99
2026-05-08 16:51:36 | INFO | Reading frame:  100
2026-05-08 16:51:36 | INFO | Reading frame:  101
2026-05-08 16:51:36 | INFO | Reading frame:  102
2026-05-08 16:51:36 | INFO | Reading frame:  103
2026-05-08 16:51:36 | INFO | Reading frame:  104
2026-05-08 16:51:36 | INFO | Reading frame:  105
2026-05-08 16:51:36 | INFO | Reading frame:  106
2026-05-08 16:51:36 | INFO | Reading frame:  107
2026-05-08 16:51:36 | INFO | Reading frame:  108
2026-05-08 16:51:36 | INFO | Reading frame:  109
2026-05-08 16:51:36 | INFO | Reading frame:  110
2026-05-08 16:51:36 | INFO | Reading frame:  111
2026-05-08 16:51:36 | INFO | Reading frame:  112
2026-05-08 16:51:36 | INFO | Reading frame:  113
2026-05-08 16:51:36 | INFO | Reading frame:  114
2026-05-08 16:51:36 | INFO | Reading frame:  115
2026-05-08 16:51:36 | INFO | Reading frame:  116
2026-05-08 16:51:36 | INFO | Reading frame:  117
2026-05-08 16:51:36 | INFO | Reading frame:  118
2026-05-08 16:51:36 | INFO | Reading frame:  119
2026-05-08 16:51:36 | INFO | Reading frame:  120
2026-05-08 16:51:36 | INFO | Reading frame:  121
2026-05-08 16:51:36 | INFO | Reading frame:  122
2026-05-08 16:51:36 | INFO | Reading frame:  123
2026-05-08 16:51:36 | INFO | Reading frame:  124
2026-05-08 16:51:36 | INFO | Reading frame:  125
2026-05-08 16:51:36 | INFO | Reading frame:  126
2026-05-08 16:51:36 | INFO | Reading frame:  127
2026-05-08 16:51:36 | INFO | Reading frame:  128
2026-05-08 16:51:36 | INFO | Reading frame:  129
2026-05-08 16:51:36 | INFO | Reading frame:  130
2026-05-08 16:51:36 | INFO | Reading frame:  131
2026-05-08 16:51:36 | INFO | Reading frame:  132
2026-05-08 16:51:36 | INFO | Reading frame:  133
2026-05-08 16:51:36 | INFO | Reading frame:  134
2026-05-08 16:51:36 | INFO | Reading frame:  135
2026-05-08 16:51:36 | INFO | Reading frame:  136
2026-05-08 16:51:36 | INFO | Reading frame:  137
2026-05-08 16:51:36 | INFO | Reading frame:  138
2026-05-08 16:51:36 | INFO | Reading frame:  139
2026-05-08 16:51:36 | INFO | Reading frame:  140
2026-05-08 16:51:36 | INFO | Reading frame:  141
2026-05-08 16:51:36 | INFO | Reading frame:  142
2026-05-08 16:51:36 | INFO | Reading frame:  143
2026-05-08 16:51:36 | INFO | Reading frame:  144
2026-05-08 16:51:36 | INFO | Reading frame:  145
2026-05-08 16:51:36 | INFO | Reading frame:  146
2026-05-08 16:51:36 | INFO | Reading frame:  147
2026-05-08 16:51:36 | INFO | Reading frame:  148
2026-05-08 16:51:36 | INFO | Reading frame:  149
2026-05-08 16:51:36 | INFO | Reading frame:  150
2026-05-08 16:51:36 | INFO | Reading frame:  151
2026-05-08 16:51:36 | INFO | Reading frame:  152
2026-05-08 16:51:36 | INFO | Reading frame:  153
2026-05-08 16:51:36 | INFO | Reading frame:  154
2026-05-08 16:51:36 | INFO | Reading frame:  155
2026-05-08 16:51:36 | INFO | Reading frame:  156
2026-05-08 16:51:36 | INFO | Reading frame:  157
2026-05-08 16:51:36 | INFO | Reading frame:  158
2026-05-08 16:51:36 | INFO | Reading frame:  159
2026-05-08 16:51:36 | INFO | Reading frame:  160
2026-05-08 16:51:36 | INFO | Reading frame:  161
2026-05-08 16:51:36 | INFO | Reading frame:  162
2026-05-08 16:51:36 | INFO | Reading frame:  163
2026-05-08 16:51:36 | INFO | Reading frame:  164
2026-05-08 16:51:36 | INFO | Reading frame:  165
2026-05-08 16:51:36 | INFO | Reading frame:  166
2026-05-08 16:51:36 | INFO | Reading frame:  167
2026-05-08 16:51:36 | INFO | Reading frame:  168
2026-05-08 16:51:36 | INFO | Reading frame:  169
2026-05-08 16:51:36 | INFO | Reading frame:  170
2026-05-08 16:51:36 | INFO | Reading frame:  171
2026-05-08 16:51:36 | INFO | Reading frame:  172
2026-05-08 16:51:36 | INFO | Reading frame:  173
2026-05-08 16:51:36 | INFO | Reading frame:  174
2026-05-08 16:51:36 | INFO | Reading frame:  175
2026-05-08 16:51:36 | INFO | Reading frame:  176
2026-05-08 16:51:36 | INFO | Reading frame:  177
2026-05-08 16:51:36 | INFO | Reading frame:  178
2026-05-08 16:51:36 | INFO | Reading frame:  179
2026-05-08 16:51:36 | INFO | Reading frame:  180
2026-05-08 16:51:36 | INFO | Reading frame:  181
2026-05-08 16:51:36 | INFO | Reading frame:  182
2026-05-08 16:51:36 | INFO | Reading frame:  183
2026-05-08 16:51:36 | INFO | Reading frame:  184
2026-05-08 16:51:36 | INFO | Reading frame:  185
2026-05-08 16:51:36 | INFO | Reading frame:  186
2026-05-08 16:51:36 | INFO | Reading frame:  187
2026-05-08 16:51:36 | INFO | Reading frame:  188
2026-05-08 16:51:36 | INFO | Reading frame:  189
2026-05-08 16:51:36 | INFO | Reading frame:  190
2026-05-08 16:51:36 | INFO | Reading frame:  191
2026-05-08 16:51:36 | INFO | Reading frame:  192
2026-05-08 16:51:36 | INFO | Reading frame:  193
2026-05-08 16:51:36 | INFO | Reading frame:  194
2026-05-08 16:51:36 | INFO | Reading frame:  195
2026-05-08 16:51:36 | INFO | Reading frame:  196
2026-05-08 16:51:36 | INFO | Reading frame:  197
2026-05-08 16:51:36 | INFO | Reading frame:  198
2026-05-08 16:51:36 | INFO | Reading frame:  199
2026-05-08 16:51:36 | INFO | Reading frame:  200
2026-05-08 16:51:36 | INFO | Reading frame:  201
2026-05-08 16:51:36 | INFO | Reading frame:  202
2026-05-08 16:51:36 | INFO | Reading frame:  203
2026-05-08 16:51:36 | INFO | Reading frame:  204
2026-05-08 16:51:36 | INFO | Reading frame:  205
2026-05-08 16:51:36 | INFO | Reading frame:  206
2026-05-08 16:51:36 | INFO | Reading frame:  207
2026-05-08 16:51:36 | INFO | Reading frame:  208
2026-05-08 16:51:36 | INFO | Reading frame:  209
2026-05-08 16:51:36 | INFO | Reading frame:  210
2026-05-08 16:51:36 | INFO | Reading frame:  211
2026-05-08 16:51:36 | INFO | Reading frame:  212
2026-05-08 16:51:36 | INFO | Reading frame:  213
2026-05-08 16:51:36 | INFO | Reading frame:  214
2026-05-08 16:51:36 | INFO | Reading frame:  215
2026-05-08 16:51:36 | INFO | Reading frame:  216
2026-05-08 16:51:36 | INFO | Reading frame:  217
2026-05-08 16:51:36 | INFO | Reading frame:  218
2026-05-08 16:51:36 | INFO | Reading frame:  219
2026-05-08 16:51:36 | INFO | Reading frame:  220
2026-05-08 16:51:36 | INFO | Reading frame:  221
2026-05-08 16:51:36 | INFO | Reading frame:  222
2026-05-08 16:51:36 | INFO | Reading frame:  223
2026-05-08 16:51:36 | INFO | Reading frame:  224
2026-05-08 16:51:36 | INFO | Reading frame:  225
2026-05-08 16:51:36 | INFO | Reading frame:  226
2026-05-08 16:51:36 | INFO | Reading frame:  227
2026-05-08 16:51:36 | INFO | Reading frame:  228
2026-05-08 16:51:36 | INFO | Reading frame:  229
2026-05-08 16:51:36 | INFO | Reading frame:  230
2026-05-08 16:51:36 | INFO | Reading frame:  231
2026-05-08 16:51:36 | INFO | Reading frame:  232
2026-05-08 16:51:36 | INFO | Reading frame:  233
2026-05-08 16:51:36 | INFO | Reading frame:  234
2026-05-08 16:51:36 | INFO | Reading frame:  235
2026-05-08 16:51:36 | INFO | Reading frame:  236
2026-05-08 16:51:36 | INFO | Reading frame:  237
2026-05-08 16:51:36 | INFO | Reading frame:  238
2026-05-08 16:51:36 | INFO | Reading frame:  239
2026-05-08 16:51:36 | INFO | Reading frame:  240
2026-05-08 16:51:36 | INFO | Reading frame:  241
2026-05-08 16:51:36 | INFO | Reading frame:  242
2026-05-08 16:51:36 | INFO | Reading frame:  243
2026-05-08 16:51:36 | INFO | Reading frame:  244
2026-05-08 16:51:36 | INFO | Reading frame:  245
2026-05-08 16:51:36 | INFO | Reading frame:  246
2026-05-08 16:51:36 | INFO | Reading frame:  247
2026-05-08 16:51:36 | INFO | Reading frame:  248
2026-05-08 16:51:36 | INFO | Reading frame:  249
2026-05-08 16:51:36 | INFO | Reading frame:  250
2026-05-08 16:51:36 | INFO | Reading frame:  251
2026-05-08 16:51:36 | INFO | Reading frame:  252
2026-05-08 16:51:36 | INFO | Reading frame:  253
2026-05-08 16:51:36 | INFO | Reading frame:  254
2026-05-08 16:51:36 | INFO | Reading frame:  255
2026-05-08 16:51:36 | INFO | Reading frame:  256
2026-05-08 16:51:36 | INFO | Reading frame:  257
2026-05-08 16:51:36 | INFO | Reading frame:  258
2026-05-08 16:51:36 | INFO | Reading frame:  259
2026-05-08 16:51:36 | INFO | Reading frame:  260
2026-05-08 16:51:36 | INFO | Reading frame:  261
2026-05-08 16:51:36 | INFO | Reading frame:  262
2026-05-08 16:51:36 | INFO | Reading frame:  263
2026-05-08 16:51:36 | INFO | Reading frame:  264
2026-05-08 16:51:36 | INFO | Reading frame:  265
2026-05-08 16:51:36 | INFO | Reading frame:  266
2026-05-08 16:51:36 | INFO | Reading frame:  267
2026-05-08 16:51:36 | INFO | Reading frame:  268
2026-05-08 16:51:36 | INFO | Reading frame:  269
2026-05-08 16:51:36 | INFO | Reading frame:  270
2026-05-08 16:51:36 | INFO | Reading frame:  271
2026-05-08 16:51:36 | INFO | Reading frame:  272
2026-05-08 16:51:36 | INFO | Reading frame:  273
2026-05-08 16:51:36 | INFO | Reading frame:  274
2026-05-08 16:51:36 | INFO | Reading frame:  275
2026-05-08 16:51:36 | INFO | Reading frame:  276
2026-05-08 16:51:36 | INFO | Reading frame:  277
2026-05-08 16:51:36 | INFO | Reading frame:  278
2026-05-08 16:51:36 | INFO | Reading frame:  279
2026-05-08 16:51:36 | INFO | Reading frame:  280
2026-05-08 16:51:36 | INFO | Reading frame:  281
2026-05-08 16:51:36 | INFO | Reading frame:  282
2026-05-08 16:51:36 | INFO | Reading frame:  283
2026-05-08 16:51:36 | INFO | Reading frame:  284
2026-05-08 16:51:36 | INFO | Reading frame:  285
2026-05-08 16:51:36 | INFO | Reading frame:  286
2026-05-08 16:51:36 | INFO | Reading frame:  287
2026-05-08 16:51:36 | INFO | Reading frame:  288
2026-05-08 16:51:36 | INFO | Reading frame:  289
2026-05-08 16:51:36 | INFO | Reading frame:  290
2026-05-08 16:51:36 | INFO | Reading frame:  291
2026-05-08 16:51:36 | INFO | Reading frame:  292
2026-05-08 16:51:36 | INFO | Reading frame:  293
2026-05-08 16:51:36 | INFO | Reading frame:  294
2026-05-08 16:51:36 | INFO | Reading frame:  295
2026-05-08 16:51:36 | INFO | Reading frame:  296
2026-05-08 16:51:36 | INFO | Reading frame:  297
2026-05-08 16:51:36 | INFO | Reading frame:  298
2026-05-08 16:51:36 | INFO | Reading frame:  299
2026-05-08 16:51:36 | INFO | Reading frame:  300
2026-05-08 16:51:36 | INFO | Reading frame:  301
2026-05-08 16:51:36 | INFO | Reading frame:  302
2026-05-08 16:51:36 | INFO | Reading frame:  303
2026-05-08 16:51:36 | INFO | Reading frame:  304
2026-05-08 16:51:36 | INFO | Reading frame:  305
2026-05-08 16:51:36 | INFO | Reading frame:  306
2026-05-08 16:51:36 | INFO | Reading frame:  307
2026-05-08 16:51:36 | INFO | Reading frame:  308
2026-05-08 16:51:36 | INFO | Reading frame:  309
2026-05-08 16:51:36 | INFO | Reading frame:  310
2026-05-08 16:51:36 | INFO | Reading frame:  311
2026-05-08 16:51:36 | INFO | Reading frame:  312
2026-05-08 16:51:36 | INFO | Reading frame:  313
2026-05-08 16:51:36 | INFO | Reading frame:  314
2026-05-08 16:51:36 | INFO | Reading frame:  315
2026-05-08 16:51:36 | INFO | Reading frame:  316
2026-05-08 16:51:36 | INFO | Reading frame:  317
2026-05-08 16:51:36 | INFO | Reading frame:  318
2026-05-08 16:51:36 | INFO | Reading frame:  319
2026-05-08 16:51:36 | INFO | Reading frame:  320
2026-05-08 16:51:36 | INFO | Reading frame:  321
2026-05-08 16:51:36 | INFO | Reading frame:  322
2026-05-08 16:51:36 | INFO | Reading frame:  323
2026-05-08 16:51:36 | INFO | Reading frame:  324
2026-05-08 16:51:36 | INFO | Reading frame:  325
2026-05-08 16:51:36 | INFO | Reading frame:  326
2026-05-08 16:51:36 | INFO | Reading frame:  327
2026-05-08 16:51:36 | INFO | Reading frame:  328
2026-05-08 16:51:36 | INFO | Reading frame:  329
2026-05-08 16:51:36 | INFO | Reading frame:  330
2026-05-08 16:51:36 | INFO | Reading frame:  331
2026-05-08 16:51:36 | INFO | Reading frame:  332
2026-05-08 16:51:36 | INFO | Reading frame:  333
2026-05-08 16:51:36 | INFO | Reading frame:  334
2026-05-08 16:51:36 | INFO | Reading frame:  335
2026-05-08 16:51:36 | INFO | Reading frame:  336
2026-05-08 16:51:36 | INFO | Reading frame:  337
2026-05-08 16:51:36 | INFO | Reading frame:  338
2026-05-08 16:51:36 | INFO | Reading frame:  339
2026-05-08 16:51:36 | INFO | Reading frame:  340
2026-05-08 16:51:36 | INFO | Reading frame:  341
2026-05-08 16:51:36 | INFO | Reading frame:  342
2026-05-08 16:51:36 | INFO | Reading frame:  343
2026-05-08 16:51:36 | INFO | Reading frame:  344
2026-05-08 16:51:36 | INFO | Reading frame:  345
2026-05-08 16:51:36 | INFO | Reading frame:  346
2026-05-08 16:51:36 | INFO | Reading frame:  347
2026-05-08 16:51:36 | INFO | Reading frame:  348
2026-05-08 16:51:36 | INFO | Reading frame:  349
2026-05-08 16:51:36 | INFO | Reading frame:  350
2026-05-08 16:51:36 | INFO | Reading frame:  351
2026-05-08 16:51:36 | INFO | Reading frame:  352
2026-05-08 16:51:36 | INFO | Reading frame:  353
2026-05-08 16:51:36 | INFO | Reading frame:  354
2026-05-08 16:51:36 | INFO | Reading frame:  355
2026-05-08 16:51:36 | INFO | Reading frame:  356
2026-05-08 16:51:36 | INFO | Reading frame:  357
2026-05-08 16:51:36 | INFO | Reading frame:  358
2026-05-08 16:51:36 | INFO | Reading frame:  359
2026-05-08 16:51:36 | INFO | Reading frame:  360
2026-05-08 16:51:36 | INFO | Reading frame:  361
2026-05-08 16:51:36 | INFO | Reading frame:  362
2026-05-08 16:51:36 | INFO | Reading frame:  363
2026-05-08 16:51:36 | INFO | Reading frame:  364
2026-05-08 16:51:36 | INFO | Reading frame:  365
2026-05-08 16:51:36 | INFO | Reading frame:  366
2026-05-08 16:51:36 | INFO | Reading frame:  367
2026-05-08 16:51:36 | INFO | Reading frame:  368
2026-05-08 16:51:36 | INFO | Reading frame:  369
2026-05-08 16:51:36 | INFO | Reading frame:  370
2026-05-08 16:51:36 | INFO | Reading frame:  371
2026-05-08 16:51:36 | INFO | Reading frame:  372
2026-05-08 16:51:36 | INFO | Reading frame:  373
2026-05-08 16:51:36 | INFO | Reading frame:  374
2026-05-08 16:51:36 | INFO | Reading frame:  375
2026-05-08 16:51:36 | INFO | Reading frame:  376
2026-05-08 16:51:36 | INFO | Reading frame:  377
2026-05-08 16:51:36 | INFO | Reading frame:  378
2026-05-08 16:51:36 | INFO | Reading frame:  379
2026-05-08 16:51:36 | INFO | Reading frame:  380
2026-05-08 16:51:36 | INFO | Reading frame:  381
2026-05-08 16:51:36 | INFO | Reading frame:  382
2026-05-08 16:51:36 | INFO | Reading frame:  383
2026-05-08 16:51:36 | INFO | Reading frame:  384
2026-05-08 16:51:36 | INFO | Reading frame:  385
2026-05-08 16:51:39 | INFO | Reading frame: Warning: You are sending unauthenticated requests to the HF Hub. Please set a HF_TOKEN to enable higher rate limits and faster downloads.
2026-05-08 16:51:39 | INFO |  386
2026-05-08 16:51:39 | INFO | Reading frame:  387
2026-05-08 16:51:39 | INFO | Reading frame:  388
2026-05-08 16:51:39 | INFO | Reading frame:  389
2026-05-08 16:51:39 | INFO | Reading frame:  390
2026-05-08 16:51:39 | INFO | Reading frame:  391
2026-05-08 16:51:39 | INFO | Reading frame:  392
2026-05-08 16:51:39 | INFO | Reading frame:  393
2026-05-08 16:51:39 | INFO | Reading frame:  394
2026-05-08 16:51:39 | INFO | Reading frame:  395
2026-05-08 16:51:39 | INFO | Reading frame:  396
2026-05-08 16:51:39 | INFO | Reading frame:  397
2026-05-08 16:51:39 | INFO | Reading frame:  398
2026-05-08 16:51:39 | INFO | Reading frame:  399
2026-05-08 16:51:39 | INFO | Reading frame:  400
2026-05-08 16:51:39 | INFO | Reading frame:  401
2026-05-08 16:51:39 | INFO | Reading frame:  402
2026-05-08 16:51:39 | INFO | Reading frame:  403
2026-05-08 16:51:39 | INFO | Reading frame:  404
2026-05-08 16:51:39 | INFO | Reading frame:  405
2026-05-08 16:51:39 | INFO | Reading frame:  406
2026-05-08 16:51:39 | INFO | Reading frame:  407
2026-05-08 16:51:39 | INFO | Reading frame:  408
2026-05-08 16:51:39 | INFO | Reading frame:  409
2026-05-08 16:51:39 | INFO | Reading frame:  410
2026-05-08 16:51:39 | INFO | Reading frame:  411
2026-05-08 16:51:39 | INFO | Reading frame:  412
2026-05-08 16:51:39 | INFO | Reading frame:  413
2026-05-08 16:51:39 | INFO | Reading frame:  414
2026-05-08 16:51:39 | INFO | Reading frame:  415
2026-05-08 16:51:39 | INFO | Reading frame:  416
2026-05-08 16:51:39 | INFO | Reading frame:  417
2026-05-08 16:51:39 | INFO | Reading frame:  418
2026-05-08 16:51:39 | INFO | Reading frame:  419
2026-05-08 16:51:39 | INFO | Reading frame:  420
2026-05-08 16:51:39 | INFO | Reading frame:  421
2026-05-08 16:51:39 | INFO | Reading frame:  422
2026-05-08 16:51:39 | INFO | Reading frame:  423
2026-05-08 16:51:39 | INFO | Reading frame:  424
2026-05-08 16:51:39 | INFO | Reading frame:  425
2026-05-08 16:51:39 | INFO | Reading frame:  426
2026-05-08 16:51:39 | INFO | Reading frame:  427
2026-05-08 16:51:39 | INFO | Reading frame:  428
2026-05-08 16:51:39 | INFO | Reading frame:  429
2026-05-08 16:51:39 | INFO | Reading frame:  430
2026-05-08 16:51:39 | INFO | Reading frame:  431
2026-05-08 16:51:39 | INFO | Reading frame:  432
2026-05-08 16:51:39 | INFO | Reading frame:  433
2026-05-08 16:51:39 | INFO | Reading frame:  434
2026-05-08 16:51:39 | INFO | Reading frame:  435
2026-05-08 16:51:39 | INFO | Reading frame:  436
2026-05-08 16:51:39 | INFO | Reading frame:  437
2026-05-08 16:51:39 | INFO | Reading frame:  438
2026-05-08 16:51:39 | INFO | Reading frame:  439
2026-05-08 16:51:39 | INFO | Reading frame:  440
2026-05-08 16:51:39 | INFO | Reading frame:  441
2026-05-08 16:51:39 | INFO | Reading frame:  442
2026-05-08 16:51:39 | INFO | Reading frame:  443
2026-05-08 16:51:39 | INFO | Reading frame:  444
2026-05-08 16:51:39 | INFO | Reading frame:  445
2026-05-08 16:51:39 | INFO | Reading frame:  446
2026-05-08 16:51:39 | INFO | Reading frame:  447
2026-05-08 16:51:39 | INFO | Reading frame:  448
2026-05-08 16:51:39 | INFO | Reading frame:  449
2026-05-08 16:51:39 | INFO | Reading frame:  450
2026-05-08 16:51:39 | INFO | Reading frame:  451
2026-05-08 16:51:39 | INFO | Reading frame:  452
2026-05-08 16:51:39 | INFO | Reading frame:  453
2026-05-08 16:51:39 | INFO | Reading frame:  454
2026-05-08 16:51:39 | INFO | Reading frame:  455
2026-05-08 16:51:39 | INFO | Reading frame:  456
2026-05-08 16:51:39 | INFO | Reading frame:  457
2026-05-08 16:51:39 | INFO | Reading frame:  458
2026-05-08 16:51:39 | INFO | Reading frame:  459
2026-05-08 16:51:39 | INFO | Reading frame:  460
2026-05-08 16:51:39 | INFO | Reading frame:  461
2026-05-08 16:51:39 | INFO | Reading frame:  462
2026-05-08 16:51:39 | INFO | Reading frame:  463
2026-05-08 16:51:39 | INFO | Reading frame:  464
2026-05-08 16:51:39 | INFO | Reading frame:  465
2026-05-08 16:51:39 | INFO | Reading frame:  466
2026-05-08 16:51:39 | INFO | Reading frame:  467
2026-05-08 16:51:39 | INFO | Reading frame:  468
2026-05-08 16:51:39 | INFO | Reading frame:  469
2026-05-08 16:51:39 | INFO | Reading frame:  470
2026-05-08 16:51:39 | INFO | Reading frame:  471
2026-05-08 16:51:39 | INFO | Reading frame:  472
2026-05-08 16:51:39 | INFO | Reading frame:  473
2026-05-08 16:51:39 | INFO | Reading frame:  474
2026-05-08 16:51:39 | INFO | Reading frame:  475
2026-05-08 16:51:39 | INFO | Reading frame:  476
2026-05-08 16:51:39 | INFO | Reading frame:  477
2026-05-08 16:51:39 | INFO | Reading frame:  478
2026-05-08 16:51:39 | INFO | Reading frame:  479
2026-05-08 16:51:39 | INFO | Reading frame:  480
2026-05-08 16:51:39 | INFO | Reading frame:  481
2026-05-08 16:51:39 | INFO | Reading frame:  482
2026-05-08 16:51:39 | INFO | Reading frame:  483
2026-05-08 16:51:39 | INFO | Reading frame:  484
2026-05-08 16:51:39 | INFO | Reading frame:  485
2026-05-08 16:51:39 | INFO | Reading frame:  486
2026-05-08 16:51:39 | INFO | Reading frame:  487
2026-05-08 16:51:39 | INFO | Reading frame:  488
2026-05-08 16:51:39 | INFO | Reading frame:  489
2026-05-08 16:51:39 | INFO | Reading frame:  490
2026-05-08 16:51:39 | INFO | Reading frame:  491
2026-05-08 16:51:39 | INFO | Reading frame:  492
2026-05-08 16:51:39 | INFO | Reading frame:  493
2026-05-08 16:51:39 | INFO | Reading frame:  494
2026-05-08 16:51:39 | INFO | Reading frame:  495
2026-05-08 16:51:39 | INFO | Reading frame:  496
2026-05-08 16:51:39 | INFO | Reading frame:  497
2026-05-08 16:51:39 | INFO | Reading frame:  498
2026-05-08 16:51:39 | INFO | Reading frame:  499
2026-05-08 16:51:39 | INFO | Reading frame:  500
2026-05-08 16:51:39 | INFO | Reading frame:  501
2026-05-08 16:51:39 | INFO | Reading frame:  502
2026-05-08 16:51:39 | INFO | Reading frame:  503
2026-05-08 16:51:39 | INFO | Reading frame:  504
2026-05-08 16:51:39 | INFO | Reading frame:  505
2026-05-08 16:51:39 | INFO | Reading frame:  506
2026-05-08 16:51:39 | INFO | Reading frame:  507
2026-05-08 16:51:39 | INFO | Reading frame:  508
2026-05-08 16:51:39 | INFO | Reading frame:  509
2026-05-08 16:51:39 | INFO | Reading frame:  510
2026-05-08 16:51:39 | INFO | Reading frame:  511
2026-05-08 16:51:39 | INFO | Reading frame:  512
2026-05-08 16:51:39 | INFO | Reading frame:  513
2026-05-08 16:51:39 | INFO | Reading frame:  514
2026-05-08 16:51:39 | INFO | Reading frame:  515
2026-05-08 16:51:39 | INFO | Reading frame:  516
2026-05-08 16:51:39 | INFO | Reading frame:  517
2026-05-08 16:51:39 | INFO | Reading frame:  518
2026-05-08 16:51:39 | INFO | Reading frame:  519
2026-05-08 16:51:39 | INFO | Reading frame:  520
2026-05-08 16:51:39 | INFO | Reading frame:  521
2026-05-08 16:51:39 | INFO | Reading frame:  522
2026-05-08 16:51:39 | INFO | Reading frame:  523
2026-05-08 16:51:39 | INFO | Reading frame:  524
2026-05-08 16:51:39 | INFO | Reading frame:  525
2026-05-08 16:51:39 | INFO | Reading frame:  526
2026-05-08 16:51:39 | INFO | Reading frame:  527
2026-05-08 16:51:39 | INFO | Reading frame:  528
2026-05-08 16:51:39 | INFO | Reading frame:  529
2026-05-08 16:51:39 | INFO | Reading frame:  530
2026-05-08 16:51:39 | INFO | Reading frame:  531
2026-05-08 16:51:39 | INFO | Reading frame:  532
2026-05-08 16:51:39 | INFO | Reading frame:  533
2026-05-08 16:51:39 | INFO | Reading frame:  534
2026-05-08 16:51:39 | INFO | Reading frame:  535
2026-05-08 16:51:39 | INFO | Reading frame:  536
2026-05-08 16:51:39 | INFO | Reading frame:  537
2026-05-08 16:51:39 | INFO | Reading frame:  538
2026-05-08 16:51:39 | INFO | Reading frame:  539
2026-05-08 16:51:39 | INFO | Reading frame:  540
2026-05-08 16:51:39 | INFO | Reading frame:  541
2026-05-08 16:51:39 | INFO | Reading frame:  542
2026-05-08 16:51:39 | INFO | Reading frame:  543
2026-05-08 16:51:39 | INFO | Reading frame:  544
2026-05-08 16:51:39 | INFO | Reading frame:  545
2026-05-08 16:51:39 | INFO | Reading frame:  546
2026-05-08 16:51:39 | INFO | Reading frame:  547
2026-05-08 16:51:39 | INFO | Reading frame:  548
2026-05-08 16:51:39 | INFO | Reading frame:  549
2026-05-08 16:51:39 | INFO | Reading frame:  550
2026-05-08 16:51:39 | INFO | Reading frame:  551
2026-05-08 16:51:39 | INFO | Reading frame:  552
2026-05-08 16:51:39 | INFO | Reading frame:  553
2026-05-08 16:51:39 | INFO | Reading frame:  554
2026-05-08 16:51:39 | INFO | Reading frame:  555
2026-05-08 16:51:39 | INFO | Reading frame:  556
2026-05-08 16:51:39 | INFO | Reading frame:  557
2026-05-08 16:51:39 | INFO | Reading frame:  558
2026-05-08 16:51:39 | INFO | Reading frame:  559
2026-05-08 16:51:39 | INFO | Reading frame:  560
2026-05-08 16:51:39 | INFO | Reading frame:  561
2026-05-08 16:51:39 | INFO | Reading frame:  562
2026-05-08 16:51:39 | INFO | Reading frame:  563
2026-05-08 16:51:39 | INFO | Reading frame:  564
2026-05-08 16:51:39 | INFO | Reading frame:  565
2026-05-08 16:51:39 | INFO | Reading frame:  566
2026-05-08 16:51:39 | INFO | Reading frame:  567
2026-05-08 16:51:39 | INFO | Reading frame:  568
2026-05-08 16:51:39 | INFO | Reading frame:  569
2026-05-08 16:51:39 | INFO | Reading frame:  570
2026-05-08 16:51:39 | INFO | Reading frame:  571
2026-05-08 16:51:39 | INFO | Reading frame:  572
2026-05-08 16:51:39 | INFO | Reading frame:  573
2026-05-08 16:51:39 | INFO | Reading frame:  574
2026-05-08 16:51:39 | INFO | Reading frame:  575
2026-05-08 16:51:39 | INFO | Reading frame:  576
2026-05-08 16:51:39 | INFO | Reading frame:  577
2026-05-08 16:51:39 | INFO | Reading frame:  578
2026-05-08 16:51:39 | INFO | Reading frame:  579
2026-05-08 16:51:39 | INFO | Reading frame:  580
2026-05-08 16:51:39 | INFO | Reading frame:  581
2026-05-08 16:51:39 | INFO | Reading frame:  582
2026-05-08 16:51:39 | INFO | Reading frame:  583
2026-05-08 16:51:39 | INFO | Reading frame:  584
2026-05-08 16:51:39 | INFO | Reading frame:  585
2026-05-08 16:51:39 | INFO | Reading frame:  586
2026-05-08 16:51:39 | INFO | Reading frame:  587
2026-05-08 16:51:39 | INFO | Reading frame:  588
2026-05-08 16:51:39 | INFO | Reading frame:  589
2026-05-08 16:51:39 | INFO | Reading frame:  590
2026-05-08 16:51:39 | INFO | Reading frame:  591
2026-05-08 16:51:39 | INFO | Reading frame:  592
2026-05-08 16:51:39 | INFO | Reading frame:  593
2026-05-08 16:51:39 | INFO | Reading frame:  594
2026-05-08 16:51:39 | INFO | Reading frame:  595
2026-05-08 16:51:39 | INFO | Reading frame:  596
2026-05-08 16:51:39 | INFO | Reading frame:  597
2026-05-08 16:51:39 | INFO | Reading frame:  598
2026-05-08 16:51:39 | INFO | Reading frame:  599
2026-05-08 16:51:39 | INFO | Reading frame:  600
2026-05-08 16:51:39 | INFO | Reading frame:  601
2026-05-08 16:51:39 | INFO | Reading frame:  602
2026-05-08 16:51:39 | INFO | Reading frame:  603
2026-05-08 16:51:39 | INFO | Reading frame:  604
2026-05-08 16:51:39 | INFO | Reading frame:  605
2026-05-08 16:51:39 | INFO | Reading frame:  606
2026-05-08 16:51:39 | INFO | Reading frame:  607
2026-05-08 16:51:39 | INFO | Reading frame:  608
2026-05-08 16:51:39 | INFO | Reading frame:  609
2026-05-08 16:51:39 | INFO | Reading frame:  610
2026-05-08 16:51:39 | INFO | Reading frame:  611
2026-05-08 16:51:39 | INFO | Reading frame:  612
2026-05-08 16:51:39 | INFO | Reading frame:  613
2026-05-08 16:51:39 | INFO | Reading frame:  614
2026-05-08 16:51:39 | INFO | Reading frame:  615
2026-05-08 16:51:39 | INFO | Reading frame:  616
2026-05-08 16:51:39 | INFO | Reading frame:  617
2026-05-08 16:51:39 | INFO | Reading frame:  618
2026-05-08 16:51:39 | INFO | Reading frame:  619
2026-05-08 16:51:39 | INFO | Reading frame:  620
2026-05-08 16:51:39 | INFO | Reading frame:  621
2026-05-08 16:51:39 | INFO | Reading frame:  622
2026-05-08 16:51:39 | INFO | Reading frame:  623
2026-05-08 16:51:39 | INFO | Reading frame:  624
2026-05-08 16:51:39 | INFO | Reading frame:  625
2026-05-08 16:51:39 | INFO | Reading frame:  626
2026-05-08 16:51:39 | INFO | Reading frame:  627
2026-05-08 16:51:39 | INFO | Reading frame:  628
2026-05-08 16:51:39 | INFO | Reading frame:  629
2026-05-08 16:51:39 | INFO | Reading frame:  630
2026-05-08 16:51:39 | INFO | Reading frame:  631
2026-05-08 16:51:39 | INFO | Reading frame:  632
2026-05-08 16:51:39 | INFO | Reading frame:  633
2026-05-08 16:51:39 | INFO | Reading frame:  634
2026-05-08 16:51:39 | INFO | Reading frame:  635
2026-05-08 16:51:39 | INFO | Reading frame:  636
2026-05-08 16:51:39 | INFO | Reading frame:  637
2026-05-08 16:51:39 | INFO | Reading frame:  638
2026-05-08 16:51:39 | INFO | Reading frame:  639
2026-05-08 16:51:39 | INFO | Reading frame:  640
2026-05-08 16:51:39 | INFO | Reading frame:  641
2026-05-08 16:51:39 | INFO | Reading frame:  642
2026-05-08 16:51:39 | INFO | Reading frame:  643
2026-05-08 16:51:39 | INFO | Reading frame:  644
2026-05-08 16:51:39 | INFO | Reading frame:  645
2026-05-08 16:51:39 | INFO | Reading frame:  646
2026-05-08 16:51:39 | INFO | Reading frame:  647
2026-05-08 16:51:39 | INFO | Reading frame:  648
2026-05-08 16:51:39 | INFO | Reading frame:  649
2026-05-08 16:51:39 | INFO | Reading frame:  650
2026-05-08 16:51:39 | INFO | Reading frame:  651
2026-05-08 16:51:39 | INFO | Reading frame:  652
2026-05-08 16:51:39 | INFO | Reading frame:  653
2026-05-08 16:51:39 | INFO | Reading frame:  654
2026-05-08 16:51:39 | INFO | Reading frame:  655
2026-05-08 16:51:39 | INFO | Reading frame:  656
2026-05-08 16:51:39 | INFO | Reading frame:  657
2026-05-08 16:51:39 | INFO | Reading frame:  658
2026-05-08 16:51:39 | INFO | Reading frame:  659
2026-05-08 16:51:39 | INFO | Reading frame:  660
2026-05-08 16:51:39 | INFO | Reading frame:  661
2026-05-08 16:51:39 | INFO | Reading frame:  662
2026-05-08 16:51:39 | INFO | Reading frame:  663
2026-05-08 16:51:39 | INFO | Reading frame:  664
2026-05-08 16:51:39 | INFO | Reading frame:  665
2026-05-08 16:51:39 | INFO | Reading frame:  666
2026-05-08 16:51:39 | INFO | Reading frame:  667
2026-05-08 16:51:39 | INFO | Reading frame:  668
2026-05-08 16:51:39 | INFO | Reading frame:  669
2026-05-08 16:51:39 | INFO | Reading frame:  670
2026-05-08 16:51:39 | INFO | Reading frame:  671
2026-05-08 16:51:39 | INFO | Reading frame:  672
2026-05-08 16:51:39 | INFO | Reading frame:  673
2026-05-08 16:51:39 | INFO | Reading frame:  674
2026-05-08 16:51:39 | INFO | Reading frame:  675
2026-05-08 16:51:39 | INFO | Reading frame:  676
2026-05-08 16:51:39 | INFO | Reading frame:  677
2026-05-08 16:51:39 | INFO | Reading frame:  678
2026-05-08 16:51:39 | INFO | Reading frame:  679
2026-05-08 16:51:39 | INFO | Reading frame:  680
2026-05-08 16:51:39 | INFO | Reading frame:  681
2026-05-08 16:51:39 | INFO | Reading frame:  682
2026-05-08 16:51:39 | INFO | Reading frame:  683
2026-05-08 16:51:39 | INFO | Reading frame:  684
2026-05-08 16:51:39 | INFO | Reading frame:  685
2026-05-08 16:51:39 | INFO | Reading frame:  686
2026-05-08 16:51:39 | INFO | Reading frame:  687
2026-05-08 16:51:39 | INFO | Reading frame:  688
2026-05-08 16:51:39 | INFO | Reading frame:  689
2026-05-08 16:51:39 | INFO | Reading frame:  690
2026-05-08 16:51:39 | INFO | Reading frame:  691
2026-05-08 16:51:39 | INFO | Reading frame:  692
2026-05-08 16:51:39 | INFO | Reading frame:  693
2026-05-08 16:51:39 | INFO | Reading frame:  694
2026-05-08 16:51:39 | INFO | Reading frame:  695
2026-05-08 16:51:39 | INFO | Reading frame:  696
2026-05-08 16:51:39 | INFO | Reading frame:  697
2026-05-08 16:51:39 | INFO | Reading frame:  698
2026-05-08 16:51:39 | INFO | Reading frame:  699
2026-05-08 16:51:39 | INFO | Reading frame:  700
2026-05-08 16:51:39 | INFO | Reading frame:  701
2026-05-08 16:51:39 | INFO | Reading frame:  702
2026-05-08 16:51:39 | INFO | Reading frame:  703
2026-05-08 16:51:39 | INFO | Reading frame:  704
2026-05-08 16:51:39 | INFO | Reading frame:  705
2026-05-08 16:51:39 | INFO | Reading frame:  706
2026-05-08 16:51:39 | INFO | Reading frame:  707
2026-05-08 16:51:39 | INFO | Reading frame:  708
2026-05-08 16:51:39 | INFO | Reading frame:  709
2026-05-08 16:51:39 | INFO | Reading frame:  710
2026-05-08 16:51:39 | INFO | Reading frame:  711
2026-05-08 16:51:39 | INFO | Reading frame:  712
2026-05-08 16:51:39 | INFO | Reading frame:  713
2026-05-08 16:51:39 | INFO | Reading frame:  714
2026-05-08 16:51:39 | INFO | Reading frame:  715
2026-05-08 16:51:39 | INFO | Reading frame:  716
2026-05-08 16:51:39 | INFO | Reading frame:  717
2026-05-08 16:51:39 | INFO | Reading frame:  718
2026-05-08 16:51:39 | INFO | Reading frame:  719
2026-05-08 16:51:39 | INFO | Reading frame:  720
2026-05-08 16:51:39 | INFO | Reading frame:  721
2026-05-08 16:51:39 | INFO | Reading frame:  722
2026-05-08 16:51:39 | INFO | Reading frame:  723
2026-05-08 16:51:39 | INFO | Reading frame:  724
2026-05-08 16:51:39 | INFO | Reading frame:  725
2026-05-08 16:51:39 | INFO | Reading frame:  726
2026-05-08 16:51:39 | INFO | Reading frame:  727
2026-05-08 16:51:39 | INFO | Reading frame:  728
2026-05-08 16:51:39 | INFO | Reading frame:  729
2026-05-08 16:51:39 | INFO | Reading frame:  730
2026-05-08 16:51:39 | INFO | Reading frame:  731
2026-05-08 16:51:39 | INFO | Reading frame:  732
2026-05-08 16:51:39 | INFO | Reading frame:  733
2026-05-08 16:51:39 | INFO | Reading frame:  734
2026-05-08 16:51:39 | INFO | Reading frame:  735
2026-05-08 16:51:39 | INFO | Reading frame:  736
2026-05-08 16:51:39 | INFO | Reading frame:  737
2026-05-08 16:51:39 | INFO | Reading frame:  738
2026-05-08 16:51:39 | INFO | Reading frame:  739
2026-05-08 16:51:39 | INFO | Reading frame:  740
2026-05-08 16:51:39 | INFO | Reading frame:  741
2026-05-08 16:51:39 | INFO | Reading frame:  742
2026-05-08 16:51:39 | INFO | Reading frame:  743
2026-05-08 16:51:39 | INFO | Reading frame:  744
2026-05-08 16:51:39 | INFO | Reading frame:  745
2026-05-08 16:51:39 | INFO | Reading frame:  746
2026-05-08 16:51:39 | INFO | Reading frame:  747
2026-05-08 16:51:39 | INFO | Reading frame:  748
2026-05-08 16:51:39 | INFO | Reading frame:  749
2026-05-08 16:51:39 | INFO | Reading frame:  750
2026-05-08 16:51:39 | INFO | Reading frame:  751
2026-05-08 16:51:39 | INFO | Reading frame:  752
2026-05-08 16:51:39 | INFO | Reading frame:  753
2026-05-08 16:51:39 | INFO | Reading frame:  754
2026-05-08 16:51:39 | INFO | Reading frame:  755
2026-05-08 16:51:39 | INFO | Reading frame:  756
2026-05-08 16:51:39 | INFO | Reading frame:  757
2026-05-08 16:51:39 | INFO | Reading frame:  758
2026-05-08 16:51:39 | INFO | Reading frame:  759
2026-05-08 16:51:39 | INFO | Reading frame:  760
2026-05-08 16:51:39 | INFO | Reading frame:  761
2026-05-08 16:51:39 | INFO | Reading frame:  762
2026-05-08 16:51:39 | INFO | Reading frame:  763
2026-05-08 16:51:39 | INFO | Reading frame:  764
2026-05-08 16:51:39 | INFO | Reading frame:  765
2026-05-08 16:51:39 | INFO | Reading frame:  766
2026-05-08 16:51:39 | INFO | Reading frame:  767
2026-05-08 16:51:39 | INFO | Reading frame:  768
2026-05-08 16:51:39 | INFO | Reading frame:  769
2026-05-08 16:51:39 | INFO | Reading frame:  770
2026-05-08 16:51:39 | INFO | Reading frame:  771
2026-05-08 16:51:39 | INFO | Reading frame:  772
2026-05-08 16:51:39 | INFO | Reading frame:  773
2026-05-08 16:51:39 | INFO | Reading frame:  774
2026-05-08 16:51:39 | INFO | Reading frame:  775
2026-05-08 16:51:39 | INFO | Reading frame:  776
2026-05-08 16:51:39 | INFO | Reading frame:  777
2026-05-08 16:51:39 | INFO | Reading frame:  778
2026-05-08 16:51:39 | INFO | Reading frame:  779
2026-05-08 16:51:39 | INFO | Reading frame:  780
2026-05-08 16:51:39 | INFO | Reading frame:  781
2026-05-08 16:51:39 | INFO | Reading frame:  782
2026-05-08 16:51:39 | INFO | Reading frame:  783
2026-05-08 16:51:39 | INFO | Reading frame:  784
2026-05-08 16:51:39 | INFO | Reading frame:  785
2026-05-08 16:51:39 | INFO | Reading frame:  786
2026-05-08 16:51:39 | INFO | Reading frame:  787
2026-05-08 16:51:39 | INFO | Reading frame:  788
2026-05-08 16:51:39 | INFO | Reading frame:  789
2026-05-08 16:51:39 | INFO | Reading frame:  790
2026-05-08 16:51:39 | INFO | Reading frame:  791
2026-05-08 16:51:39 | INFO | Reading frame:  792
2026-05-08 16:51:39 | INFO | Reading frame:  793
2026-05-08 16:51:39 | INFO | Reading frame:  794
2026-05-08 16:51:39 | INFO | Reading frame:  795
2026-05-08 16:51:39 | INFO | Reading frame:  796
2026-05-08 16:51:39 | INFO | Reading frame:  797
2026-05-08 16:51:39 | INFO | Reading frame:  798
2026-05-08 16:51:39 | INFO | Reading frame:  799
2026-05-08 16:51:39 | INFO | Reading frame:  800
2026-05-08 16:51:39 | INFO | Reading frame:  801
2026-05-08 16:51:39 | INFO | Reading frame:  802
2026-05-08 16:51:39 | INFO | Reading frame:  803
2026-05-08 16:51:39 | INFO | Reading frame:  804
2026-05-08 16:51:39 | INFO | Reading frame:  805
2026-05-08 16:51:39 | INFO | Reading frame:  806
2026-05-08 16:51:39 | INFO | Reading frame:  807
2026-05-08 16:51:39 | INFO | Reading frame:  808
2026-05-08 16:51:39 | INFO | Reading frame:  809
2026-05-08 16:51:39 | INFO | Reading frame:  810
2026-05-08 16:51:39 | INFO | Reading frame:  811
2026-05-08 16:51:39 | INFO | Reading frame:  812
2026-05-08 16:51:39 | INFO | Reading frame:  813
2026-05-08 16:51:39 | INFO | Reading frame:  814
2026-05-08 16:51:39 | INFO | Reading frame:  815
2026-05-08 16:51:39 | INFO | Reading frame:  816
2026-05-08 16:51:39 | INFO | Reading frame:  817
2026-05-08 16:51:39 | INFO | Reading frame:  818
2026-05-08 16:51:39 | INFO | Reading frame:  819
2026-05-08 16:51:39 | INFO | Reading frame:  820
2026-05-08 16:51:39 | INFO | Reading frame:  821
2026-05-08 16:51:39 | INFO | Reading frame:  822
2026-05-08 16:51:39 | INFO | Reading frame:  823
2026-05-08 16:51:39 | INFO | Reading frame:  824
2026-05-08 16:51:39 | INFO | Reading frame:  825
2026-05-08 16:51:39 | INFO | Reading frame:  826
2026-05-08 16:51:39 | INFO | Reading frame:  827
2026-05-08 16:51:39 | INFO | Reading frame:  828
2026-05-08 16:51:39 | INFO | Reading frame:  829
2026-05-08 16:51:39 | INFO | Reading frame:  830
2026-05-08 16:51:39 | INFO | Reading frame:  831
2026-05-08 16:51:39 | INFO | Reading frame:  832
2026-05-08 16:51:39 | INFO | Reading frame:  833
2026-05-08 16:51:39 | INFO | Reading frame:  834
2026-05-08 16:51:39 | INFO | Reading frame:  835
2026-05-08 16:51:39 | INFO | Reading frame:  836
2026-05-08 16:51:39 | INFO | Reading frame:  837
2026-05-08 16:51:39 | INFO | Reading frame:  838
2026-05-08 16:51:39 | INFO | Reading frame:  839
2026-05-08 16:51:39 | INFO | Reading frame:  840
2026-05-08 16:51:39 | INFO | Reading frame:  841
2026-05-08 16:51:39 | INFO | Reading frame:  842
2026-05-08 16:51:39 | INFO | Reading frame:  843
2026-05-08 16:51:39 | INFO | Reading frame:  844
2026-05-08 16:51:39 | INFO | Reading frame:  845
2026-05-08 16:51:39 | INFO | Reading frame:  846
2026-05-08 16:51:39 | INFO | Reading frame:  847
2026-05-08 16:51:39 | INFO | Reading frame:  848
2026-05-08 16:51:39 | INFO | Reading frame:  849
2026-05-08 16:51:39 | INFO | Reading frame:  850
2026-05-08 16:51:39 | INFO | Reading frame:  851
2026-05-08 16:51:39 | INFO | Reading frame:  852
2026-05-08 16:51:39 | INFO | Reading frame:  853
2026-05-08 16:51:39 | INFO | Reading frame:  854
2026-05-08 16:51:39 | INFO | Reading frame:  855
2026-05-08 16:51:39 | INFO | Reading frame:  856
2026-05-08 16:51:39 | INFO | Reading frame:  857
2026-05-08 16:51:39 | INFO | Reading frame:  858
2026-05-08 16:51:39 | INFO | Reading frame:  859
2026-05-08 16:51:39 | INFO | Reading frame:  860
2026-05-08 16:51:39 | INFO | Reading frame:  861
2026-05-08 16:51:39 | INFO | Reading frame:  862
2026-05-08 16:51:39 | INFO | Reading frame:  863
2026-05-08 16:51:39 | INFO | Reading frame:  864
2026-05-08 16:51:39 | INFO | Reading frame:  865
2026-05-08 16:51:39 | INFO | Reading frame:  866
2026-05-08 16:51:39 | INFO | Reading frame:  867
2026-05-08 16:51:39 | INFO | Reading frame:  868
2026-05-08 16:51:39 | INFO | Reading frame:  869
2026-05-08 16:51:39 | INFO | Reading frame:  870
2026-05-08 16:51:39 | INFO | Reading frame:  871
2026-05-08 16:51:39 | INFO | Reading frame:  872
2026-05-08 16:51:39 | INFO | Reading frame:  873
2026-05-08 16:51:39 | INFO | Reading frame:  874
2026-05-08 16:51:39 | INFO | Reading frame:  875
2026-05-08 16:51:39 | INFO | Reading frame:  876
2026-05-08 16:51:39 | INFO | Reading frame:  877
2026-05-08 16:51:39 | INFO | Reading frame:  878
2026-05-08 16:51:39 | INFO | Reading frame:  879
2026-05-08 16:51:39 | INFO | Reading frame:  880
2026-05-08 16:51:39 | INFO | Reading frame:  881
2026-05-08 16:51:39 | INFO | Reading frame:  882
2026-05-08 16:51:39 | INFO | Reading frame:  883
2026-05-08 16:51:39 | INFO | Reading frame:  884
2026-05-08 16:51:39 | INFO | Reading frame:  885
2026-05-08 16:51:39 | INFO | Reading frame:  886
2026-05-08 16:51:39 | INFO | Reading frame:  887
2026-05-08 16:51:39 | INFO | Reading frame:  888
2026-05-08 16:51:39 | INFO | Reading frame:  889
2026-05-08 16:51:39 | INFO | Reading frame:  890
2026-05-08 16:51:39 | INFO | Reading frame:  891
2026-05-08 16:51:39 | INFO | Reading frame:  892
2026-05-08 16:51:39 | INFO | Reading frame:  893
2026-05-08 16:51:39 | INFO | Reading frame:  894
2026-05-08 16:51:39 | INFO | Reading frame:  895
2026-05-08 16:51:39 | INFO | Reading frame:  896
2026-05-08 16:51:39 | INFO | Reading frame:  897
2026-05-08 16:51:39 | INFO | Reading frame:  898
2026-05-08 16:51:39 | INFO | Reading frame:  899
2026-05-08 16:51:39 | INFO | Reading frame:  900
2026-05-08 16:51:39 | INFO | Reading frame:  901
2026-05-08 16:51:39 | INFO | Reading frame:  902
2026-05-08 16:51:39 | INFO | Reading frame:  903
2026-05-08 16:51:39 | INFO | Reading frame:  904
2026-05-08 16:51:39 | INFO | Reading frame:  905
2026-05-08 16:51:39 | INFO | Reading frame:  906
2026-05-08 16:51:39 | INFO | Reading frame:  907
2026-05-08 16:51:39 | INFO | Reading frame:  908
2026-05-08 16:51:39 | INFO | Reading frame:  909
2026-05-08 16:51:39 | INFO | Reading frame:  910
2026-05-08 16:51:39 | INFO | Reading frame:  911
2026-05-08 16:51:39 | INFO | Reading frame:  912
2026-05-08 16:51:39 | INFO | Reading frame:  913
2026-05-08 16:51:39 | INFO | Reading frame:  914
2026-05-08 16:51:39 | INFO | Reading frame:  915
2026-05-08 16:51:39 | INFO | Reading frame:  916
2026-05-08 16:51:39 | INFO | Reading frame:  917
2026-05-08 16:51:39 | INFO | Reading frame:  918
2026-05-08 16:51:39 | INFO | Reading frame:  919
2026-05-08 16:51:39 | INFO | Reading frame:  920
2026-05-08 16:51:39 | INFO | Reading frame:  921
2026-05-08 16:51:39 | INFO | Reading frame:  922
2026-05-08 16:51:39 | INFO | Reading frame:  923
2026-05-08 16:51:39 | INFO | Reading frame:  924
2026-05-08 16:51:39 | INFO | Reading frame:  925
2026-05-08 16:51:39 | INFO | Reading frame:  926
2026-05-08 16:51:39 | INFO | Reading frame:  927
2026-05-08 16:51:39 | INFO | Reading frame:  928
2026-05-08 16:51:39 | INFO | Reading frame:  929
2026-05-08 16:51:39 | INFO | Reading frame:  930
2026-05-08 16:51:39 | INFO | Reading frame:  931
2026-05-08 16:51:39 | INFO | Reading frame:  932
2026-05-08 16:51:39 | INFO | Reading frame:  933
2026-05-08 16:51:39 | INFO | Reading frame:  934
2026-05-08 16:51:39 | INFO | Reading frame:  935
2026-05-08 16:51:39 | INFO | Reading frame:  936
2026-05-08 16:51:39 | INFO | Reading frame:  937
2026-05-08 16:51:39 | INFO | Reading frame:  938
2026-05-08 16:51:39 | INFO | Reading frame:  939
2026-05-08 16:51:39 | INFO | Reading frame:  940
2026-05-08 16:51:39 | INFO | Reading frame:  941
2026-05-08 16:51:39 | INFO | Reading frame:  942
2026-05-08 16:51:39 | INFO | Reading frame:  943
2026-05-08 16:51:39 | INFO | Reading frame:  944
2026-05-08 16:51:39 | INFO | Reading frame:  945
2026-05-08 16:51:39 | INFO | Reading frame:  946
2026-05-08 16:51:39 | INFO | Reading frame:  947
2026-05-08 16:51:39 | INFO | Reading frame:  948
2026-05-08 16:51:39 | INFO | Reading frame:  949
2026-05-08 16:51:39 | INFO | Reading frame:  950
2026-05-08 16:51:39 | INFO | Reading frame:  951
2026-05-08 16:51:39 | INFO | Reading frame:  952
2026-05-08 16:51:39 | INFO | Reading frame:  953
2026-05-08 16:51:39 | INFO | Reading frame:  954
2026-05-08 16:51:39 | INFO | Reading frame:  955
2026-05-08 16:51:39 | INFO | Reading frame:  956
2026-05-08 16:51:39 | INFO | Reading frame:  957
2026-05-08 16:51:39 | INFO | Reading frame:  958
2026-05-08 16:51:39 | INFO | Reading frame:  959
2026-05-08 16:51:39 | INFO | Reading frame:  960
2026-05-08 16:51:39 | INFO | Reading frame:  961
2026-05-08 16:51:39 | INFO | Reading frame:  962
2026-05-08 16:51:39 | INFO | Reading frame:  963
2026-05-08 16:51:39 | INFO | Reading frame:  964
2026-05-08 16:51:39 | INFO | Reading frame:  965
2026-05-08 16:51:39 | INFO | Reading frame:  966
2026-05-08 16:51:39 | INFO | Reading frame:  967
2026-05-08 16:51:39 | INFO | Reading frame:  968
2026-05-08 16:51:39 | INFO | Reading frame:  969
2026-05-08 16:51:39 | INFO | Reading frame:  970
2026-05-08 16:51:39 | INFO | Reading frame:  971
2026-05-08 16:51:39 | INFO | Reading frame:  972
2026-05-08 16:51:39 | INFO | Reading frame:  973
2026-05-08 16:51:39 | INFO | Reading frame:  974
2026-05-08 16:51:39 | INFO | Reading frame:  975
2026-05-08 16:51:39 | INFO | Reading frame:  976
2026-05-08 16:51:39 | INFO | Reading frame:  977
2026-05-08 16:51:39 | INFO | Reading frame:  978
2026-05-08 16:51:39 | INFO | Reading frame:  979
2026-05-08 16:51:39 | INFO | Reading frame:  980
2026-05-08 16:51:39 | INFO | Reading frame:  981
2026-05-08 16:51:39 | INFO | Reading frame:  982
2026-05-08 16:51:39 | INFO | Reading frame:  983
2026-05-08 16:51:39 | INFO | Reading frame:  984
2026-05-08 16:51:39 | INFO | Reading frame:  985
2026-05-08 16:51:39 | INFO | Reading frame:  986
2026-05-08 16:51:39 | INFO | Reading frame:  987
2026-05-08 16:51:39 | INFO | Reading frame:  988
2026-05-08 16:51:39 | INFO | Reading frame:  989
2026-05-08 16:51:39 | INFO | Reading frame:  990
2026-05-08 16:51:39 | INFO | Reading frame:  991
2026-05-08 16:51:39 | INFO | Reading frame:  992
2026-05-08 16:51:39 | INFO | Reading frame:  993
2026-05-08 16:51:39 | INFO | Reading frame:  994
2026-05-08 16:51:39 | INFO | Reading frame:  995
2026-05-08 16:51:39 | INFO | Reading frame:  996
2026-05-08 16:51:39 | INFO | Reading frame:  997
2026-05-08 16:51:39 | INFO | Reading frame:  998
2026-05-08 16:51:39 | INFO | Reading frame:  999
2026-05-08 16:51:39 | INFO | Reading frame:  1000
2026-05-08 16:51:39 | INFO | Reading frame:  1001
2026-05-08 16:51:39 | INFO | Reading frame:  1002
2026-05-08 16:51:39 | INFO | Reading frame:  1003
2026-05-08 16:51:39 | INFO | Reading frame:  1004
2026-05-08 16:51:39 | INFO | Reading frame:  1005
2026-05-08 16:51:39 | INFO | Reading frame:  1006
2026-05-08 16:51:39 | INFO | Reading frame:  1007
2026-05-08 16:51:39 | INFO | Reading frame:  1008
2026-05-08 16:51:39 | INFO | Reading frame:  1009
2026-05-08 16:51:39 | INFO | Reading frame:  1010
2026-05-08 16:51:39 | INFO | Reading frame:  1011
2026-05-08 16:51:39 | INFO | Reading frame:  1012
2026-05-08 16:51:39 | INFO | Reading frame:  1013
2026-05-08 16:51:39 | INFO | Reading frame:  1014
2026-05-08 16:51:39 | INFO | Reading frame:  1015
2026-05-08 16:51:39 | INFO | Reading frame:  1016
2026-05-08 16:51:39 | INFO | Reading frame:  1017
2026-05-08 16:51:39 | INFO | Reading frame:  1018
2026-05-08 16:51:39 | INFO | Reading frame:  1019
2026-05-08 16:51:39 | INFO | Reading frame:  1020
2026-05-08 16:51:39 | INFO | Reading frame:  1021
2026-05-08 16:51:39 | INFO | Reading frame:  1022
2026-05-08 16:51:39 | INFO | Reading frame:  1023
2026-05-08 16:51:39 | INFO | Reading frame:  1024
2026-05-08 16:51:39 | INFO | Reading frame:  1025
2026-05-08 16:51:39 | INFO | Reading frame:  1026
2026-05-08 16:51:39 | INFO | Reading frame:  1027
2026-05-08 16:51:39 | INFO | Reading frame:  1028
2026-05-08 16:51:39 | INFO | Reading frame:  1029
2026-05-08 16:51:39 | INFO | Reading frame:  1030
2026-05-08 16:51:39 | INFO | Reading frame:  1031
2026-05-08 16:51:39 | INFO | Reading frame:  1032
2026-05-08 16:51:39 | INFO | Reading frame:  1033
2026-05-08 16:51:39 | INFO | Reading frame:  1034
2026-05-08 16:51:39 | INFO | Reading frame:  1035
2026-05-08 16:51:39 | INFO | Reading frame:  1036
2026-05-08 16:51:39 | INFO | 🔍 Detecting stable segments...
2026-05-08 16:51:39 | INFO | 
2026-05-08 16:51:39 | INFO | Loading weights:   0%|          | 0/398 [00:00<?, ?it/s]
2026-05-08 16:51:39 | INFO | Loading weights: 100%|██████████| 398/398 [00:00<00:00, 43702.10it/s]
2026-05-08 16:51:39 | INFO | [1mCLIPModel LOAD REPORT[0m from: openai/clip-vit-base-patch32
2026-05-08 16:51:39 | INFO | Key                                  | Status     |  | 
2026-05-08 16:51:39 | INFO | -------------------------------------+------------+--+-
2026-05-08 16:51:39 | INFO | text_model.embeddings.position_ids   | UNEXPECTED |  | 
2026-05-08 16:51:39 | INFO | vision_model.embeddings.position_ids | UNEXPECTED |  | 
2026-05-08 16:51:39 | INFO | 
2026-05-08 16:51:39 | INFO | Notes:
2026-05-08 16:51:39 | INFO | - UNEXPECTED:	can be ignored when loading from different task/architecture; not ok if you expect identical arch.
2026-05-08 16:51:48 | INFO | `use_return_dict` is deprecated! Use `return_dict` instead!
2026-05-08 16:51:50 | INFO | UserWarning: torch.utils.checkpoint: the use_reentrant parameter should be passed explicitly. Starting in PyTorch 2.9, calling checkpoint without use_reentrant will raise an exception. use_reentrant=False is recommended, but if you need to preserve the current default behavior, you can pass use_reentrant=True. Refer to docs for more details on the differences between the two variants.
2026-05-08 16:51:50 | INFO | UserWarning: None of the inputs have requires_grad=True. Gradients will be None
2026-05-08 16:51:58 | INFO | FutureWarning: `torch.cuda.amp.autocast(args...)` is deprecated. Please use `torch.amp.autocast('cuda', args...)` instead.
2026-05-08 16:54:21 | INFO | UserWarning: torch.utils.checkpoint: the use_reentrant parameter should be passed explicitly. Starting in PyTorch 2.9, calling checkpoint without use_reentrant will raise an exception. use_reentrant=False is recommended, but if you need to preserve the current default behavior, you can pass use_reentrant=True. Refer to docs for more details on the differences between the two variants.
2026-05-08 16:54:21 | INFO | UserWarning: None of the inputs have requires_grad=True. Gradients will be None
2026-05-08 16:54:27 | INFO | FutureWarning: `torch.cuda.amp.autocast(args...)` is deprecated. Please use `torch.amp.autocast('cuda', args...)` instead.
2026-05-08 16:55:44 | INFO | UserWarning: torch.utils.checkpoint: the use_reentrant parameter should be passed explicitly. Starting in PyTorch 2.9, calling checkpoint without use_reentrant will raise an exception. use_reentrant=False is recommended, but if you need to preserve the current default behavior, you can pass use_reentrant=True. Refer to docs for more details on the differences between the two variants.
2026-05-08 16:55:44 | INFO | UserWarning: None of the inputs have requires_grad=True. Gradients will be None
2026-05-08 16:55:49 | INFO | FutureWarning: `torch.cuda.amp.autocast(args...)` is deprecated. Please use `torch.amp.autocast('cuda', args...)` instead.
2026-05-08 16:57:59 | INFO | UserWarning: torch.utils.checkpoint: the use_reentrant parameter should be passed explicitly. Starting in PyTorch 2.9, calling checkpoint without use_reentrant will raise an exception. use_reentrant=False is recommended, but if you need to preserve the current default behavior, you can pass use_reentrant=True. Refer to docs for more details on the differences between the two variants.
2026-05-08 16:57:59 | INFO | UserWarning: None of the inputs have requires_grad=True. Gradients will be None
2026-05-08 16:58:04 | INFO | FutureWarning: `torch.cuda.amp.autocast(args...)` is deprecated. Please use `torch.amp.autocast('cuda', args...)` instead.
2026-05-08 17:00:14 | INFO | ✅ CLIP similarity list loaded from cache.
2026-05-08 17:00:14 | INFO | 
2026-05-08 17:00:14 | INFO | 📂 Processing segment 0...
2026-05-08 17:00:14 | INFO | Taking screenshot: /sdcard/screenshot-0.png -> /Users/tanmaybhuskute/Documents/gifdroid-reproduction/apps/batterytemperaturedisplay/llm/ViBR_gemini/handheld/run-001/artifacts/hhv-001/step_0_screenshot-0.png
2026-05-08 17:00:14 | INFO | 🔍 Annotated DINO output saved to /Users/tanmaybhuskute/Documents/gifdroid-reproduction/apps/batterytemperaturedisplay/llm/ViBR_gemini/handheld/run-001/artifacts/hhv-001/step_0_dino.png
2026-05-08 17:00:14 | INFO | /Users/tanmaybhuskute/Documents/gifdroid-reproduction/apps/batterytemperaturedisplay/llm/ViBR_gemini/handheld/run-001/artifacts/hhv-001/step_0_dino.png
2026-05-08 17:00:14 | INFO | /Users/tanmaybhuskute/Documents/gifdroid-reproduction/apps/batterytemperaturedisplay/llm/ViBR_gemini/handheld/run-001/artifacts/hhv-001/step_0_tmp_stop.png
2026-05-08 17:00:14 | INFO | Relevant Region Response from Gemini: ```json
2026-05-08 17:00:14 | INFO | {
2026-05-08 17:00:14 | INFO |   "target_regions": [
2026-05-08 17:00:14 | INFO |     4,
2026-05-08 17:00:14 | INFO |     5,
2026-05-08 17:00:14 | INFO |     17,
2026-05-08 17:00:14 | INFO |     22
2026-05-08 17:00:14 | INFO |   ],
2026-05-08 17:00:14 | INFO |   "predicted_action": "tap"
2026-05-08 17:00:14 | INFO | }
2026-05-08 17:00:14 | INFO | ```
2026-05-08 17:00:14 | INFO | 🔍 Relevant regions: {'target_regions': [4, 5, 17, 22], 'predicted_action': 'tap'}
2026-05-08 17:00:14 | INFO | 🧠 GPT selected regions: [4, 5, 17, 22]
2026-05-08 17:00:14 | INFO | ✅ Relevant-only annotation saved to /Users/tanmaybhuskute/Documents/gifdroid-reproduction/apps/batterytemperaturedisplay/llm/ViBR_gemini/handheld/run-001/artifacts/hhv-001/step_0_relevant_regions.png
2026-05-08 17:00:14 | INFO | /Users/tanmaybhuskute/Documents/gifdroid-reproduction/apps/batterytemperaturedisplay/llm/ViBR_gemini/handheld/run-001/artifacts/hhv-001/step_0_relevant_regions.png
2026-05-08 17:00:14 | INFO | /Users/tanmaybhuskute/Documents/gifdroid-reproduction/apps/batterytemperaturedisplay/llm/ViBR_gemini/handheld/run-001/artifacts/hhv-001/step_0_screenshot-0.png
2026-05-08 17:00:14 | INFO | Consistency Response from Gemini: ```json
2026-05-08 17:00:14 | INFO | {
2026-05-08 17:00:14 | INFO |   "same_state": "no",
2026-05-08 17:00:14 | INFO |   "description": "The current screen displays a system permission dialog asking to allow notifications, which is not present in the reference screen. This dialog blocks interaction with the underlying app interface, preventing the user from performing the same actions as in the reference state."
2026-05-08 17:00:14 | INFO | }
2026-05-08 17:00:14 | INFO | ```
2026-05-08 17:00:14 | INFO | 🔄 Attempting to align state (try 1/3)...
2026-05-08 17:00:14 | INFO | /Users/tanmaybhuskute/Documents/gifdroid-reproduction/apps/batterytemperaturedisplay/llm/ViBR_gemini/handheld/run-001/artifacts/hhv-001/step_0_tmp_start.png
2026-05-08 17:00:14 | INFO | /Users/tanmaybhuskute/Documents/gifdroid-reproduction/apps/batterytemperaturedisplay/llm/ViBR_gemini/handheld/run-001/artifacts/hhv-001/step_0_tmp_stop.png
2026-05-08 17:00:14 | INFO | /Users/tanmaybhuskute/Documents/gifdroid-reproduction/apps/batterytemperaturedisplay/llm/ViBR_gemini/handheld/run-001/artifacts/hhv-001/step_0_labeled.png
2026-05-08 17:00:14 | INFO | Region Action Response from Gemini: ```json
2026-05-08 17:00:14 | INFO | {
2026-05-08 17:00:14 | INFO |     "action": "tap",
2026-05-08 17:00:14 | INFO |     "region": 5,
2026-05-08 17:00:14 | INFO |     "description": "Tap on the 'Don't allow' button, as it is the most semantically similar negative action to the original 'KILL APP & EXIT' tap."
2026-05-08 17:00:14 | INFO | }
2026-05-08 17:00:14 | INFO | ```
2026-05-08 17:00:14 | INFO | 🎯 Recovery using region index: 5 at (540, 1196)
2026-05-08 17:00:14 | INFO | [1] Tap on the 'Don't allow' button, as it is the most semantically similar negative action to the original 'KILL APP & EXIT' tap. -> tap
2026-05-08 17:00:14 | INFO | Taking screenshot: /sdcard/screenshot-0.png -> /Users/tanmaybhuskute/Documents/gifdroid-reproduction/apps/batterytemperaturedisplay/llm/ViBR_gemini/handheld/run-001/artifacts/hhv-001/step_0_screenshot-0.png
2026-05-08 17:00:14 | INFO | /Users/tanmaybhuskute/Documents/gifdroid-reproduction/apps/batterytemperaturedisplay/llm/ViBR_gemini/handheld/run-001/artifacts/hhv-001/step_0_tmp_stop.png
2026-05-08 17:00:14 | INFO | /Users/tanmaybhuskute/Documents/gifdroid-reproduction/apps/batterytemperaturedisplay/llm/ViBR_gemini/handheld/run-001/artifacts/hhv-001/step_0_screenshot-0.png
2026-05-08 17:00:14 | INFO | Consistency Response from Gemini: ```json
2026-05-08 17:00:14 | INFO | {
2026-05-08 17:00:14 | INFO |   "same_state": "yes"
2026-05-08 17:00:14 | INFO | }
2026-05-08 17:00:14 | INFO | ```
2026-05-08 17:00:14 | INFO | /Users/tanmaybhuskute/Documents/gifdroid-reproduction/apps/batterytemperaturedisplay/llm/ViBR_gemini/handheld/run-001/artifacts/hhv-001/step_0_relevant_regions.png
2026-05-08 17:00:14 | INFO | /Users/tanmaybhuskute/Documents/gifdroid-reproduction/apps/batterytemperaturedisplay/llm/ViBR_gemini/handheld/run-001/artifacts/hhv-001/step_0_tmp_stop.png
2026-05-08 17:00:14 | INFO | /Users/tanmaybhuskute/Documents/gifdroid-reproduction/apps/batterytemperaturedisplay/llm/ViBR_gemini/handheld/run-001/artifacts/hhv-001/step_0_labeled.png
2026-05-08 17:00:14 | INFO | Region Action Response from Gemini: ```json
2026-05-08 17:00:14 | INFO | {
2026-05-08 17:00:14 | INFO |   "action": "tap",
2026-05-08 17:00:14 | INFO |   "region": 5,
2026-05-08 17:00:14 | INFO |   "description": "Tap 'Don't allow' button"
2026-05-08 17:00:14 | INFO | }
2026-05-08 17:00:14 | INFO | ```
2026-05-08 17:00:14 | INFO | 🎯 Using region index: 5 at (540, 1196)
2026-05-08 17:00:14 | INFO | [1] Tap 'Don't allow' button -> tap
2026-05-08 17:00:14 | INFO | ✅ Action executed.
2026-05-08 17:00:14 | INFO | 
2026-05-08 17:00:14 | INFO | 
2026-05-08 17:00:14 | INFO | 📂 Processing segment 1...
2026-05-08 17:00:14 | INFO | Taking screenshot: /sdcard/screenshot-0.png -> /Users/tanmaybhuskute/Documents/gifdroid-reproduction/apps/batterytemperaturedisplay/llm/ViBR_gemini/handheld/run-001/artifacts/hhv-001/step_1_screenshot-0.png
2026-05-08 17:00:14 | INFO | 🔍 Annotated DINO output saved to /Users/tanmaybhuskute/Documents/gifdroid-reproduction/apps/batterytemperaturedisplay/llm/ViBR_gemini/handheld/run-001/artifacts/hhv-001/step_1_dino.png
2026-05-08 17:00:14 | INFO | /Users/tanmaybhuskute/Documents/gifdroid-reproduction/apps/batterytemperaturedisplay/llm/ViBR_gemini/handheld/run-001/artifacts/hhv-001/step_1_dino.png
2026-05-08 17:00:14 | INFO | /Users/tanmaybhuskute/Documents/gifdroid-reproduction/apps/batterytemperaturedisplay/llm/ViBR_gemini/handheld/run-001/artifacts/hhv-001/step_1_tmp_stop.png
2026-05-08 17:00:14 | INFO | Relevant Region Response from Gemini: ```json
2026-05-08 17:00:14 | INFO | {
2026-05-08 17:00:14 | INFO |   "target_regions": [
2026-05-08 17:00:14 | INFO |     1
2026-05-08 17:00:14 | INFO |   ],
2026-05-08 17:00:14 | INFO |   "predicted_action": "input_text"
2026-05-08 17:00:14 | INFO | }
2026-05-08 17:00:14 | INFO | ```
2026-05-08 17:00:14 | INFO | 🔍 Relevant regions: {'target_regions': [1], 'predicted_action': 'input_text'}
2026-05-08 17:00:14 | INFO | 🧠 GPT selected regions: [1]
2026-05-08 17:00:14 | INFO | ✅ Relevant-only annotation saved to /Users/tanmaybhuskute/Documents/gifdroid-reproduction/apps/batterytemperaturedisplay/llm/ViBR_gemini/handheld/run-001/artifacts/hhv-001/step_1_relevant_regions.png
2026-05-08 17:00:14 | INFO | /Users/tanmaybhuskute/Documents/gifdroid-reproduction/apps/batterytemperaturedisplay/llm/ViBR_gemini/handheld/run-001/artifacts/hhv-001/step_1_relevant_regions.png
2026-05-08 17:00:14 | INFO | /Users/tanmaybhuskute/Documents/gifdroid-reproduction/apps/batterytemperaturedisplay/llm/ViBR_gemini/handheld/run-001/artifacts/hhv-001/step_1_screenshot-0.png
2026-05-08 17:00:14 | INFO | Consistency Response from Gemini: ```json
2026-05-08 17:00:14 | INFO | {
2026-05-08 17:00:14 | INFO |   "same_state": "yes"
2026-05-08 17:00:14 | INFO | }
2026-05-08 17:00:14 | INFO | ```
2026-05-08 17:00:14 | INFO | /Users/tanmaybhuskute/Documents/gifdroid-reproduction/apps/batterytemperaturedisplay/llm/ViBR_gemini/handheld/run-001/artifacts/hhv-001/step_1_relevant_regions.png
2026-05-08 17:00:14 | INFO | /Users/tanmaybhuskute/Documents/gifdroid-reproduction/apps/batterytemperaturedisplay/llm/ViBR_gemini/handheld/run-001/artifacts/hhv-001/step_1_tmp_stop.png
2026-05-08 17:00:14 | INFO | /Users/tanmaybhuskute/Documents/gifdroid-reproduction/apps/batterytemperaturedisplay/llm/ViBR_gemini/handheld/run-001/artifacts/hhv-001/step_1_labeled.png
2026-05-08 17:00:14 | INFO | Region Action Response from Gemini: ```json
2026-05-08 17:00:14 | INFO | {
2026-05-08 17:00:14 | INFO |   "action": "input_text",
2026-05-08 17:00:14 | INFO |   "text": "2",
2026-05-08 17:00:14 | INFO |   "description": "Type the number 2 into the focused input field."
2026-05-08 17:00:14 | INFO | }
2026-05-08 17:00:14 | INFO | ```
2026-05-08 17:00:14 | INFO | ⚠️ No valid region or element match. Proceeding without position.
2026-05-08 17:00:14 | INFO | [1] Type the number 2 into the focused input field. -> input_text
2026-05-08 17:00:14 | INFO | ✅ Action executed.
2026-05-08 17:00:14 | INFO | 
2026-05-08 17:00:14 | INFO | 
2026-05-08 17:00:14 | INFO | 📂 Processing segment 2...
2026-05-08 17:00:14 | INFO | Taking screenshot: /sdcard/screenshot-0.png -> /Users/tanmaybhuskute/Documents/gifdroid-reproduction/apps/batterytemperaturedisplay/llm/ViBR_gemini/handheld/run-001/artifacts/hhv-001/step_2_screenshot-0.png
2026-05-08 17:00:14 | INFO | 🔍 Annotated DINO output saved to /Users/tanmaybhuskute/Documents/gifdroid-reproduction/apps/batterytemperaturedisplay/llm/ViBR_gemini/handheld/run-001/artifacts/hhv-001/step_2_dino.png
2026-05-08 17:00:14 | INFO | /Users/tanmaybhuskute/Documents/gifdroid-reproduction/apps/batterytemperaturedisplay/llm/ViBR_gemini/handheld/run-001/artifacts/hhv-001/step_2_dino.png
2026-05-08 17:00:14 | INFO | /Users/tanmaybhuskute/Documents/gifdroid-reproduction/apps/batterytemperaturedisplay/llm/ViBR_gemini/handheld/run-001/artifacts/hhv-001/step_2_tmp_stop.png
2026-05-08 17:00:14 | INFO | Relevant Region Response from Gemini: ```json
2026-05-08 17:00:14 | INFO | {
2026-05-08 17:00:14 | INFO |   "target_regions": [
2026-05-08 17:00:14 | INFO |     25
2026-05-08 17:00:14 | INFO |   ],
2026-05-08 17:00:14 | INFO |   "predicted_action": "tap"
2026-05-08 17:00:14 | INFO | }
2026-05-08 17:00:14 | INFO | ```
2026-05-08 17:00:14 | INFO | 🔍 Relevant regions: {'target_regions': [25], 'predicted_action': 'tap'}
2026-05-08 17:00:14 | INFO | 🧠 GPT selected regions: [25]
2026-05-08 17:00:14 | INFO | ✅ Relevant-only annotation saved to /Users/tanmaybhuskute/Documents/gifdroid-reproduction/apps/batterytemperaturedisplay/llm/ViBR_gemini/handheld/run-001/artifacts/hhv-001/step_2_relevant_regions.png
2026-05-08 17:00:14 | INFO | /Users/tanmaybhuskute/Documents/gifdroid-reproduction/apps/batterytemperaturedisplay/llm/ViBR_gemini/handheld/run-001/artifacts/hhv-001/step_2_relevant_regions.png
2026-05-08 17:00:14 | INFO | /Users/tanmaybhuskute/Documents/gifdroid-reproduction/apps/batterytemperaturedisplay/llm/ViBR_gemini/handheld/run-001/artifacts/hhv-001/step_2_screenshot-0.png
2026-05-08 17:00:14 | INFO | Consistency Response from Gemini: ```json
2026-05-08 17:00:14 | INFO | {
2026-05-08 17:00:14 | INFO |   "same_state": "no",
2026-05-08 17:00:14 | INFO |   "description": "The two screens represent different states of the application. The reference screen shows the app in an active logging state, with a \"STOP LOGGING\" button visible. The current screen shows the app in an idle state, with a \"START LOGGING\" button. The primary action available to the user is different in each screen."
2026-05-08 17:00:14 | INFO | }
2026-05-08 17:00:59 | INFO | ```UserWarning: torch.utils.checkpoint: the use_reentrant parameter should be passed explicitly. Starting in PyTorch 2.9, calling checkpoint without use_reentrant will raise an exception. use_reentrant=False is recommended, but if you need to preserve the current default behavior, you can pass use_reentrant=True. Refer to docs for more details on the differences between the two variants.
2026-05-08 17:00:59 | INFO | UserWarning: None of the inputs have requires_grad=True. Gradients will be None
2026-05-08 17:01:05 | INFO | FutureWarning: `torch.cuda.amp.autocast(args...)` is deprecated. Please use `torch.amp.autocast('cuda', args...)` instead.
2026-05-08 17:02:22 | INFO | 
2026-05-08 17:02:22 | INFO | 🔄 Attempting to align state (try 1/3)...
2026-05-08 17:02:22 | INFO | /Users/tanmaybhuskute/Documents/gifdroid-reproduction/apps/batterytemperaturedisplay/llm/ViBR_gemini/handheld/run-001/artifacts/hhv-001/step_2_tmp_start.png
2026-05-08 17:02:22 | INFO | /Users/tanmaybhuskute/Documents/gifdroid-reproduction/apps/batterytemperaturedisplay/llm/ViBR_gemini/handheld/run-001/artifacts/hhv-001/step_2_tmp_stop.png
2026-05-08 17:02:22 | INFO | /Users/tanmaybhuskute/Documents/gifdroid-reproduction/apps/batterytemperaturedisplay/llm/ViBR_gemini/handheld/run-001/artifacts/hhv-001/step_2_labeled.png
2026-05-08 17:02:22 | INFO | Region Action Response from Gemini: ```json
2026-05-08 17:02:22 | INFO | {
2026-05-08 17:02:22 | INFO |   "action": "tap",
2026-05-08 17:02:22 | INFO |   "region": 2,
2026-05-08 17:02:22 | INFO |   "description": "Tap on the dropdown menu with the text 'minutes'."
2026-05-08 17:02:22 | INFO | }
2026-05-08 17:02:22 | INFO | ```
2026-05-08 17:02:22 | INFO | 🎯 Recovery using region index: 2 at (471, 918)
2026-05-08 17:02:22 | INFO | [1] Tap on the dropdown menu with the text 'minutes'. -> tap
2026-05-08 17:02:22 | INFO | Taking screenshot: /sdcard/screenshot-0.png -> /Users/tanmaybhuskute/Documents/gifdroid-reproduction/apps/batterytemperaturedisplay/llm/ViBR_gemini/handheld/run-001/artifacts/hhv-001/step_2_screenshot-0.png
2026-05-08 17:02:22 | INFO | /Users/tanmaybhuskute/Documents/gifdroid-reproduction/apps/batterytemperaturedisplay/llm/ViBR_gemini/handheld/run-001/artifacts/hhv-001/step_2_tmp_stop.png
2026-05-08 17:02:22 | INFO | /Users/tanmaybhuskute/Documents/gifdroid-reproduction/apps/batterytemperaturedisplay/llm/ViBR_gemini/handheld/run-001/artifacts/hhv-001/step_2_screenshot-0.png
2026-05-08 17:02:22 | INFO | Consistency Response from Gemini: ```json
2026-05-08 17:02:22 | INFO | {
2026-05-08 17:02:22 | INFO |   "same_state": "no",
2026-05-08 17:02:22 | INFO |   "description": "The state of the application is different. In the reference image, the logging is active, indicated by the \"STOP LOGGING\" button. In the current image, the logging is not active, as shown by the \"START LOGGING\" button. Additionally, a dropdown menu for time units is open in the current screen, which is not the case in the reference screen."
2026-05-08 17:02:22 | INFO | }
2026-05-08 17:02:22 | INFO | ```
2026-05-08 17:02:22 | INFO | 🔄 Attempting to align state (try 2/3)...
2026-05-08 17:02:22 | INFO | /Users/tanmaybhuskute/Documents/gifdroid-reproduction/apps/batterytemperaturedisplay/llm/ViBR_gemini/handheld/run-001/artifacts/hhv-001/step_2_tmp_start.png
2026-05-08 17:02:22 | INFO | /Users/tanmaybhuskute/Documents/gifdroid-reproduction/apps/batterytemperaturedisplay/llm/ViBR_gemini/handheld/run-001/artifacts/hhv-001/step_2_tmp_stop.png
2026-05-08 17:02:22 | INFO | /Users/tanmaybhuskute/Documents/gifdroid-reproduction/apps/batterytemperaturedisplay/llm/ViBR_gemini/handheld/run-001/artifacts/hhv-001/step_2_labeled.png
2026-05-08 17:02:22 | INFO | Region Action Response from Gemini: ```json
2026-05-08 17:02:22 | INFO | {
2026-05-08 17:02:22 | INFO |   "action": "tap",
2026-05-08 17:02:22 | INFO |   "region": 2,
2026-05-08 17:02:22 | INFO |   "description": "Tap on the dropdown menu with the text 'minutes'."
2026-05-08 17:02:22 | INFO | }
2026-05-08 17:02:22 | INFO | ```
2026-05-08 17:02:22 | INFO | 🎯 Recovery using region index: 2 at (471, 918)
2026-05-08 17:02:22 | INFO | [1] Tap on the dropdown menu with the text 'minutes'. -> tap
2026-05-08 17:02:22 | INFO | Taking screenshot: /sdcard/screenshot-0.png -> /Users/tanmaybhuskute/Documents/gifdroid-reproduction/apps/batterytemperaturedisplay/llm/ViBR_gemini/handheld/run-001/artifacts/hhv-001/step_2_screenshot-0.png
2026-05-08 17:02:22 | INFO | /Users/tanmaybhuskute/Documents/gifdroid-reproduction/apps/batterytemperaturedisplay/llm/ViBR_gemini/handheld/run-001/artifacts/hhv-001/step_2_tmp_stop.png
2026-05-08 17:02:22 | INFO | /Users/tanmaybhuskute/Documents/gifdroid-reproduction/apps/batterytemperaturedisplay/llm/ViBR_gemini/handheld/run-001/artifacts/hhv-001/step_2_screenshot-0.png
2026-05-08 17:02:22 | INFO | Consistency Response from Gemini: ```json
2026-05-08 17:02:22 | INFO | {
2026-05-08 17:02:22 | INFO |   "same_state": "yes"
2026-05-08 17:02:22 | INFO | }
2026-05-08 17:02:22 | INFO | ```
2026-05-08 17:02:22 | INFO | /Users/tanmaybhuskute/Documents/gifdroid-reproduction/apps/batterytemperaturedisplay/llm/ViBR_gemini/handheld/run-001/artifacts/hhv-001/step_2_relevant_regions.png
2026-05-08 17:02:22 | INFO | /Users/tanmaybhuskute/Documents/gifdroid-reproduction/apps/batterytemperaturedisplay/llm/ViBR_gemini/handheld/run-001/artifacts/hhv-001/step_2_tmp_stop.png
2026-05-08 17:02:22 | INFO | /Users/tanmaybhuskute/Documents/gifdroid-reproduction/apps/batterytemperaturedisplay/llm/ViBR_gemini/handheld/run-001/artifacts/hhv-001/step_2_labeled.png
2026-05-08 17:02:22 | INFO | Region Action Response from Gemini: ```json
2026-05-08 17:02:22 | INFO | {
2026-05-08 17:02:22 | INFO |   "action": "tap",
2026-05-08 17:02:22 | INFO |   "region": 4,
2026-05-08 17:02:22 | INFO |   "description": "Tap on the 'hours' option in the dropdown menu, which is analogous to tapping a button in the keyboard's action bar from the recording."
2026-05-08 17:02:22 | INFO | }
2026-05-08 17:02:22 | INFO | ```
2026-05-08 17:02:22 | INFO | 🎯 Using region index: 4 at (540, 1067)
2026-05-08 17:02:22 | INFO | [1] Tap on the 'hours' option in the dropdown menu, which is analogous to tapping a button in the keyboard's action bar from the recording. -> tap
2026-05-08 17:02:22 | INFO | ✅ Action executed.
2026-05-08 17:02:22 | INFO | 
2026-05-08 17:02:22 | INFO | 
2026-05-08 17:02:22 | INFO | 📂 Processing segment 3...
2026-05-08 17:02:22 | INFO | Taking screenshot: /sdcard/screenshot-0.png -> /Users/tanmaybhuskute/Documents/gifdroid-reproduction/apps/batterytemperaturedisplay/llm/ViBR_gemini/handheld/run-001/artifacts/hhv-001/step_3_screenshot-0.png
2026-05-08 17:02:22 | INFO | 🔍 Annotated DINO output saved to /Users/tanmaybhuskute/Documents/gifdroid-reproduction/apps/batterytemperaturedisplay/llm/ViBR_gemini/handheld/run-001/artifacts/hhv-001/step_3_dino.png
2026-05-08 17:02:22 | INFO | /Users/tanmaybhuskute/Documents/gifdroid-reproduction/apps/batterytemperaturedisplay/llm/ViBR_gemini/handheld/run-001/artifacts/hhv-001/step_3_dino.png
2026-05-08 17:02:22 | INFO | /Users/tanmaybhuskute/Documents/gifdroid-reproduction/apps/batterytemperaturedisplay/llm/ViBR_gemini/handheld/run-001/artifacts/hhv-001/step_3_tmp_stop.png
2026-05-08 17:02:22 | INFO | Relevant Region Response from Gemini: ```json
2026-05-08 17:02:22 | INFO | {
2026-05-08 17:02:22 | INFO |   "target_regions": [],
2026-05-08 17:02:22 | INFO |   "predicted_action": "back"
2026-05-08 17:02:22 | INFO | }
2026-05-08 17:02:22 | INFO | ```
2026-05-08 17:02:22 | INFO | 🔍 Relevant regions: {'target_regions': [], 'predicted_action': 'back'}
2026-05-08 17:02:22 | INFO | 🧠 GPT selected regions: []
2026-05-08 17:02:22 | INFO | ⚠️ No relevant regions to annotate.
2026-05-08 17:02:22 | INFO | /Users/tanmaybhuskute/Documents/gifdroid-reproduction/apps/batterytemperaturedisplay/llm/ViBR_gemini/handheld/run-001/artifacts/hhv-001/step_3_relevant_regions.png
2026-05-08 17:02:22 | INFO | /Users/tanmaybhuskute/Documents/gifdroid-reproduction/apps/batterytemperaturedisplay/llm/ViBR_gemini/handheld/run-001/artifacts/hhv-001/step_3_screenshot-0.png
2026-05-08 17:02:22 | INFO | Consistency Response from Gemini: ```json
2026-05-08 17:02:22 | INFO | {
2026-05-08 17:02:22 | INFO |   "same_state": "no",
2026-05-08 17:02:22 | INFO |   "description": "The reference screen shows that logging is in progress, indicated by the 'STOP LOGGING' button. The current screen is in a pre-logging state, with a 'START LOGGING' button. This represents a different functional state of the application."
2026-05-08 17:02:22 | INFO | }
2026-05-08 17:02:22 | INFO | ```
2026-05-08 17:02:22 | INFO | 🔄 Attempting to align state (try 1/3)...
2026-05-08 17:02:22 | INFO | /Users/tanmaybhuskute/Documents/gifdroid-reproduction/apps/batterytemperaturedisplay/llm/ViBR_gemini/handheld/run-001/artifacts/hhv-001/step_3_tmp_start.png
2026-05-08 17:02:22 | INFO | /Users/tanmaybhuskute/Documents/gifdroid-reproduction/apps/batterytemperaturedisplay/llm/ViBR_gemini/handheld/run-001/artifacts/hhv-001/step_3_tmp_stop.png
2026-05-08 17:02:22 | INFO | /Users/tanmaybhuskute/Documents/gifdroid-reproduction/apps/batterytemperaturedisplay/llm/ViBR_gemini/handheld/run-001/artifacts/hhv-001/step_3_labeled.png
2026-05-08 17:02:22 | INFO | Region Action Response from Gemini: ```json
2026-05-08 17:02:22 | INFO | {
2026-05-08 17:02:22 | INFO |   "action": "tap",
2026-05-08 17:02:22 | INFO |   "region": 1,
2026-05-08 17:02:22 | INFO |   "description": "Tap the input field for 'Log for'."
2026-05-08 17:02:22 | INFO | }
2026-05-08 17:02:22 | INFO | ```
2026-05-08 17:02:22 | INFO | 🎯 Recovery using region index: 1 at (238, 919)
2026-05-08 17:02:22 | INFO | [1] Tap the input field for 'Log for'. -> tap
2026-05-08 17:02:22 | INFO | Taking screenshot: /sdcard/screenshot-0.png -> /Users/tanmaybhuskute/Documents/gifdroid-reproduction/apps/batterytemperaturedisplay/llm/ViBR_gemini/handheld/run-001/artifacts/hhv-001/step_3_screenshot-0.png
2026-05-08 17:02:22 | INFO | /Users/tanmaybhuskute/Documents/gifdroid-reproduction/apps/batterytemperaturedisplay/llm/ViBR_gemini/handheld/run-001/artifacts/hhv-001/step_3_tmp_stop.png
2026-05-08 17:02:22 | INFO | /Users/tanmaybhuskute/Documents/gifdroid-reproduction/apps/batterytemperaturedisplay/llm/ViBR_gemini/handheld/run-001/artifacts/hhv-001/step_3_screenshot-0.png
2026-05-08 17:02:22 | INFO | Consistency Response from Gemini: ```json
2026-05-08 17:02:22 | INFO | {
2026-05-08 17:02:22 | INFO |   "same_state": "no",
2026-05-08 17:02:22 | INFO |   "description": "The state of the app is different. In the reference image, the logging is active, indicated by the 'STOP LOGGING' button. In the current image, the logging is inactive, indicated by the 'START LOGGING' button. Additionally, the UI layout is different, with extra options like 'Enable Auto Start' and 'KILL APP & EXIT' visible in the current image but not in the reference."
2026-05-08 17:02:22 | INFO | }
2026-05-08 17:02:22 | INFO | ```
2026-05-08 17:02:22 | INFO | 🔄 Attempting to align state (try 2/3)...
2026-05-08 17:02:22 | INFO | /Users/tanmaybhuskute/Documents/gifdroid-reproduction/apps/batterytemperaturedisplay/llm/ViBR_gemini/handheld/run-001/artifacts/hhv-001/step_3_tmp_start.png
2026-05-08 17:02:22 | INFO | /Users/tanmaybhuskute/Documents/gifdroid-reproduction/apps/batterytemperaturedisplay/llm/ViBR_gemini/handheld/run-001/artifacts/hhv-001/step_3_tmp_stop.png
2026-05-08 17:02:22 | INFO | /Users/tanmaybhuskute/Documents/gifdroid-reproduction/apps/batterytemperaturedisplay/llm/ViBR_gemini/handheld/run-001/artifacts/hhv-001/step_3_labeled.png
2026-05-08 17:02:22 | INFO | Region Action Response from Gemini: ```json
2026-05-08 17:02:22 | INFO | {
2026-05-08 17:02:22 | INFO |   "action": "tap",
2026-05-08 17:02:22 | INFO |   "region": 3,
2026-05-08 17:02:22 | INFO |   "description": "Tap the START LOGGING button."
2026-05-08 17:02:22 | INFO | }
2026-05-08 17:02:22 | INFO | ```
2026-05-08 17:02:22 | INFO | 🎯 Recovery using region index: 3 at (821, 919)
2026-05-08 17:02:22 | INFO | [1] Tap the START LOGGING button. -> tap
2026-05-08 17:02:51 | INFO | Taking screenshot: /sdcard/screenshot-0.png -> /Users/tanmaybhuskute/Documents/gifdroid-reproduction/apps/batterytemperaturedisplay/llm/ViBR_gemini/handheld/run-001/artifacts/hhv-001/step_3_screenshot-0.pngUserWarning: torch.utils.checkpoint: the use_reentrant parameter should be passed explicitly. Starting in PyTorch 2.9, calling checkpoint without use_reentrant will raise an exception. use_reentrant=False is recommended, but if you need to preserve the current default behavior, you can pass use_reentrant=True. Refer to docs for more details on the differences between the two variants.
2026-05-08 17:02:51 | INFO | UserWarning: None of the inputs have requires_grad=True. Gradients will be None
2026-05-08 17:02:56 | INFO | FutureWarning: `torch.cuda.amp.autocast(args...)` is deprecated. Please use `torch.amp.autocast('cuda', args...)` instead.
2026-05-08 17:05:22 | INFO | 
2026-05-08 17:05:22 | INFO | /Users/tanmaybhuskute/Documents/gifdroid-reproduction/apps/batterytemperaturedisplay/llm/ViBR_gemini/handheld/run-001/artifacts/hhv-001/step_3_tmp_stop.png
2026-05-08 17:05:22 | INFO | /Users/tanmaybhuskute/Documents/gifdroid-reproduction/apps/batterytemperaturedisplay/llm/ViBR_gemini/handheld/run-001/artifacts/hhv-001/step_3_screenshot-0.png
2026-05-08 17:05:22 | INFO | Consistency Response from Gemini: ```json
2026-05-08 17:05:22 | INFO | {
2026-05-08 17:05:22 | INFO |   "same_state": "no",
2026-05-08 17:05:22 | INFO |   "description": "The two screens represent different functional states of the app. The reference image shows a \"STOP LOGGING\" button, suggesting a logging process is active or has been set up. The current image shows a \"START LOGGING\" button and requires the user to input a duration, indicating the app is in a pre-logging state. The primary action available is different in each screen."
2026-05-08 17:05:22 | INFO | }
2026-05-08 17:05:22 | INFO | ```
2026-05-08 17:05:22 | INFO | 🔄 Attempting to align state (try 3/3)...
2026-05-08 17:05:22 | INFO | /Users/tanmaybhuskute/Documents/gifdroid-reproduction/apps/batterytemperaturedisplay/llm/ViBR_gemini/handheld/run-001/artifacts/hhv-001/step_3_tmp_start.png
2026-05-08 17:05:22 | INFO | /Users/tanmaybhuskute/Documents/gifdroid-reproduction/apps/batterytemperaturedisplay/llm/ViBR_gemini/handheld/run-001/artifacts/hhv-001/step_3_tmp_stop.png
2026-05-08 17:05:22 | INFO | /Users/tanmaybhuskute/Documents/gifdroid-reproduction/apps/batterytemperaturedisplay/llm/ViBR_gemini/handheld/run-001/artifacts/hhv-001/step_3_labeled.png
2026-05-08 17:05:22 | INFO | Region Action Response from Gemini: ```json
2026-05-08 17:05:22 | INFO | {
2026-05-08 17:05:22 | INFO |   "action": "tap",
2026-05-08 17:05:22 | INFO |   "region": 3,
2026-05-08 17:05:22 | INFO |   "description": "Tap the 'START LOGGING' button."
2026-05-08 17:05:22 | INFO | }
2026-05-08 17:05:22 | INFO | ```
2026-05-08 17:05:22 | INFO | 🎯 Recovery using region index: 3 at (821, 919)
2026-05-08 17:05:22 | INFO | [1] Tap the 'START LOGGING' button. -> tap
2026-05-08 17:05:22 | INFO | Taking screenshot: /sdcard/screenshot-0.png -> /Users/tanmaybhuskute/Documents/gifdroid-reproduction/apps/batterytemperaturedisplay/llm/ViBR_gemini/handheld/run-001/artifacts/hhv-001/step_3_screenshot-0.png
2026-05-08 17:05:22 | INFO | /Users/tanmaybhuskute/Documents/gifdroid-reproduction/apps/batterytemperaturedisplay/llm/ViBR_gemini/handheld/run-001/artifacts/hhv-001/step_3_tmp_stop.png
2026-05-08 17:05:22 | INFO | /Users/tanmaybhuskute/Documents/gifdroid-reproduction/apps/batterytemperaturedisplay/llm/ViBR_gemini/handheld/run-001/artifacts/hhv-001/step_3_screenshot-0.png
2026-05-08 17:05:22 | INFO | Consistency Response from Gemini: ```json
2026-05-08 17:05:22 | INFO | {
2026-05-08 17:05:22 | INFO |   "same_state": "no",
2026-05-08 17:05:22 | INFO |   "description": "The two screens represent different states of the app's logging feature. The reference screen shows that logging is currently active, indicated by the 'STOP LOGGING' button. The current screen shows that logging is not active, indicated by the 'START LOGGING' button and an error message 'Please enter duration'."
2026-05-08 17:05:22 | INFO | }
2026-05-08 17:05:22 | INFO | ```
2026-05-08 17:05:22 | INFO | ⚠️ Skipping action: current GUI state does not match start state.
2026-05-08 17:05:22 | INFO | Mismatch reason: the two screens represent different states of the app's logging feature. the reference screen shows that logging is currently active, indicated by the 'stop logging' button. the current screen shows that logging is not active, indicated by the 'start logging' button and an error message 'please enter duration'.
2026-05-08 17:05:22 | INFO | 
2026-05-08 17:05:22 | INFO | 📂 Processing segment 4...
2026-05-08 17:05:22 | INFO | Taking screenshot: /sdcard/screenshot-0.png -> /Users/tanmaybhuskute/Documents/gifdroid-reproduction/apps/batterytemperaturedisplay/llm/ViBR_gemini/handheld/run-001/artifacts/hhv-001/step_4_screenshot-0.png
2026-05-08 17:05:22 | INFO | 🔍 Annotated DINO output saved to /Users/tanmaybhuskute/Documents/gifdroid-reproduction/apps/batterytemperaturedisplay/llm/ViBR_gemini/handheld/run-001/artifacts/hhv-001/step_4_dino.png
2026-05-08 17:05:22 | INFO | /Users/tanmaybhuskute/Documents/gifdroid-reproduction/apps/batterytemperaturedisplay/llm/ViBR_gemini/handheld/run-001/artifacts/hhv-001/step_4_dino.png
2026-05-08 17:05:22 | INFO | /Users/tanmaybhuskute/Documents/gifdroid-reproduction/apps/batterytemperaturedisplay/llm/ViBR_gemini/handheld/run-001/artifacts/hhv-001/step_4_tmp_stop.png
2026-05-08 17:05:22 | INFO | Relevant Region Response from Gemini: ```json
2026-05-08 17:05:22 | INFO | {
2026-05-08 17:05:22 | INFO |   "target_regions": [
2026-05-08 17:05:22 | INFO |     6
2026-05-08 17:05:22 | INFO |   ],
2026-05-08 17:05:22 | INFO |   "predicted_action": "tap"
2026-05-08 17:05:22 | INFO | }
2026-05-08 17:05:22 | INFO | ```
2026-05-08 17:05:22 | INFO | 🔍 Relevant regions: {'target_regions': [6], 'predicted_action': 'tap'}
2026-05-08 17:05:22 | INFO | 🧠 GPT selected regions: [6]
2026-05-08 17:05:22 | INFO | ✅ Relevant-only annotation saved to /Users/tanmaybhuskute/Documents/gifdroid-reproduction/apps/batterytemperaturedisplay/llm/ViBR_gemini/handheld/run-001/artifacts/hhv-001/step_4_relevant_regions.png
2026-05-08 17:05:22 | INFO | /Users/tanmaybhuskute/Documents/gifdroid-reproduction/apps/batterytemperaturedisplay/llm/ViBR_gemini/handheld/run-001/artifacts/hhv-001/step_4_relevant_regions.png
2026-05-08 17:05:22 | INFO | /Users/tanmaybhuskute/Documents/gifdroid-reproduction/apps/batterytemperaturedisplay/llm/ViBR_gemini/handheld/run-001/artifacts/hhv-001/step_4_screenshot-0.png
2026-05-08 17:05:22 | INFO | Consistency Response from Gemini: ```json
2026-05-08 17:05:22 | INFO | {
2026-05-08 17:05:22 | INFO |   "same_state": "no",
2026-05-08 17:05:22 | INFO |   "description": "The current screen does not have the keyboard open, so the user cannot perform the intended action of tapping on the number '6'. The reference screen shows the keyboard is active and ready for input. Additionally, the overall layout and available options are significantly different, with the current screen showing more settings at the bottom and a validation error message that is not present in the reference screen."
2026-05-08 17:05:22 | INFO | }
2026-05-08 17:05:22 | INFO | ```
2026-05-08 17:05:22 | INFO | 🔄 Attempting to align state (try 1/3)...
2026-05-08 17:05:22 | INFO | /Users/tanmaybhuskute/Documents/gifdroid-reproduction/apps/batterytemperaturedisplay/llm/ViBR_gemini/handheld/run-001/artifacts/hhv-001/step_4_tmp_start.png
2026-05-08 17:05:22 | INFO | /Users/tanmaybhuskute/Documents/gifdroid-reproduction/apps/batterytemperaturedisplay/llm/ViBR_gemini/handheld/run-001/artifacts/hhv-001/step_4_tmp_stop.png
2026-05-08 17:05:22 | INFO | /Users/tanmaybhuskute/Documents/gifdroid-reproduction/apps/batterytemperaturedisplay/llm/ViBR_gemini/handheld/run-001/artifacts/hhv-001/step_4_labeled.png
2026-05-08 17:05:22 | INFO | Region Action Response from Gemini: ```json
2026-05-08 17:05:22 | INFO | {
2026-05-08 17:05:22 | INFO |   "action": "tap",
2026-05-08 17:05:22 | INFO |   "region": 5,
2026-05-08 17:05:22 | INFO |   "description": "Tap the input field with the text '50' to enter a new alarm temperature."
2026-05-08 17:05:22 | INFO | }
2026-05-08 17:05:22 | INFO | ```
2026-05-08 17:05:22 | INFO | 🎯 Recovery using region index: 5 at (345, 1208)
2026-05-08 17:05:22 | INFO | [1] Tap the input field with the text '50' to enter a new alarm temperature. -> tap
2026-05-08 17:05:22 | INFO | Taking screenshot: /sdcard/screenshot-0.png -> /Users/tanmaybhuskute/Documents/gifdroid-reproduction/apps/batterytemperaturedisplay/llm/ViBR_gemini/handheld/run-001/artifacts/hhv-001/step_4_screenshot-0.png
2026-05-08 17:05:22 | INFO | /Users/tanmaybhuskute/Documents/gifdroid-reproduction/apps/batterytemperaturedisplay/llm/ViBR_gemini/handheld/run-001/artifacts/hhv-001/step_4_tmp_stop.png
2026-05-08 17:05:22 | INFO | /Users/tanmaybhuskute/Documents/gifdroid-reproduction/apps/batterytemperaturedisplay/llm/ViBR_gemini/handheld/run-001/artifacts/hhv-001/step_4_screenshot-0.png
2026-05-08 17:05:22 | INFO | Consistency Response from Gemini: ```json
2026-05-08 17:05:22 | INFO | {
2026-05-08 17:05:22 | INFO |   "same_state": "no",
2026-05-08 17:05:22 | INFO |   "description": "The current screen has a different layout and additional UI elements at the bottom, such as 'Enable Auto Start', 'KILL APP & EXIT', and 'Notification icon text color' options, which are not present in the reference screen. The overall theme is also different (light vs. dark)."
2026-05-08 17:05:22 | INFO | }
2026-05-08 17:05:22 | INFO | ```
2026-05-08 17:05:22 | INFO | 🔄 Attempting to align state (try 2/3)...
2026-05-08 17:05:22 | INFO | /Users/tanmaybhuskute/Documents/gifdroid-reproduction/apps/batterytemperaturedisplay/llm/ViBR_gemini/handheld/run-001/artifacts/hhv-001/step_4_tmp_start.png
2026-05-08 17:05:22 | INFO | /Users/tanmaybhuskute/Documents/gifdroid-reproduction/apps/batterytemperaturedisplay/llm/ViBR_gemini/handheld/run-001/artifacts/hhv-001/step_4_tmp_stop.png
2026-05-08 17:05:22 | INFO | /Users/tanmaybhuskute/Documents/gifdroid-reproduction/apps/batterytemperaturedisplay/llm/ViBR_gemini/handheld/run-001/artifacts/hhv-001/step_4_labeled.png
2026-05-08 17:05:22 | INFO | Region Action Response from Gemini: ```json
2026-05-08 17:05:22 | INFO | {
2026-05-08 17:05:22 | INFO |   "action": "tap",
2026-05-08 17:05:22 | INFO |   "region": 1,
2026-05-08 17:05:22 | INFO |   "description": "Tap the input field for 'Log for' to enter the duration."
2026-05-08 17:05:22 | INFO | }
2026-05-08 17:05:22 | INFO | ```
2026-05-08 17:05:22 | INFO | 🎯 Recovery using region index: 1 at (238, 919)
2026-05-08 17:05:22 | INFO | [1] Tap the input field for 'Log for' to enter the duration. -> tap
2026-05-08 17:05:22 | INFO | Taking screenshot: /sdcard/screenshot-0.png -> /Users/tanmaybhuskute/Documents/gifdroid-reproduction/apps/batterytemperaturedisplay/llm/ViBR_gemini/handheld/run-001/artifacts/hhv-001/step_4_screenshot-0.png
2026-05-08 17:05:22 | INFO | /Users/tanmaybhuskute/Documents/gifdroid-reproduction/apps/batterytemperaturedisplay/llm/ViBR_gemini/handheld/run-001/artifacts/hhv-001/step_4_tmp_stop.png
2026-05-08 17:05:22 | INFO | /Users/tanmaybhuskute/Documents/gifdroid-reproduction/apps/batterytemperaturedisplay/llm/ViBR_gemini/handheld/run-001/artifacts/hhv-001/step_4_screenshot-0.png
2026-05-08 17:05:22 | INFO | Consistency Response from Gemini: ```json
2026-05-08 17:05:22 | INFO | {
2026-05-08 17:05:22 | INFO |   "same_state": "no",
2026-05-08 17:05:22 | INFO |   "description": "The user interface has been significantly redesigned. The reference image has a dark theme and a simpler layout, while the current image has a light theme, a different layout for the temperature display and graph, and additional settings at the bottom of the screen (e.g., 'Enable Auto Start', 'KILL APP & EXIT') that are not present in the reference image. Furthermore, the current screen shows an error message 'Please enter duration', which is not present in the reference screen."
2026-05-08 17:05:22 | INFO | }
2026-05-08 17:05:34 | INFO | ```UserWarning: torch.utils.checkpoint: the use_reentrant parameter should be passed explicitly. Starting in PyTorch 2.9, calling checkpoint without use_reentrant will raise an exception. use_reentrant=False is recommended, but if you need to preserve the current default behavior, you can pass use_reentrant=True. Refer to docs for more details on the differences between the two variants.
2026-05-08 17:05:34 | INFO | UserWarning: None of the inputs have requires_grad=True. Gradients will be None
2026-05-08 17:05:39 | INFO | FutureWarning: `torch.cuda.amp.autocast(args...)` is deprecated. Please use `torch.amp.autocast('cuda', args...)` instead.
2026-05-08 17:07:30 | INFO | 
2026-05-08 17:07:30 | INFO | 🔄 Attempting to align state (try 3/3)...
2026-05-08 17:07:30 | INFO | /Users/tanmaybhuskute/Documents/gifdroid-reproduction/apps/batterytemperaturedisplay/llm/ViBR_gemini/handheld/run-001/artifacts/hhv-001/step_4_tmp_start.png
2026-05-08 17:07:30 | INFO | /Users/tanmaybhuskute/Documents/gifdroid-reproduction/apps/batterytemperaturedisplay/llm/ViBR_gemini/handheld/run-001/artifacts/hhv-001/step_4_tmp_stop.png
2026-05-08 17:07:30 | INFO | /Users/tanmaybhuskute/Documents/gifdroid-reproduction/apps/batterytemperaturedisplay/llm/ViBR_gemini/handheld/run-001/artifacts/hhv-001/step_4_labeled.png
2026-05-08 17:07:30 | INFO | Region Action Response from Gemini: ```json
2026-05-08 17:07:30 | INFO | {
2026-05-08 17:07:30 | INFO |   "action": "tap",
2026-05-08 17:07:30 | INFO |   "region": 3,
2026-05-08 17:07:30 | INFO |   "description": "Tap the 'START LOGGING' button."
2026-05-08 17:07:30 | INFO | }
2026-05-08 17:07:30 | INFO | ```
2026-05-08 17:07:30 | INFO | 🎯 Recovery using region index: 3 at (821, 919)
2026-05-08 17:07:30 | INFO | [1] Tap the 'START LOGGING' button. -> tap
2026-05-08 17:07:30 | INFO | Taking screenshot: /sdcard/screenshot-0.png -> /Users/tanmaybhuskute/Documents/gifdroid-reproduction/apps/batterytemperaturedisplay/llm/ViBR_gemini/handheld/run-001/artifacts/hhv-001/step_4_screenshot-0.png
2026-05-08 17:07:30 | INFO | /Users/tanmaybhuskute/Documents/gifdroid-reproduction/apps/batterytemperaturedisplay/llm/ViBR_gemini/handheld/run-001/artifacts/hhv-001/step_4_tmp_stop.png
2026-05-08 17:07:30 | INFO | /Users/tanmaybhuskute/Documents/gifdroid-reproduction/apps/batterytemperaturedisplay/llm/ViBR_gemini/handheld/run-001/artifacts/hhv-001/step_4_screenshot-0.png
2026-05-08 17:07:30 | INFO | Consistency Response from Gemini: ```json
2026-05-08 17:07:30 | INFO | {
2026-05-08 17:07:30 | INFO |   "same_state": "no",
2026-05-08 17:07:30 | INFO |   "description": "The current screen shows an error state, indicated by the message \"Please enter duration\" and a red exclamation mark next to the \"Log for\" input field. This prevents the user from starting the logging process. The reference screen does not have this error and has a valid duration entered, making it functionally different."
2026-05-08 17:07:30 | INFO | }
2026-05-08 17:07:30 | INFO | ```
2026-05-08 17:07:30 | INFO | ⚠️ Skipping action: current GUI state does not match start state.
2026-05-08 17:07:30 | INFO | Mismatch reason: the current screen shows an error state, indicated by the message "please enter duration" and a red exclamation mark next to the "log for" input field. this prevents the user from starting the logging process. the reference screen does not have this error and has a valid duration entered, making it functionally different.
2026-05-08 17:07:30 | INFO | 
2026-05-08 17:07:30 | INFO | 📂 Processing segment 5...
2026-05-08 17:07:30 | INFO | Taking screenshot: /sdcard/screenshot-0.png -> /Users/tanmaybhuskute/Documents/gifdroid-reproduction/apps/batterytemperaturedisplay/llm/ViBR_gemini/handheld/run-001/artifacts/hhv-001/step_5_screenshot-0.png
2026-05-08 17:07:30 | INFO | 🔍 Annotated DINO output saved to /Users/tanmaybhuskute/Documents/gifdroid-reproduction/apps/batterytemperaturedisplay/llm/ViBR_gemini/handheld/run-001/artifacts/hhv-001/step_5_dino.png
2026-05-08 17:07:30 | INFO | /Users/tanmaybhuskute/Documents/gifdroid-reproduction/apps/batterytemperaturedisplay/llm/ViBR_gemini/handheld/run-001/artifacts/hhv-001/step_5_dino.png
2026-05-08 17:07:30 | INFO | /Users/tanmaybhuskute/Documents/gifdroid-reproduction/apps/batterytemperaturedisplay/llm/ViBR_gemini/handheld/run-001/artifacts/hhv-001/step_5_tmp_stop.png
2026-05-08 17:07:30 | INFO | Relevant Region Response from Gemini: ```json
2026-05-08 17:07:30 | INFO | {
2026-05-08 17:07:30 | INFO |  "target_regions": [],
2026-05-08 17:07:30 | INFO |  "predicted_action": "swipe"
2026-05-08 17:07:30 | INFO | }
2026-05-08 17:07:30 | INFO | ```
2026-05-08 17:07:30 | INFO | 🔍 Relevant regions: {'target_regions': [], 'predicted_action': 'swipe'}
2026-05-08 17:07:30 | INFO | 🧠 GPT selected regions: []
2026-05-08 17:07:30 | INFO | ⚠️ No relevant regions to annotate.
2026-05-08 17:07:30 | INFO | /Users/tanmaybhuskute/Documents/gifdroid-reproduction/apps/batterytemperaturedisplay/llm/ViBR_gemini/handheld/run-001/artifacts/hhv-001/step_5_relevant_regions.png
2026-05-08 17:07:30 | INFO | /Users/tanmaybhuskute/Documents/gifdroid-reproduction/apps/batterytemperaturedisplay/llm/ViBR_gemini/handheld/run-001/artifacts/hhv-001/step_5_screenshot-0.png
2026-05-08 17:07:30 | INFO | Consistency Response from Gemini: ```json
2026-05-08 17:07:30 | INFO | {
2026-05-08 17:07:30 | INFO |   "same_state": "no",
2026-05-08 17:07:30 | INFO |   "description": "The reference image shows the app's page in an app store, while the current image shows the main interface of the running application. These are two completely different screens with different functionalities."
2026-05-08 17:07:30 | INFO | }
2026-05-08 17:07:30 | INFO | ```
2026-05-08 17:07:30 | INFO | 🔄 Attempting to align state (try 1/3)...
2026-05-08 17:07:30 | INFO | /Users/tanmaybhuskute/Documents/gifdroid-reproduction/apps/batterytemperaturedisplay/llm/ViBR_gemini/handheld/run-001/artifacts/hhv-001/step_5_tmp_start.png
2026-05-08 17:07:30 | INFO | /Users/tanmaybhuskute/Documents/gifdroid-reproduction/apps/batterytemperaturedisplay/llm/ViBR_gemini/handheld/run-001/artifacts/hhv-001/step_5_tmp_stop.png
2026-05-08 17:07:30 | INFO | /Users/tanmaybhuskute/Documents/gifdroid-reproduction/apps/batterytemperaturedisplay/llm/ViBR_gemini/handheld/run-001/artifacts/hhv-001/step_5_labeled.png
2026-05-08 17:07:30 | INFO | Region Action Response from Gemini: ```json
2026-05-08 17:07:30 | INFO | {
2026-05-08 17:07:30 | INFO |   "action": "swipe",
2026-05-08 17:07:30 | INFO |   "from": [
2026-05-08 17:07:30 | INFO |     900,
2026-05-08 17:07:30 | INFO |     950
2026-05-08 17:07:30 | INFO |   ],
2026-05-08 17:07:30 | INFO |   "to": [
2026-05-08 17:07:30 | INFO |     200,
2026-05-08 17:07:30 | INFO |     950
2026-05-08 17:07:30 | INFO |   ],
2026-05-08 17:07:30 | INFO |   "duration": 500,
2026-05-08 17:07:30 | INFO |   "description": "Swipe left on the graph to view older data."
2026-05-08 17:07:30 | INFO | }
2026-05-08 17:07:30 | INFO | ```
2026-05-08 17:07:30 | INFO | [1] Swipe left on the graph to view older data. -> swipe
2026-05-08 17:07:30 | INFO | Taking screenshot: /sdcard/screenshot-0.png -> /Users/tanmaybhuskute/Documents/gifdroid-reproduction/apps/batterytemperaturedisplay/llm/ViBR_gemini/handheld/run-001/artifacts/hhv-001/step_5_screenshot-0.png
2026-05-08 17:07:30 | INFO | /Users/tanmaybhuskute/Documents/gifdroid-reproduction/apps/batterytemperaturedisplay/llm/ViBR_gemini/handheld/run-001/artifacts/hhv-001/step_5_tmp_stop.png
2026-05-08 17:07:30 | INFO | /Users/tanmaybhuskute/Documents/gifdroid-reproduction/apps/batterytemperaturedisplay/llm/ViBR_gemini/handheld/run-001/artifacts/hhv-001/step_5_screenshot-0.png
2026-05-08 17:07:30 | INFO | Consistency Response from Gemini: ```json
2026-05-08 17:07:30 | INFO | {
2026-05-08 17:07:30 | INFO |   "same_state": "no",
2026-05-08 17:07:30 | INFO |   "description": "The reference image shows the app's page on an app store, with options to 'Uninstall' or 'Open' the app. The current image shows the main interface of the app itself, after it has been opened. These are two different screens with completely different functionalities."
2026-05-08 17:07:30 | INFO | }
2026-05-08 17:07:30 | INFO | ```
2026-05-08 17:07:30 | INFO | 🔄 Attempting to align state (try 2/3)...
2026-05-08 17:07:30 | INFO | /Users/tanmaybhuskute/Documents/gifdroid-reproduction/apps/batterytemperaturedisplay/llm/ViBR_gemini/handheld/run-001/artifacts/hhv-001/step_5_tmp_start.png
2026-05-08 17:07:30 | INFO | /Users/tanmaybhuskute/Documents/gifdroid-reproduction/apps/batterytemperaturedisplay/llm/ViBR_gemini/handheld/run-001/artifacts/hhv-001/step_5_tmp_stop.png
2026-05-08 17:07:30 | INFO | /Users/tanmaybhuskute/Documents/gifdroid-reproduction/apps/batterytemperaturedisplay/llm/ViBR_gemini/handheld/run-001/artifacts/hhv-001/step_5_labeled.png
2026-05-08 17:07:30 | INFO | Region Action Response from Gemini: ```json
2026-05-08 17:07:30 | INFO | {
2026-05-08 17:07:30 | INFO |     "action": "swipe",
2026-05-08 17:07:30 | INFO |     "from": [
2026-05-08 17:07:30 | INFO |         200,
2026-05-08 17:07:30 | INFO |         750
2026-05-08 17:07:30 | INFO |     ],
2026-05-08 17:07:30 | INFO |     "to": [
2026-05-08 17:07:30 | INFO |         880,
2026-05-08 17:07:30 | INFO |         750
2026-05-08 17:07:30 | INFO |     ],
2026-05-08 17:07:30 | INFO |     "duration": 500,
2026-05-08 17:07:30 | INFO |     "description": "Swipe right on the graph to view older temperature data."
2026-05-08 17:07:30 | INFO | }
2026-05-08 17:07:30 | INFO | ```
2026-05-08 17:07:30 | INFO | [1] Swipe right on the graph to view older temperature data. -> swipe
2026-05-08 17:07:30 | INFO | Taking screenshot: /sdcard/screenshot-0.png -> /Users/tanmaybhuskute/Documents/gifdroid-reproduction/apps/batterytemperaturedisplay/llm/ViBR_gemini/handheld/run-001/artifacts/hhv-001/step_5_screenshot-0.png
2026-05-08 17:07:30 | INFO | /Users/tanmaybhuskute/Documents/gifdroid-reproduction/apps/batterytemperaturedisplay/llm/ViBR_gemini/handheld/run-001/artifacts/hhv-001/step_5_tmp_stop.png
2026-05-08 17:07:30 | INFO | /Users/tanmaybhuskute/Documents/gifdroid-reproduction/apps/batterytemperaturedisplay/llm/ViBR_gemini/handheld/run-001/artifacts/hhv-001/step_5_screenshot-0.png
2026-05-08 17:07:30 | INFO | Consistency Response from Gemini: ```json
2026-05-08 17:07:30 | INFO | {
2026-05-08 17:07:30 | INFO |   "same_state": "no",
2026-05-08 17:07:30 | INFO |   "description": "The reference image shows the app's page in an app store, with options to 'Uninstall' or 'Open'. The current image shows the main interface of the app itself, which is the screen you would see after opening the app. These are two distinct and functionally different states."
2026-05-08 17:07:30 | INFO | }
2026-05-08 17:07:30 | INFO | ```
2026-05-08 17:07:30 | INFO | 🔄 Attempting to align state (try 3/3)...
2026-05-08 17:07:30 | INFO | /Users/tanmaybhuskute/Documents/gifdroid-reproduction/apps/batterytemperaturedisplay/llm/ViBR_gemini/handheld/run-001/artifacts/hhv-001/step_5_tmp_start.png
2026-05-08 17:07:30 | INFO | /Users/tanmaybhuskute/Documents/gifdroid-reproduction/apps/batterytemperaturedisplay/llm/ViBR_gemini/handheld/run-001/artifacts/hhv-001/step_5_tmp_stop.png
2026-05-08 17:07:30 | INFO | /Users/tanmaybhuskute/Documents/gifdroid-reproduction/apps/batterytemperaturedisplay/llm/ViBR_gemini/handheld/run-001/artifacts/hhv-001/step_5_labeled.png
2026-05-08 17:07:30 | INFO | Region Action Response from Gemini: ```json
2026-05-08 17:07:30 | INFO | {
2026-05-08 17:07:30 | INFO |   "action": "swipe",
2026-05-08 17:07:30 | INFO |   "from": [
2026-05-08 17:07:30 | INFO |     900,
2026-05-08 17:07:30 | INFO |     1050
2026-05-08 17:07:30 | INFO |   ],
2026-05-08 17:07:30 | INFO |   "to": [
2026-05-08 17:07:30 | INFO |     200,
2026-05-08 17:07:30 | INFO |     1050
2026-05-08 17:07:30 | INFO |   ],
2026-05-08 17:07:30 | INFO |   "duration": 500,
2026-05-08 17:07:30 | INFO |   "description": "Swipe left on the graph to view historical data."
2026-05-08 17:07:30 | INFO | }
2026-05-08 17:07:30 | INFO | ```
2026-05-08 17:07:30 | INFO | [1] Swipe left on the graph to view historical data. -> swipe
2026-05-08 17:07:30 | INFO | Taking screenshot: /sdcard/screenshot-0.png -> /Users/tanmaybhuskute/Documents/gifdroid-reproduction/apps/batterytemperaturedisplay/llm/ViBR_gemini/handheld/run-001/artifacts/hhv-001/step_5_screenshot-0.png
2026-05-08 17:07:32 | INFO | /Users/tanmaybhuskute/Documents/gifdroid-reproduction/apps/batterytemperaturedisplay/llm/ViBR_gemini/handheld/run-001/artifacts/hhv-001/step_5_tmp_stop.pngUserWarning: torch.utils.checkpoint: the use_reentrant parameter should be passed explicitly. Starting in PyTorch 2.9, calling checkpoint without use_reentrant will raise an exception. use_reentrant=False is recommended, but if you need to preserve the current default behavior, you can pass use_reentrant=True. Refer to docs for more details on the differences between the two variants.
2026-05-08 17:07:32 | INFO | UserWarning: None of the inputs have requires_grad=True. Gradients will be None
2026-05-08 17:07:37 | INFO | FutureWarning: `torch.cuda.amp.autocast(args...)` is deprecated. Please use `torch.amp.autocast('cuda', args...)` instead.
2026-05-08 17:10:03 | INFO | UserWarning: torch.utils.checkpoint: the use_reentrant parameter should be passed explicitly. Starting in PyTorch 2.9, calling checkpoint without use_reentrant will raise an exception. use_reentrant=False is recommended, but if you need to preserve the current default behavior, you can pass use_reentrant=True. Refer to docs for more details on the differences between the two variants.
2026-05-08 17:10:03 | INFO | UserWarning: None of the inputs have requires_grad=True. Gradients will be None
2026-05-08 17:10:08 | INFO | FutureWarning: `torch.cuda.amp.autocast(args...)` is deprecated. Please use `torch.amp.autocast('cuda', args...)` instead.
2026-05-08 17:10:36 | INFO | 
2026-05-08 17:10:36 | INFO | /Users/tanmaybhuskute/Documents/gifdroid-reproduction/apps/batterytemperaturedisplay/llm/ViBR_gemini/handheld/run-001/artifacts/hhv-001/step_5_screenshot-0.png
2026-05-08 17:10:36 | INFO | Consistency Response from Gemini: ```json
2026-05-08 17:10:36 | INFO | {
2026-05-08 17:10:36 | INFO |   "same_state": "no",
2026-05-08 17:10:36 | INFO |   "description": "The reference image shows the app's page on the Google Play Store, with an 'Open' button. The current image shows the main interface of the app itself, which is the screen you see after pressing 'Open'. These are two different states in the user flow."
2026-05-08 17:10:36 | INFO | }
2026-05-08 17:10:36 | INFO | ```
2026-05-08 17:10:36 | INFO | ⚠️ Skipping action: current GUI state does not match start state.
2026-05-08 17:10:36 | INFO | Mismatch reason: the reference image shows the app's page on the google play store, with an 'open' button. the current image shows the main interface of the app itself, which is the screen you see after pressing 'open'. these are two different states in the user flow.
2026-05-08 17:10:36 | INFO | 
2026-05-08 17:10:36 | INFO | 📂 Processing segment 6...
2026-05-08 17:10:36 | INFO | Taking screenshot: /sdcard/screenshot-0.png -> /Users/tanmaybhuskute/Documents/gifdroid-reproduction/apps/batterytemperaturedisplay/llm/ViBR_gemini/handheld/run-001/artifacts/hhv-001/step_6_screenshot-0.png
2026-05-08 17:10:36 | INFO | 🔍 Annotated DINO output saved to /Users/tanmaybhuskute/Documents/gifdroid-reproduction/apps/batterytemperaturedisplay/llm/ViBR_gemini/handheld/run-001/artifacts/hhv-001/step_6_dino.png
2026-05-08 17:10:36 | INFO | /Users/tanmaybhuskute/Documents/gifdroid-reproduction/apps/batterytemperaturedisplay/llm/ViBR_gemini/handheld/run-001/artifacts/hhv-001/step_6_dino.png
2026-05-08 17:10:36 | INFO | /Users/tanmaybhuskute/Documents/gifdroid-reproduction/apps/batterytemperaturedisplay/llm/ViBR_gemini/handheld/run-001/artifacts/hhv-001/step_6_tmp_stop.png
2026-05-08 17:10:36 | INFO | Relevant Region Response from Gemini: ```json
2026-05-08 17:10:36 | INFO | {
2026-05-08 17:10:36 | INFO |   "target_regions": [
2026-05-08 17:10:36 | INFO |     17,
2026-05-08 17:10:36 | INFO |     18,
2026-05-08 17:10:36 | INFO |     19
2026-05-08 17:10:36 | INFO |   ],
2026-05-08 17:10:36 | INFO |   "predicted_action": "tap"
2026-05-08 17:10:36 | INFO | }
2026-05-08 17:10:36 | INFO | ```
2026-05-08 17:10:36 | INFO | 🔍 Relevant regions: {'target_regions': [17, 18, 19], 'predicted_action': 'tap'}
2026-05-08 17:10:36 | INFO | 🧠 GPT selected regions: [17, 18, 19]
2026-05-08 17:10:36 | INFO | ✅ Relevant-only annotation saved to /Users/tanmaybhuskute/Documents/gifdroid-reproduction/apps/batterytemperaturedisplay/llm/ViBR_gemini/handheld/run-001/artifacts/hhv-001/step_6_relevant_regions.png
2026-05-08 17:10:36 | INFO | /Users/tanmaybhuskute/Documents/gifdroid-reproduction/apps/batterytemperaturedisplay/llm/ViBR_gemini/handheld/run-001/artifacts/hhv-001/step_6_relevant_regions.png
2026-05-08 17:10:36 | INFO | /Users/tanmaybhuskute/Documents/gifdroid-reproduction/apps/batterytemperaturedisplay/llm/ViBR_gemini/handheld/run-001/artifacts/hhv-001/step_6_screenshot-0.png
2026-05-08 17:10:36 | INFO | Consistency Response from Gemini: ```json
2026-05-08 17:10:36 | INFO | {
2026-05-08 17:10:36 | INFO |   "same_state": "no",
2026-05-08 17:10:36 | INFO |   "description": "The reference screen shows the app's page on the Google Play Store, where the user can choose to open or uninstall the app. The current screen shows the app itself running. These are two completely different states with different functionalities."
2026-05-08 17:10:36 | INFO | }
2026-05-08 17:10:36 | INFO | ```
2026-05-08 17:10:36 | INFO | 🔄 Attempting to align state (try 1/3)...
2026-05-08 17:10:36 | INFO | /Users/tanmaybhuskute/Documents/gifdroid-reproduction/apps/batterytemperaturedisplay/llm/ViBR_gemini/handheld/run-001/artifacts/hhv-001/step_6_tmp_start.png
2026-05-08 17:10:36 | INFO | /Users/tanmaybhuskute/Documents/gifdroid-reproduction/apps/batterytemperaturedisplay/llm/ViBR_gemini/handheld/run-001/artifacts/hhv-001/step_6_tmp_stop.png
2026-05-08 17:10:36 | INFO | /Users/tanmaybhuskute/Documents/gifdroid-reproduction/apps/batterytemperaturedisplay/llm/ViBR_gemini/handheld/run-001/artifacts/hhv-001/step_6_labeled.png
2026-05-08 17:10:36 | INFO | Region Action Response from Gemini: ```json
2026-05-08 17:10:36 | INFO | {
2026-05-08 17:10:36 | INFO |   "action": "no action",
2026-05-08 17:10:36 | INFO |   "description": "The action in the recording was to open the app, and the current screen is already the opened app. Therefore, no action is needed."
2026-05-08 17:10:36 | INFO | }
2026-05-08 17:10:36 | INFO | ```
2026-05-08 17:10:36 | INFO | [1] The action in the recording was to open the app, and the current screen is already the opened app. Therefore, no action is needed. -> no action
2026-05-08 17:10:36 | INFO | Taking screenshot: /sdcard/screenshot-0.png -> /Users/tanmaybhuskute/Documents/gifdroid-reproduction/apps/batterytemperaturedisplay/llm/ViBR_gemini/handheld/run-001/artifacts/hhv-001/step_6_screenshot-0.png
2026-05-08 17:10:36 | INFO | /Users/tanmaybhuskute/Documents/gifdroid-reproduction/apps/batterytemperaturedisplay/llm/ViBR_gemini/handheld/run-001/artifacts/hhv-001/step_6_tmp_stop.png
2026-05-08 17:10:36 | INFO | /Users/tanmaybhuskute/Documents/gifdroid-reproduction/apps/batterytemperaturedisplay/llm/ViBR_gemini/handheld/run-001/artifacts/hhv-001/step_6_screenshot-0.png
2026-05-08 17:10:36 | INFO | Consistency Response from Gemini: ```json
2026-05-08 17:10:36 | INFO | {
2026-05-08 17:10:36 | INFO |   "same_state": "no",
2026-05-08 17:10:36 | INFO |   "description": "The reference image shows the Google Play Store page for the app, while the current image shows the main screen of the app itself. These are two different screens with completely different functionalities."
2026-05-08 17:10:36 | INFO | }
2026-05-08 17:10:36 | INFO | ```
2026-05-08 17:10:36 | INFO | 🔄 Attempting to align state (try 2/3)...
2026-05-08 17:10:36 | INFO | /Users/tanmaybhuskute/Documents/gifdroid-reproduction/apps/batterytemperaturedisplay/llm/ViBR_gemini/handheld/run-001/artifacts/hhv-001/step_6_tmp_start.png
2026-05-08 17:10:36 | INFO | /Users/tanmaybhuskute/Documents/gifdroid-reproduction/apps/batterytemperaturedisplay/llm/ViBR_gemini/handheld/run-001/artifacts/hhv-001/step_6_tmp_stop.png
2026-05-08 17:10:36 | INFO | /Users/tanmaybhuskute/Documents/gifdroid-reproduction/apps/batterytemperaturedisplay/llm/ViBR_gemini/handheld/run-001/artifacts/hhv-001/step_6_labeled.png
2026-05-08 17:10:36 | INFO | Region Action Response from Gemini: ```json
2026-05-08 17:10:36 | INFO | {
2026-05-08 17:10:36 | INFO |   "action": "no action",
2026-05-08 17:10:36 | INFO |   "description": "The app is already open, which was the result of tapping 'Open' in the Play Store."
2026-05-08 17:10:36 | INFO | }
2026-05-08 17:10:36 | INFO | ```
2026-05-08 17:10:36 | INFO | [1] The app is already open, which was the result of tapping 'Open' in the Play Store. -> no action
2026-05-08 17:10:36 | INFO | Taking screenshot: /sdcard/screenshot-0.png -> /Users/tanmaybhuskute/Documents/gifdroid-reproduction/apps/batterytemperaturedisplay/llm/ViBR_gemini/handheld/run-001/artifacts/hhv-001/step_6_screenshot-0.png
2026-05-08 17:10:36 | INFO | /Users/tanmaybhuskute/Documents/gifdroid-reproduction/apps/batterytemperaturedisplay/llm/ViBR_gemini/handheld/run-001/artifacts/hhv-001/step_6_tmp_stop.png
2026-05-08 17:10:36 | INFO | /Users/tanmaybhuskute/Documents/gifdroid-reproduction/apps/batterytemperaturedisplay/llm/ViBR_gemini/handheld/run-001/artifacts/hhv-001/step_6_screenshot-0.png
2026-05-08 17:10:36 | INFO | Consistency Response from Gemini: ```json
2026-05-08 17:10:36 | INFO | {
2026-05-08 17:10:36 | INFO |   "same_state": "no",
2026-05-08 17:10:36 | INFO |   "description": "The reference image shows the app's page on the Google Play Store, from where the app can be opened. The current image shows the main interface of the app itself, which is the state after the app has been opened. These are two different functional states."
2026-05-08 17:10:36 | INFO | }
2026-05-08 17:10:36 | INFO | ```
2026-05-08 17:10:36 | INFO | 🔄 Attempting to align state (try 3/3)...
2026-05-08 17:10:36 | INFO | /Users/tanmaybhuskute/Documents/gifdroid-reproduction/apps/batterytemperaturedisplay/llm/ViBR_gemini/handheld/run-001/artifacts/hhv-001/step_6_tmp_start.png
2026-05-08 17:10:36 | INFO | /Users/tanmaybhuskute/Documents/gifdroid-reproduction/apps/batterytemperaturedisplay/llm/ViBR_gemini/handheld/run-001/artifacts/hhv-001/step_6_tmp_stop.png
2026-05-08 17:10:36 | INFO | /Users/tanmaybhuskute/Documents/gifdroid-reproduction/apps/batterytemperaturedisplay/llm/ViBR_gemini/handheld/run-001/artifacts/hhv-001/step_6_labeled.png
2026-05-08 17:10:36 | INFO | Region Action Response from Gemini: ```json
2026-05-08 17:10:36 | INFO | {
2026-05-08 17:10:36 | INFO |   "action": "no action",
2026-05-08 17:10:36 | INFO |   "description": "No action is needed as the app is already open."
2026-05-08 17:10:36 | INFO | }
2026-05-08 17:10:36 | INFO | ```
2026-05-08 17:10:36 | INFO | [1] No action is needed as the app is already open. -> no action
2026-05-08 17:10:36 | INFO | Taking screenshot: /sdcard/screenshot-0.png -> /Users/tanmaybhuskute/Documents/gifdroid-reproduction/apps/batterytemperaturedisplay/llm/ViBR_gemini/handheld/run-001/artifacts/hhv-001/step_6_screenshot-0.png
2026-05-08 17:10:36 | INFO | /Users/tanmaybhuskute/Documents/gifdroid-reproduction/apps/batterytemperaturedisplay/llm/ViBR_gemini/handheld/run-001/artifacts/hhv-001/step_6_tmp_stop.png
2026-05-08 17:10:36 | INFO | /Users/tanmaybhuskute/Documents/gifdroid-reproduction/apps/batterytemperaturedisplay/llm/ViBR_gemini/handheld/run-001/artifacts/hhv-001/step_6_screenshot-0.png
2026-05-08 17:10:36 | INFO | Consistency Response from Gemini: ```json
2026-05-08 17:10:36 | INFO | {
2026-05-08 17:10:36 | INFO |   "same_state": "no",
2026-05-08 17:10:36 | INFO |   "description": "The reference image shows the app's page on the Google Play Store, with an 'Open' button. The current image shows the main interface of the app itself after it has been opened. These are two different screens and do not offer the same functionality."
2026-05-08 17:10:36 | INFO | }
2026-05-08 17:10:36 | INFO | ```
2026-05-08 17:10:36 | INFO | ⚠️ Skipping action: current GUI state does not match start state.
2026-05-08 17:10:36 | INFO | Mismatch reason: the reference image shows the app's page on the google play store, with an 'open' button. the current image shows the main interface of the app itself after it has been opened. these are two different screens and do not offer the same functionality.
2026-05-08 17:10:36 | INFO | 
2026-05-08 17:10:36 | INFO | 📂 Processing segment 7...
2026-05-08 17:12:05 | INFO | Taking screenshot: /sdcard/screenshot-0.png -> /Users/tanmaybhuskute/Documents/gifdroid-reproduction/apps/batterytemperaturedisplay/llm/ViBR_gemini/handheld/run-001/artifacts/hhv-001/step_7_screenshot-0.png
2026-05-08 17:12:05 | INFO | 🔍 Annotated DINO output saved to /Users/tanmaybhuskute/Documents/gifdroid-reproduction/apps/batterytemperaturedisplay/llm/ViBR_gemini/handheld/run-001/artifacts/hhv-001/step_7_dino.png
2026-05-08 17:12:05 | INFO | /Users/tanmaybhuskute/Documents/gifdroid-reproduction/apps/batterytemperaturedisplay/llm/ViBR_gemini/handheld/run-001/artifacts/hhv-001/step_7_dino.png
2026-05-08 17:12:05 | INFO | /Users/tanmaybhuskute/Documents/gifdroid-reproduction/apps/batterytemperaturedisplay/llm/ViBR_gemini/handheld/run-001/artifacts/hhv-001/step_7_tmp_stop.png
2026-05-08 17:12:05 | INFO | Relevant Region Response from Gemini: ```json
2026-05-08 17:12:05 | INFO | {
2026-05-08 17:12:05 | INFO |   "target_regions": [
2026-05-08 17:12:05 | INFO |     15
2026-05-08 17:12:05 | INFO |   ],
2026-05-08 17:12:05 | INFO |   "predicted_action": "swipe"
2026-05-08 17:12:05 | INFO | }
2026-05-08 17:12:05 | INFO | ```
2026-05-08 17:12:05 | INFO | 🔍 Relevant regions: {'target_regions': [15], 'predicted_action': 'swipe'}
2026-05-08 17:12:05 | INFO | 🧠 GPT selected regions: [15]
2026-05-08 17:12:05 | INFO | ✅ Relevant-only annotation saved to /Users/tanmaybhuskute/Documents/gifdroid-reproduction/apps/batterytemperaturedisplay/llm/ViBR_gemini/handheld/run-001/artifacts/hhv-001/step_7_relevant_regions.png
2026-05-08 17:12:05 | INFO | /Users/tanmaybhuskute/Documents/gifdroid-reproduction/apps/batterytemperaturedisplay/llm/ViBR_gemini/handheld/run-001/artifacts/hhv-001/step_7_relevant_regions.png
2026-05-08 17:12:05 | INFO | /Users/tanmaybhuskute/Documents/gifdroid-reproduction/apps/batterytemperaturedisplay/llm/ViBR_gemini/handheld/run-001/artifacts/hhv-001/step_7_screenshot-0.png
2026-05-08 17:12:05 | INFO | Consistency Response from Gemini: ```json
2026-05-08 17:12:05 | INFO | {
2026-05-08 17:12:05 | INFO |   "same_state": "no",
2026-05-08 17:12:05 | INFO |   "description": "The reference screen shows the app's page on the Google Play Store, while the current screen is the main interface of the app itself. These are two completely different states in different applications."
2026-05-08 17:12:05 | INFO | }
2026-05-08 17:12:05 | INFO | ```
2026-05-08 17:12:05 | INFO | 🔄 Attempting to align state (try 1/3)...
2026-05-08 17:12:05 | INFO | /Users/tanmaybhuskute/Documents/gifdroid-reproduction/apps/batterytemperaturedisplay/llm/ViBR_gemini/handheld/run-001/artifacts/hhv-001/step_7_tmp_start.png
2026-05-08 17:12:05 | INFO | /Users/tanmaybhuskute/Documents/gifdroid-reproduction/apps/batterytemperaturedisplay/llm/ViBR_gemini/handheld/run-001/artifacts/hhv-001/step_7_tmp_stop.png
2026-05-08 17:12:05 | INFO | /Users/tanmaybhuskute/Documents/gifdroid-reproduction/apps/batterytemperaturedisplay/llm/ViBR_gemini/handheld/run-001/artifacts/hhv-001/step_7_labeled.png
2026-05-08 17:12:05 | INFO | Region Action Response from Gemini: ```json
2026-05-08 17:12:05 | INFO | {
2026-05-08 17:12:05 | INFO |   "action": "swipe",
2026-05-08 17:12:05 | INFO |   "from": [
2026-05-08 17:12:05 | INFO |     843,
2026-05-08 17:12:05 | INFO |     520
2026-05-08 17:12:05 | INFO |   ],
2026-05-08 17:12:05 | INFO |   "to": [
2026-05-08 17:12:05 | INFO |     236,
2026-05-08 17:12:05 | INFO |     520
2026-05-08 17:12:05 | INFO |   ],
2026-05-08 17:12:05 | INFO |   "duration": 500,
2026-05-08 17:12:05 | INFO |   "description": "swipe left on graph"
2026-05-08 17:12:05 | INFO | }
2026-05-08 17:12:05 | INFO | ```
2026-05-08 17:12:05 | INFO | [1] swipe left on graph -> swipe
2026-05-08 17:12:05 | INFO | Taking screenshot: /sdcard/screenshot-0.png -> /Users/tanmaybhuskute/Documents/gifdroid-reproduction/apps/batterytemperaturedisplay/llm/ViBR_gemini/handheld/run-001/artifacts/hhv-001/step_7_screenshot-0.png
2026-05-08 17:12:05 | INFO | /Users/tanmaybhuskute/Documents/gifdroid-reproduction/apps/batterytemperaturedisplay/llm/ViBR_gemini/handheld/run-001/artifacts/hhv-001/step_7_tmp_stop.png
2026-05-08 17:12:05 | INFO | /Users/tanmaybhuskute/Documents/gifdroid-reproduction/apps/batterytemperaturedisplay/llm/ViBR_gemini/handheld/run-001/artifacts/hhv-001/step_7_screenshot-0.png
2026-05-08 17:12:05 | INFO | Consistency Response from Gemini: ```json
2026-05-08 17:12:05 | INFO | {
2026-05-08 17:12:05 | INFO |   "same_state": "no",
2026-05-08 17:12:05 | INFO |   "description": "The reference image shows the app's page on the Google Play Store, with options to 'Uninstall' or 'Open' the app. The current image shows the main interface of the app itself after it has been opened. These are two different screens with completely different functionalities."
2026-05-08 17:12:05 | INFO | }
2026-05-08 17:12:05 | INFO | ```
2026-05-08 17:12:05 | INFO | 🔄 Attempting to align state (try 2/3)...
2026-05-08 17:12:05 | INFO | /Users/tanmaybhuskute/Documents/gifdroid-reproduction/apps/batterytemperaturedisplay/llm/ViBR_gemini/handheld/run-001/artifacts/hhv-001/step_7_tmp_start.png
2026-05-08 17:12:05 | INFO | /Users/tanmaybhuskute/Documents/gifdroid-reproduction/apps/batterytemperaturedisplay/llm/ViBR_gemini/handheld/run-001/artifacts/hhv-001/step_7_tmp_stop.png
2026-05-08 17:12:05 | INFO | /Users/tanmaybhuskute/Documents/gifdroid-reproduction/apps/batterytemperaturedisplay/llm/ViBR_gemini/handheld/run-001/artifacts/hhv-001/step_7_labeled.png
2026-05-08 17:12:05 | INFO | Region Action Response from Gemini: ```json
2026-05-08 17:12:05 | INFO | {
2026-05-08 17:12:05 | INFO |   "action": "swipe",
2026-05-08 17:12:05 | INFO |   "from": [216, 850],
2026-05-08 17:12:05 | INFO |   "to": [864, 850],
2026-05-08 17:12:05 | INFO |   "duration": 500,
2026-05-08 17:12:05 | INFO |   "description": "Swipe right on the graph."
2026-05-08 17:12:05 | INFO | }
2026-05-08 17:12:05 | INFO | ```
2026-05-08 17:12:05 | INFO | [1] Swipe right on the graph. -> swipe
2026-05-08 17:12:05 | INFO | Taking screenshot: /sdcard/screenshot-0.png -> /Users/tanmaybhuskute/Documents/gifdroid-reproduction/apps/batterytemperaturedisplay/llm/ViBR_gemini/handheld/run-001/artifacts/hhv-001/step_7_screenshot-0.png
2026-05-08 17:12:05 | INFO | /Users/tanmaybhuskute/Documents/gifdroid-reproduction/apps/batterytemperaturedisplay/llm/ViBR_gemini/handheld/run-001/artifacts/hhv-001/step_7_tmp_stop.png
2026-05-08 17:12:05 | INFO | /Users/tanmaybhuskute/Documents/gifdroid-reproduction/apps/batterytemperaturedisplay/llm/ViBR_gemini/handheld/run-001/artifacts/hhv-001/step_7_screenshot-0.png
2026-05-08 17:12:05 | INFO | Consistency Response from Gemini: ```json
2026-05-08 17:12:05 | INFO | {
2026-05-08 17:12:05 | INFO |   "same_state": "no",
2026-05-08 17:12:05 | INFO |   "description": "The two images show completely different screens. The first image is the app's page on the Google Play Store, with options to 'Uninstall' or 'Open' the app. The second image is the main interface of the app itself, after it has been opened, showing temperature readings and settings. The user cannot perform the same actions on both screens."
2026-05-08 17:12:05 | INFO | }
2026-05-08 17:12:05 | INFO | ```
2026-05-08 17:12:05 | INFO | 🔄 Attempting to align state (try 3/3)...
2026-05-08 17:12:05 | INFO | /Users/tanmaybhuskute/Documents/gifdroid-reproduction/apps/batterytemperaturedisplay/llm/ViBR_gemini/handheld/run-001/artifacts/hhv-001/step_7_tmp_start.png
2026-05-08 17:12:05 | INFO | /Users/tanmaybhuskute/Documents/gifdroid-reproduction/apps/batterytemperaturedisplay/llm/ViBR_gemini/handheld/run-001/artifacts/hhv-001/step_7_tmp_stop.png
2026-05-08 17:12:05 | INFO | /Users/tanmaybhuskute/Documents/gifdroid-reproduction/apps/batterytemperaturedisplay/llm/ViBR_gemini/handheld/run-001/artifacts/hhv-001/step_7_labeled.png
2026-05-08 17:12:05 | INFO | Region Action Response from Gemini: ```json
2026-05-08 17:12:05 | INFO | {
2026-05-08 17:12:05 | INFO |   "action": "swipe",
2026-05-08 17:12:05 | INFO |   "from": [
2026-05-08 17:12:05 | INFO |     900,
2026-05-08 17:12:05 | INFO |     950
2026-05-08 17:12:05 | INFO |   ],
2026-05-08 17:12:05 | INFO |   "to": [
2026-05-08 17:12:05 | INFO |     200,
2026-05-08 17:12:05 | INFO |     950
2026-05-08 17:12:05 | INFO |   ],
2026-05-08 17:12:05 | INFO |   "duration": 500,
2026-05-08 17:12:05 | INFO |   "description": "Swipe left on the graph."
2026-05-08 17:12:05 | INFO | }
2026-05-08 17:12:05 | INFO | ```
2026-05-08 17:12:05 | INFO | [1] Swipe left on the graph. -> swipe
2026-05-08 17:12:05 | INFO | Taking screenshot: /sdcard/screenshot-0.png -> /Users/tanmaybhuskute/Documents/gifdroid-reproduction/apps/batterytemperaturedisplay/llm/ViBR_gemini/handheld/run-001/artifacts/hhv-001/step_7_screenshot-0.png
2026-05-08 17:12:05 | INFO | /Users/tanmaybhuskute/Documents/gifdroid-reproduction/apps/batterytemperaturedisplay/llm/ViBR_gemini/handheld/run-001/artifacts/hhv-001/step_7_tmp_stop.png
2026-05-08 17:12:05 | INFO | /Users/tanmaybhuskute/Documents/gifdroid-reproduction/apps/batterytemperaturedisplay/llm/ViBR_gemini/handheld/run-001/artifacts/hhv-001/step_7_screenshot-0.png
2026-05-08 17:12:05 | INFO | Consistency Response from Gemini: ```json
2026-05-08 17:12:05 | INFO | {
2026-05-08 17:12:05 | INFO |   "same_state": "no",
2026-05-08 17:12:05 | INFO |   "description": "The reference image shows the app's page on the Google Play Store, with options to 'Uninstall' or 'Open' the app. The current image shows the main interface of the app itself after it has been opened. These are two distinct screens with different functionalities."
2026-05-08 17:12:05 | INFO | }
2026-05-08 17:12:05 | INFO | ```
2026-05-08 17:12:05 | INFO | ⚠️ Skipping action: current GUI state does not match start state.
2026-05-08 17:12:05 | INFO | Mismatch reason: the reference image shows the app's page on the google play store, with options to 'uninstall' or 'open' the app. the current image shows the main interface of the app itself after it has been opened. these are two distinct screens with different functionalities.
2026-05-08 17:12:05 | INFO | 
2026-05-08 17:12:05 | INFO | 📂 Processing segment 8...
2026-05-08 17:12:05 | INFO | Taking screenshot: /sdcard/screenshot-0.png -> /Users/tanmaybhuskute/Documents/gifdroid-reproduction/apps/batterytemperaturedisplay/llm/ViBR_gemini/handheld/run-001/artifacts/hhv-001/step_8_screenshot-0.png
2026-05-08 17:12:05 | INFO | 🔍 Annotated DINO output saved to /Users/tanmaybhuskute/Documents/gifdroid-reproduction/apps/batterytemperaturedisplay/llm/ViBR_gemini/handheld/run-001/artifacts/hhv-001/step_8_dino.png
2026-05-08 17:12:05 | INFO | /Users/tanmaybhuskute/Documents/gifdroid-reproduction/apps/batterytemperaturedisplay/llm/ViBR_gemini/handheld/run-001/artifacts/hhv-001/step_8_dino.png
2026-05-08 17:12:05 | INFO | /Users/tanmaybhuskute/Documents/gifdroid-reproduction/apps/batterytemperaturedisplay/llm/ViBR_gemini/handheld/run-001/artifacts/hhv-001/step_8_tmp_stop.png
2026-05-08 17:12:05 | INFO | Relevant Region Response from Gemini: ```json
2026-05-08 17:12:05 | INFO | {
2026-05-08 17:12:05 | INFO |   "target_regions": [],
2026-05-08 17:12:05 | INFO |   "predicted_action": "swipe"
2026-05-08 17:12:05 | INFO | }
2026-05-08 17:12:05 | INFO | ```
2026-05-08 17:12:05 | INFO | 🔍 Relevant regions: {'target_regions': [], 'predicted_action': 'swipe'}
2026-05-08 17:12:05 | INFO | 🧠 GPT selected regions: []
2026-05-08 17:12:05 | INFO | ⚠️ No relevant regions to annotate.
2026-05-08 17:12:05 | INFO | /Users/tanmaybhuskute/Documents/gifdroid-reproduction/apps/batterytemperaturedisplay/llm/ViBR_gemini/handheld/run-001/artifacts/hhv-001/step_8_relevant_regions.png
2026-05-08 17:12:05 | INFO | /Users/tanmaybhuskute/Documents/gifdroid-reproduction/apps/batterytemperaturedisplay/llm/ViBR_gemini/handheld/run-001/artifacts/hhv-001/step_8_screenshot-0.png
2026-05-08 17:12:05 | INFO | Consistency Response from Gemini: ```json
2026-05-08 17:12:05 | INFO | {
2026-05-08 17:12:05 | INFO |   "same_state": "no",
2026-05-08 17:12:05 | INFO |   "description": "The reference screen shows the app's page on the Google Play Store, where the user can open or uninstall the app. The current screen shows the main interface of the app itself, which is displayed after the app has been opened. These are two completely different states with different functionalities."
2026-05-08 17:12:05 | INFO | }
2026-05-08 17:12:05 | INFO | ```
2026-05-08 17:12:05 | INFO | 🔄 Attempting to align state (try 1/3)...
2026-05-08 17:12:05 | INFO | /Users/tanmaybhuskute/Documents/gifdroid-reproduction/apps/batterytemperaturedisplay/llm/ViBR_gemini/handheld/run-001/artifacts/hhv-001/step_8_tmp_start.png
2026-05-08 17:12:05 | INFO | /Users/tanmaybhuskute/Documents/gifdroid-reproduction/apps/batterytemperaturedisplay/llm/ViBR_gemini/handheld/run-001/artifacts/hhv-001/step_8_tmp_stop.png
2026-05-08 17:12:05 | INFO | /Users/tanmaybhuskute/Documents/gifdroid-reproduction/apps/batterytemperaturedisplay/llm/ViBR_gemini/handheld/run-001/artifacts/hhv-001/step_8_labeled.png
2026-05-08 17:12:05 | INFO | Region Action Response from Gemini: ```json
2026-05-08 17:12:05 | INFO | {
2026-05-08 17:12:05 | INFO |     "action": "swipe",
2026-05-08 17:12:05 | INFO |     "from": [
2026-05-08 17:12:05 | INFO |         810,
2026-05-08 17:12:05 | INFO |         982
2026-05-08 17:12:05 | INFO |     ],
2026-05-08 17:12:05 | INFO |     "to": [
2026-05-08 17:12:05 | INFO |         270,
2026-05-08 17:12:05 | INFO |         982
2026-05-08 17:12:05 | INFO |     ],
2026-05-08 17:12:05 | INFO |     "duration": 500,
2026-05-08 17:12:05 | INFO |     "description": "Swipe left on the graph."
2026-05-08 17:12:05 | INFO | }
2026-05-08 17:12:05 | INFO | ```
2026-05-08 17:12:05 | INFO | [1] Swipe left on the graph. -> swipe
2026-05-08 17:12:05 | INFO | Taking screenshot: /sdcard/screenshot-0.png -> /Users/tanmaybhuskute/Documents/gifdroid-reproduction/apps/batterytemperaturedisplay/llm/ViBR_gemini/handheld/run-001/artifacts/hhv-001/step_8_screenshot-0.png
2026-05-08 17:12:05 | INFO | /Users/tanmaybhuskute/Documents/gifdroid-reproduction/apps/batterytemperaturedisplay/llm/ViBR_gemini/handheld/run-001/artifacts/hhv-001/step_8_tmp_stop.png
2026-05-08 17:12:05 | INFO | /Users/tanmaybhuskute/Documents/gifdroid-reproduction/apps/batterytemperaturedisplay/llm/ViBR_gemini/handheld/run-001/artifacts/hhv-001/step_8_screenshot-0.png
2026-05-08 17:12:05 | INFO | Consistency Response from Gemini: ```json
2026-05-08 17:12:05 | INFO | {
2026-05-08 17:12:05 | INFO |   "same_state": "no",
2026-05-08 17:12:05 | INFO |   "description": "The reference screen is the Google Play Store page for the app, showing options to 'Uninstall' or 'Open' the app. The current screen is the main interface of the app itself, which is what you would see after opening it. The two screens represent completely different states and offer different functionalities."
2026-05-08 17:12:05 | INFO | }
2026-05-08 17:12:05 | INFO | ```
2026-05-08 17:12:05 | INFO | 🔄 Attempting to align state (try 2/3)...
2026-05-08 17:12:05 | INFO | /Users/tanmaybhuskute/Documents/gifdroid-reproduction/apps/batterytemperaturedisplay/llm/ViBR_gemini/handheld/run-001/artifacts/hhv-001/step_8_tmp_start.png
2026-05-08 17:12:05 | INFO | /Users/tanmaybhuskute/Documents/gifdroid-reproduction/apps/batterytemperaturedisplay/llm/ViBR_gemini/handheld/run-001/artifacts/hhv-001/step_8_tmp_stop.png
2026-05-08 17:12:05 | INFO | /Users/tanmaybhuskute/Documents/gifdroid-reproduction/apps/batterytemperaturedisplay/llm/ViBR_gemini/handheld/run-001/artifacts/hhv-001/step_8_labeled.png
2026-05-08 17:12:05 | INFO | Region Action Response from Gemini: ```json
2026-05-08 17:12:05 | INFO | {
2026-05-08 17:12:05 | INFO |     "action": "swipe",
2026-05-08 17:12:05 | INFO |     "from": [
2026-05-08 17:12:05 | INFO |         816,
2026-05-08 17:12:05 | INFO |         892
2026-05-08 17:12:05 | INFO |     ],
2026-05-08 17:12:05 | INFO |     "to": [
2026-05-08 17:12:05 | INFO |         231,
2026-05-08 17:12:05 | INFO |         892
2026-05-08 17:12:05 | INFO |     ],
2026-05-08 17:12:05 | INFO |     "duration": 500,
2026-05-08 17:12:05 | INFO |     "description": "Swipe left on the graph."
2026-05-08 17:12:05 | INFO | }
2026-05-08 17:12:05 | INFO | ```
2026-05-08 17:12:05 | INFO | [1] Swipe left on the graph. -> swipe
2026-05-08 17:12:05 | INFO | Taking screenshot: /sdcard/screenshot-0.png -> /Users/tanmaybhuskute/Documents/gifdroid-reproduction/apps/batterytemperaturedisplay/llm/ViBR_gemini/handheld/run-001/artifacts/hhv-001/step_8_screenshot-0.png
2026-05-08 17:12:05 | INFO | /Users/tanmaybhuskute/Documents/gifdroid-reproduction/apps/batterytemperaturedisplay/llm/ViBR_gemini/handheld/run-001/artifacts/hhv-001/step_8_tmp_stop.png
2026-05-08 17:12:05 | INFO | /Users/tanmaybhuskute/Documents/gifdroid-reproduction/apps/batterytemperaturedisplay/llm/ViBR_gemini/handheld/run-001/artifacts/hhv-001/step_8_screenshot-0.png
2026-05-08 17:12:05 | INFO | Consistency Response from Gemini: ```json
2026-05-08 17:12:05 | INFO | {
2026-05-08 17:12:05 | INFO |   "same_state": "no",
2026-05-08 17:12:05 | INFO |   "description": "The reference image shows the app's page on the Google Play Store, while the current image shows the main screen of the app itself. These are two completely different screens with different functionalities."
2026-05-08 17:12:05 | INFO | }
2026-05-08 17:12:05 | INFO | ```
2026-05-08 17:12:05 | INFO | 🔄 Attempting to align state (try 3/3)...
2026-05-08 17:12:05 | INFO | /Users/tanmaybhuskute/Documents/gifdroid-reproduction/apps/batterytemperaturedisplay/llm/ViBR_gemini/handheld/run-001/artifacts/hhv-001/step_8_tmp_start.png
2026-05-08 17:12:05 | INFO | /Users/tanmaybhuskute/Documents/gifdroid-reproduction/apps/batterytemperaturedisplay/llm/ViBR_gemini/handheld/run-001/artifacts/hhv-001/step_8_tmp_stop.png
2026-05-08 17:12:05 | INFO | /Users/tanmaybhuskute/Documents/gifdroid-reproduction/apps/batterytemperaturedisplay/llm/ViBR_gemini/handheld/run-001/artifacts/hhv-001/step_8_labeled.png
2026-05-08 17:12:05 | INFO | Region Action Response from Gemini: ```json
2026-05-08 17:12:05 | INFO | {
2026-05-08 17:12:05 | INFO |   "action": "swipe",
2026-05-08 17:12:05 | INFO |   "from": [
2026-05-08 17:12:05 | INFO |     800,
2026-05-08 17:12:05 | INFO |     400
2026-05-08 17:12:05 | INFO |   ],
2026-05-08 17:12:05 | INFO |   "to": [
2026-05-08 17:12:05 | INFO |     200,
2026-05-08 17:12:05 | INFO |     400
2026-05-08 17:12:05 | INFO |   ],
2026-05-08 17:12:05 | INFO |   "duration": 500,
2026-05-08 17:12:05 | INFO |   "description": "Swipe left on the graph."
2026-05-08 17:12:05 | INFO | }
2026-05-08 17:12:05 | INFO | ```
2026-05-08 17:12:05 | INFO | [1] Swipe left on the graph. -> swipe
2026-05-08 17:12:05 | INFO | Taking screenshot: /sdcard/screenshot-0.png -> /Users/tanmaybhuskute/Documents/gifdroid-reproduction/apps/batterytemperaturedisplay/llm/ViBR_gemini/handheld/run-001/artifacts/hhv-001/step_8_screenshot-0.png
2026-05-08 17:12:05 | INFO | /Users/tanmaybhuskute/Documents/gifdroid-reproduction/apps/batterytemperaturedisplay/llm/ViBR_gemini/handheld/run-001/artifacts/hhv-001/step_8_tmp_stop.png
2026-05-08 17:12:05 | INFO | /Users/tanmaybhuskute/Documents/gifdroid-reproduction/apps/batterytemperaturedisplay/llm/ViBR_gemini/handheld/run-001/artifacts/hhv-001/step_8_screenshot-0.png
2026-05-08 17:12:05 | INFO | Consistency Response from Gemini: ```json
2026-05-08 17:12:05 | INFO | {
2026-05-08 17:12:05 | INFO |   "same_state": "no",
2026-05-08 17:12:05 | INFO |   "description": "The reference image shows the app's page on the Google Play Store, while the current image shows the main interface of the app itself after it has been opened. These are two different states with completely different functionalities."
2026-05-08 17:12:05 | INFO | }
2026-05-08 17:12:05 | INFO | ```
2026-05-08 17:12:05 | INFO | ⚠️ Skipping action: current GUI state does not match start state.
2026-05-08 17:12:05 | INFO | Mismatch reason: the reference image shows the app's page on the google play store, while the current image shows the main interface of the app itself after it has been opened. these are two different states with completely different functionalities.
2026-05-08 17:12:05 | INFO | ✅ Video processing completed.
2026-05-08 17:12:05 | INFO | 📝 Summary saved to /Users/tanmaybhuskute/Documents/gifdroid-reproduction/apps/batterytemperaturedisplay/llm/ViBR_gemini/handheld/run-001/artifacts/hhv-001/memory.md
2026-05-08 17:12:08 | INFO | ========================================================================
RUN SUMMARY
  App         : batterytemperaturedisplay
  Video type  : handheld
  Status      : success
  Scenes      : 9/9
  Actions     : unknown=9
  LLM calls   : action_inference=24  region_detection=9  state_comparison=30
  LLM latency : min=5.2s  max=71.5s  avg=16.5s  total=1038.4s
  Tokens used : prompt=61,553  output=3,920  total=65,473
  Wall time   : 20m 54s
========================================================================

```
