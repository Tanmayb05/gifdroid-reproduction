# ViBR Run Log

**Status**: SUCCESS

## Full Log

```
2026-05-08 13:44:04 | INFO | === src_vibr.2026-05-08T17-44-04__run-006__pipeline__started ===
2026-05-08 13:44:04 | INFO | Starting ViBR run
2026-05-08 13:44:04 | INFO | App: adaway
2026-05-08 13:44:04 | INFO | Video: /Users/tanmaybhuskute/Documents/gifdroid-reproduction/apps/adaway/videos/srv-002.mp4
2026-05-08 13:44:04 | INFO | Algorithm: clip
2026-05-08 13:44:04 | INFO | LLM: gemini (gemini-2.5-pro)
2026-05-08 13:44:04 | INFO | Output: /Users/tanmaybhuskute/Documents/gifdroid-reproduction/apps/adaway/llm/ViBR_gemini/screenrec/run-006
2026-05-08 13:44:10 | INFO | FutureWarning: Importing from timm.models.layers is deprecated, please import via timm.layers
2026-05-08 13:44:10 | INFO | UserWarning: Failed to load custom C++ ops. Running on CPU mode Only!
2026-05-08 13:44:10 | INFO | UserWarning: torch.meshgrid: in an upcoming release, it will be required to pass the indexing argument. (Triggered internally at /Users/runner/work/pytorch/pytorch/pytorch/aten/src/ATen/native/TensorShape.cpp:4383.)
2026-05-08 13:44:11 | INFO | Warning: You are sending unauthenticated requests to the HF Hub. Please set a HF_TOKEN to enable higher rate limits and faster downloads.
2026-05-08 13:44:12 | INFO | final text_encoder_type: bert-base-uncased
2026-05-08 13:44:12 | INFO | 
2026-05-08 13:44:12 | INFO | Loading weights:   0%|          | 0/199 [00:00<?, ?it/s]
2026-05-08 13:44:12 | INFO | Loading weights: 100%|██████████| 199/199 [00:00<00:00, 8064.49it/s]
2026-05-08 13:44:12 | INFO | [1mBertModel LOAD REPORT[0m from: bert-base-uncased
2026-05-08 13:44:12 | INFO | Key                                        | Status     |  | 
2026-05-08 13:44:12 | INFO | -------------------------------------------+------------+--+-
2026-05-08 13:44:12 | INFO | cls.predictions.transform.dense.bias       | UNEXPECTED |  | 
2026-05-08 13:44:12 | INFO | cls.predictions.transform.LayerNorm.weight | UNEXPECTED |  | 
2026-05-08 13:44:12 | INFO | cls.predictions.transform.LayerNorm.bias   | UNEXPECTED |  | 
2026-05-08 13:44:12 | INFO | cls.seq_relationship.bias                  | UNEXPECTED |  | 
2026-05-08 13:44:12 | INFO | cls.seq_relationship.weight                | UNEXPECTED |  | 
2026-05-08 13:44:12 | INFO | cls.predictions.transform.dense.weight     | UNEXPECTED |  | 
2026-05-08 13:44:12 | INFO | cls.predictions.bias                       | UNEXPECTED |  | 
2026-05-08 13:44:12 | INFO | 
2026-05-08 13:44:12 | INFO | Notes:
2026-05-08 13:44:12 | INFO | - UNEXPECTED:	can be ignored when loading from different task/architecture; not ok if you expect identical arch.
2026-05-08 13:44:20 | INFO | 🔹 Starting video processing (algorithm=clip, llm=gemini, model=gemini-2.5-pro)...
2026-05-08 13:44:20 | INFO | Initializing ADB device controller...
2026-05-08 13:44:20 | INFO | 📱 Preparing device for app: adaway
2026-05-08 13:44:20 | INFO | 🏠 Going to home screen...
2026-05-08 13:44:20 | INFO | 🚀 Opening app 'adaway' with command: am start -n org.adaway/.ui.home.HomeActivity
2026-05-08 13:44:20 | INFO | ✅ App 'adaway' opened and ready
2026-05-08 13:44:20 | INFO | Taking screenshot: /sdcard/screenshot-0.png -> /Users/tanmaybhuskute/Documents/gifdroid-reproduction/apps/adaway/llm/ViBR_gemini/screenrec/run-006/artifacts/srv-002/screenshot-0.png
2026-05-08 13:44:20 | INFO | Reading frames from video...
2026-05-08 13:44:20 | INFO | Reading frame:  2
2026-05-08 13:44:20 | INFO | Reading frame:  3
2026-05-08 13:44:20 | INFO | Reading frame:  4
2026-05-08 13:44:20 | INFO | Reading frame:  5
2026-05-08 13:44:20 | INFO | Reading frame:  6
2026-05-08 13:44:20 | INFO | Reading frame:  7
2026-05-08 13:44:20 | INFO | Reading frame:  8
2026-05-08 13:44:20 | INFO | Reading frame:  9
2026-05-08 13:44:20 | INFO | Reading frame:  10
2026-05-08 13:44:20 | INFO | Reading frame:  11
2026-05-08 13:44:20 | INFO | Reading frame:  12
2026-05-08 13:44:20 | INFO | Reading frame:  13
2026-05-08 13:44:20 | INFO | Reading frame:  14
2026-05-08 13:44:20 | INFO | Reading frame:  15
2026-05-08 13:44:20 | INFO | Reading frame:  16
2026-05-08 13:44:20 | INFO | Reading frame:  17
2026-05-08 13:44:20 | INFO | Reading frame:  18
2026-05-08 13:44:20 | INFO | Reading frame:  19
2026-05-08 13:44:20 | INFO | Reading frame:  20
2026-05-08 13:44:20 | INFO | Reading frame:  21
2026-05-08 13:44:20 | INFO | Reading frame:  22
2026-05-08 13:44:20 | INFO | Reading frame:  23
2026-05-08 13:44:20 | INFO | Reading frame:  24
2026-05-08 13:44:20 | INFO | Reading frame:  25
2026-05-08 13:44:20 | INFO | Reading frame:  26
2026-05-08 13:44:20 | INFO | Reading frame:  27
2026-05-08 13:44:20 | INFO | Reading frame:  28
2026-05-08 13:44:20 | INFO | Reading frame:  29
2026-05-08 13:44:20 | INFO | Reading frame:  30
2026-05-08 13:44:20 | INFO | Reading frame:  31
2026-05-08 13:44:20 | INFO | Reading frame:  32
2026-05-08 13:44:20 | INFO | Reading frame:  33
2026-05-08 13:44:20 | INFO | Reading frame:  34
2026-05-08 13:44:20 | INFO | Reading frame:  35
2026-05-08 13:44:20 | INFO | Reading frame:  36
2026-05-08 13:44:20 | INFO | Reading frame:  37
2026-05-08 13:44:20 | INFO | Reading frame:  38
2026-05-08 13:44:20 | INFO | Reading frame:  39
2026-05-08 13:44:20 | INFO | Reading frame:  40
2026-05-08 13:44:20 | INFO | Reading frame:  41
2026-05-08 13:44:20 | INFO | Reading frame:  42
2026-05-08 13:44:20 | INFO | Reading frame:  43
2026-05-08 13:44:20 | INFO | Reading frame:  44
2026-05-08 13:44:20 | INFO | Reading frame:  45
2026-05-08 13:44:20 | INFO | Reading frame:  46
2026-05-08 13:44:20 | INFO | Reading frame:  47
2026-05-08 13:44:20 | INFO | Reading frame:  48
2026-05-08 13:44:20 | INFO | Reading frame:  49
2026-05-08 13:44:20 | INFO | Reading frame:  50
2026-05-08 13:44:20 | INFO | Reading frame:  51
2026-05-08 13:44:20 | INFO | Reading frame:  52
2026-05-08 13:44:20 | INFO | Reading frame:  53
2026-05-08 13:44:20 | INFO | Reading frame:  54
2026-05-08 13:44:20 | INFO | Reading frame:  55
2026-05-08 13:44:20 | INFO | Reading frame:  56
2026-05-08 13:44:20 | INFO | Reading frame:  57
2026-05-08 13:44:20 | INFO | Reading frame:  58
2026-05-08 13:44:20 | INFO | Reading frame:  59
2026-05-08 13:44:20 | INFO | Reading frame:  60
2026-05-08 13:44:20 | INFO | Reading frame:  61
2026-05-08 13:44:20 | INFO | Reading frame:  62
2026-05-08 13:44:20 | INFO | Reading frame:  63
2026-05-08 13:44:20 | INFO | Reading frame:  64
2026-05-08 13:44:20 | INFO | Reading frame:  65
2026-05-08 13:44:20 | INFO | Reading frame:  66
2026-05-08 13:44:20 | INFO | Reading frame:  67
2026-05-08 13:44:20 | INFO | Reading frame:  68
2026-05-08 13:44:20 | INFO | Reading frame:  69
2026-05-08 13:44:20 | INFO | Reading frame:  70
2026-05-08 13:44:20 | INFO | Reading frame:  71
2026-05-08 13:44:20 | INFO | Reading frame:  72
2026-05-08 13:44:20 | INFO | Reading frame:  73
2026-05-08 13:44:20 | INFO | Reading frame:  74
2026-05-08 13:44:20 | INFO | Reading frame:  75
2026-05-08 13:44:20 | INFO | Reading frame:  76
2026-05-08 13:44:20 | INFO | Reading frame:  77
2026-05-08 13:44:20 | INFO | Reading frame:  78
2026-05-08 13:44:20 | INFO | Reading frame:  79
2026-05-08 13:44:20 | INFO | Reading frame:  80
2026-05-08 13:44:20 | INFO | Reading frame:  81
2026-05-08 13:44:20 | INFO | Reading frame:  82
2026-05-08 13:44:20 | INFO | Reading frame:  83
2026-05-08 13:44:20 | INFO | Reading frame:  84
2026-05-08 13:44:20 | INFO | Reading frame:  85
2026-05-08 13:44:20 | INFO | Reading frame:  86
2026-05-08 13:44:20 | INFO | Reading frame:  87
2026-05-08 13:44:20 | INFO | Reading frame:  88
2026-05-08 13:44:20 | INFO | Reading frame:  89
2026-05-08 13:44:20 | INFO | Reading frame:  90
2026-05-08 13:44:20 | INFO | Reading frame:  91
2026-05-08 13:44:20 | INFO | Reading frame:  92
2026-05-08 13:44:20 | INFO | Reading frame:  93
2026-05-08 13:44:20 | INFO | Reading frame:  94
2026-05-08 13:44:20 | INFO | Reading frame:  95
2026-05-08 13:44:20 | INFO | Reading frame:  96
2026-05-08 13:44:20 | INFO | Reading frame:  97
2026-05-08 13:44:20 | INFO | Reading frame:  98
2026-05-08 13:44:20 | INFO | Reading frame:  99
2026-05-08 13:44:20 | INFO | Reading frame:  100
2026-05-08 13:44:20 | INFO | Reading frame:  101
2026-05-08 13:44:20 | INFO | Reading frame:  102
2026-05-08 13:44:20 | INFO | Reading frame:  103
2026-05-08 13:44:20 | INFO | Reading frame:  104
2026-05-08 13:44:20 | INFO | Reading frame:  105
2026-05-08 13:44:20 | INFO | Reading frame:  106
2026-05-08 13:44:20 | INFO | Reading frame:  107
2026-05-08 13:44:20 | INFO | Reading frame:  108
2026-05-08 13:44:20 | INFO | Reading frame:  109
2026-05-08 13:44:20 | INFO | Reading frame:  110
2026-05-08 13:44:20 | INFO | Reading frame:  111
2026-05-08 13:44:20 | INFO | Reading frame:  112
2026-05-08 13:44:20 | INFO | Reading frame:  113
2026-05-08 13:44:20 | INFO | Reading frame:  114
2026-05-08 13:44:20 | INFO | Reading frame:  115
2026-05-08 13:44:20 | INFO | Reading frame:  116
2026-05-08 13:44:20 | INFO | Reading frame:  117
2026-05-08 13:44:20 | INFO | Reading frame:  118
2026-05-08 13:44:20 | INFO | Reading frame:  119
2026-05-08 13:44:20 | INFO | Reading frame:  120
2026-05-08 13:44:20 | INFO | Reading frame:  121
2026-05-08 13:44:20 | INFO | Reading frame:  122
2026-05-08 13:44:20 | INFO | Reading frame:  123
2026-05-08 13:44:20 | INFO | Reading frame:  124
2026-05-08 13:44:20 | INFO | Reading frame:  125
2026-05-08 13:44:20 | INFO | Reading frame:  126
2026-05-08 13:44:20 | INFO | Reading frame:  127
2026-05-08 13:44:20 | INFO | Reading frame:  128
2026-05-08 13:44:20 | INFO | Reading frame:  129
2026-05-08 13:44:20 | INFO | Reading frame:  130
2026-05-08 13:44:20 | INFO | Reading frame:  131
2026-05-08 13:44:20 | INFO | Reading frame:  132
2026-05-08 13:44:20 | INFO | Reading frame:  133
2026-05-08 13:44:20 | INFO | Reading frame:  134
2026-05-08 13:44:20 | INFO | Reading frame:  135
2026-05-08 13:44:20 | INFO | Reading frame:  136
2026-05-08 13:44:20 | INFO | Reading frame:  137
2026-05-08 13:44:20 | INFO | Reading frame:  138
2026-05-08 13:44:20 | INFO | Reading frame:  139
2026-05-08 13:44:20 | INFO | Reading frame:  140
2026-05-08 13:44:20 | INFO | Reading frame:  141
2026-05-08 13:44:20 | INFO | Reading frame:  142
2026-05-08 13:44:20 | INFO | Reading frame:  143
2026-05-08 13:44:20 | INFO | Reading frame:  144
2026-05-08 13:44:20 | INFO | Reading frame:  145
2026-05-08 13:44:20 | INFO | Reading frame:  146
2026-05-08 13:44:20 | INFO | Reading frame:  147
2026-05-08 13:44:20 | INFO | Reading frame:  148
2026-05-08 13:44:20 | INFO | Reading frame:  149
2026-05-08 13:44:20 | INFO | Reading frame:  150
2026-05-08 13:44:20 | INFO | Reading frame:  151
2026-05-08 13:44:20 | INFO | Reading frame:  152
2026-05-08 13:44:20 | INFO | Reading frame:  153
2026-05-08 13:44:20 | INFO | Reading frame:  154
2026-05-08 13:44:20 | INFO | Reading frame:  155
2026-05-08 13:44:20 | INFO | Reading frame:  156
2026-05-08 13:44:20 | INFO | Reading frame:  157
2026-05-08 13:44:20 | INFO | Reading frame:  158
2026-05-08 13:44:20 | INFO | Reading frame:  159
2026-05-08 13:44:20 | INFO | Reading frame:  160
2026-05-08 13:44:20 | INFO | Reading frame:  161
2026-05-08 13:44:20 | INFO | Reading frame:  162
2026-05-08 13:44:20 | INFO | Reading frame:  163
2026-05-08 13:44:20 | INFO | Reading frame:  164
2026-05-08 13:44:20 | INFO | Reading frame:  165
2026-05-08 13:44:20 | INFO | Reading frame:  166
2026-05-08 13:44:20 | INFO | Reading frame:  167
2026-05-08 13:44:20 | INFO | Reading frame:  168
2026-05-08 13:44:20 | INFO | Reading frame:  169
2026-05-08 13:44:20 | INFO | Reading frame:  170
2026-05-08 13:44:20 | INFO | Reading frame:  171
2026-05-08 13:44:20 | INFO | Reading frame:  172
2026-05-08 13:44:20 | INFO | Reading frame:  173
2026-05-08 13:44:20 | INFO | Reading frame:  174
2026-05-08 13:44:20 | INFO | Reading frame:  175
2026-05-08 13:44:20 | INFO | Reading frame:  176
2026-05-08 13:44:20 | INFO | Reading frame:  177
2026-05-08 13:44:20 | INFO | Reading frame:  178
2026-05-08 13:44:20 | INFO | Reading frame:  179
2026-05-08 13:44:20 | INFO | Reading frame:  180
2026-05-08 13:44:20 | INFO | Reading frame:  181
2026-05-08 13:44:20 | INFO | Reading frame:  182
2026-05-08 13:44:20 | INFO | Reading frame:  183
2026-05-08 13:44:20 | INFO | Reading frame:  184
2026-05-08 13:44:20 | INFO | Reading frame:  185
2026-05-08 13:44:20 | INFO | Reading frame:  186
2026-05-08 13:44:20 | INFO | Reading frame:  187
2026-05-08 13:44:20 | INFO | Reading frame:  188
2026-05-08 13:44:20 | INFO | Reading frame:  189
2026-05-08 13:44:20 | INFO | Reading frame:  190
2026-05-08 13:44:20 | INFO | Reading frame:  191
2026-05-08 13:44:20 | INFO | Reading frame:  192
2026-05-08 13:44:20 | INFO | Reading frame:  193
2026-05-08 13:44:20 | INFO | Reading frame:  194
2026-05-08 13:44:20 | INFO | Reading frame:  195
2026-05-08 13:44:20 | INFO | Reading frame:  196
2026-05-08 13:44:20 | INFO | Reading frame:  197
2026-05-08 13:44:20 | INFO | Reading frame:  198
2026-05-08 13:44:20 | INFO | Reading frame:  199
2026-05-08 13:44:20 | INFO | Reading frame:  200
2026-05-08 13:44:20 | INFO | Reading frame:  201
2026-05-08 13:44:20 | INFO | Reading frame:  202
2026-05-08 13:44:20 | INFO | Reading frame:  203
2026-05-08 13:44:20 | INFO | Reading frame:  204
2026-05-08 13:44:20 | INFO | Reading frame:  205
2026-05-08 13:44:20 | INFO | Reading frame:  206
2026-05-08 13:44:20 | INFO | Reading frame:  207
2026-05-08 13:44:20 | INFO | Reading frame:  208
2026-05-08 13:44:20 | INFO | Reading frame:  209
2026-05-08 13:44:20 | INFO | Reading frame:  210
2026-05-08 13:44:20 | INFO | Reading frame:  211
2026-05-08 13:44:20 | INFO | Reading frame:  212
2026-05-08 13:44:20 | INFO | Reading frame:  213
2026-05-08 13:44:20 | INFO | Reading frame:  214
2026-05-08 13:44:20 | INFO | Reading frame:  215
2026-05-08 13:44:20 | INFO | Reading frame:  216
2026-05-08 13:44:20 | INFO | Reading frame:  217
2026-05-08 13:44:20 | INFO | Reading frame:  218
2026-05-08 13:44:20 | INFO | Reading frame:  219
2026-05-08 13:44:20 | INFO | Reading frame:  220
2026-05-08 13:44:20 | INFO | Reading frame:  221
2026-05-08 13:44:20 | INFO | Reading frame:  222
2026-05-08 13:44:20 | INFO | Reading frame:  223
2026-05-08 13:44:20 | INFO | Reading frame:  224
2026-05-08 13:44:20 | INFO | Reading frame:  225
2026-05-08 13:44:20 | INFO | Reading frame:  226
2026-05-08 13:44:20 | INFO | Reading frame:  227
2026-05-08 13:44:20 | INFO | Reading frame:  228
2026-05-08 13:44:20 | INFO | Reading frame:  229
2026-05-08 13:44:20 | INFO | Reading frame:  230
2026-05-08 13:44:20 | INFO | Reading frame:  231
2026-05-08 13:44:20 | INFO | Reading frame:  232
2026-05-08 13:44:20 | INFO | Reading frame:  233
2026-05-08 13:44:20 | INFO | Reading frame:  234
2026-05-08 13:44:20 | INFO | Reading frame:  235
2026-05-08 13:44:20 | INFO | Reading frame:  236
2026-05-08 13:44:20 | INFO | Reading frame:  237
2026-05-08 13:44:20 | INFO | Reading frame:  238
2026-05-08 13:44:20 | INFO | Reading frame:  239
2026-05-08 13:44:20 | INFO | Reading frame:  240
2026-05-08 13:44:20 | INFO | Reading frame:  241
2026-05-08 13:44:20 | INFO | Reading frame:  242
2026-05-08 13:44:20 | INFO | Reading frame:  243
2026-05-08 13:44:20 | INFO | Reading frame:  244
2026-05-08 13:44:20 | INFO | Reading frame:  245
2026-05-08 13:44:20 | INFO | Reading frame:  246
2026-05-08 13:44:20 | INFO | Reading frame:  247
2026-05-08 13:44:20 | INFO | Reading frame:  248
2026-05-08 13:44:20 | INFO | Reading frame:  249
2026-05-08 13:44:20 | INFO | Reading frame:  250
2026-05-08 13:44:20 | INFO | Reading frame:  251
2026-05-08 13:44:20 | INFO | Reading frame:  252
2026-05-08 13:44:20 | INFO | Reading frame:  253
2026-05-08 13:44:20 | INFO | Reading frame:  254
2026-05-08 13:44:20 | INFO | Reading frame:  255
2026-05-08 13:44:20 | INFO | Reading frame:  256
2026-05-08 13:44:20 | INFO | Reading frame:  257
2026-05-08 13:44:20 | INFO | Reading frame:  258
2026-05-08 13:44:20 | INFO | Reading frame:  259
2026-05-08 13:44:20 | INFO | Reading frame:  260
2026-05-08 13:44:20 | INFO | Reading frame:  261
2026-05-08 13:44:20 | INFO | Reading frame:  262
2026-05-08 13:44:20 | INFO | Reading frame:  263
2026-05-08 13:44:20 | INFO | Reading frame:  264
2026-05-08 13:44:20 | INFO | Reading frame:  265
2026-05-08 13:44:20 | INFO | Reading frame:  266
2026-05-08 13:44:20 | INFO | Reading frame:  267
2026-05-08 13:44:20 | INFO | Reading frame:  268
2026-05-08 13:44:20 | INFO | Reading frame:  269
2026-05-08 13:44:20 | INFO | Reading frame:  270
2026-05-08 13:44:20 | INFO | Reading frame:  271
2026-05-08 13:44:20 | INFO | Reading frame:  272
2026-05-08 13:44:20 | INFO | Reading frame:  273
2026-05-08 13:44:20 | INFO | Reading frame:  274
2026-05-08 13:44:20 | INFO | Reading frame:  275
2026-05-08 13:44:20 | INFO | Reading frame:  276
2026-05-08 13:44:20 | INFO | Reading frame:  277
2026-05-08 13:44:20 | INFO | Reading frame:  278
2026-05-08 13:44:20 | INFO | Reading frame:  279
2026-05-08 13:44:20 | INFO | Reading frame:  280
2026-05-08 13:44:20 | INFO | Reading frame:  281
2026-05-08 13:44:20 | INFO | Reading frame:  282
2026-05-08 13:44:20 | INFO | Reading frame:  283
2026-05-08 13:44:20 | INFO | Reading frame:  284
2026-05-08 13:44:20 | INFO | Reading frame:  285
2026-05-08 13:44:20 | INFO | Reading frame:  286
2026-05-08 13:44:20 | INFO | Reading frame:  287
2026-05-08 13:44:20 | INFO | Reading frame:  288
2026-05-08 13:44:20 | INFO | Reading frame:  289
2026-05-08 13:44:20 | INFO | Reading frame:  290
2026-05-08 13:44:20 | INFO | Reading frame:  291
2026-05-08 13:44:20 | INFO | Reading frame:  292
2026-05-08 13:44:20 | INFO | Reading frame:  293
2026-05-08 13:44:20 | INFO | Reading frame:  294
2026-05-08 13:44:20 | INFO | Reading frame:  295
2026-05-08 13:44:20 | INFO | Reading frame:  296
2026-05-08 13:44:20 | INFO | Reading frame:  297
2026-05-08 13:44:20 | INFO | Reading frame:  298
2026-05-08 13:44:20 | INFO | Reading frame:  299
2026-05-08 13:44:20 | INFO | Reading frame:  300
2026-05-08 13:44:20 | INFO | Reading frame:  301
2026-05-08 13:44:20 | INFO | Reading frame:  302
2026-05-08 13:44:20 | INFO | Reading frame:  303
2026-05-08 13:44:20 | INFO | Reading frame:  304
2026-05-08 13:44:20 | INFO | Reading frame:  305
2026-05-08 13:44:20 | INFO | Reading frame:  306
2026-05-08 13:44:20 | INFO | Reading frame:  307
2026-05-08 13:44:20 | INFO | Reading frame:  308
2026-05-08 13:44:20 | INFO | Reading frame:  309
2026-05-08 13:44:20 | INFO | Reading frame:  310
2026-05-08 13:44:20 | INFO | Reading frame:  311
2026-05-08 13:44:20 | INFO | Reading frame:  312
2026-05-08 13:44:20 | INFO | Reading frame:  313
2026-05-08 13:44:20 | INFO | Reading frame:  314
2026-05-08 13:44:20 | INFO | Reading frame:  315
2026-05-08 13:44:20 | INFO | Reading frame:  316
2026-05-08 13:44:20 | INFO | Reading frame:  317
2026-05-08 13:44:20 | INFO | Reading frame:  318
2026-05-08 13:44:20 | INFO | Reading frame:  319
2026-05-08 13:44:20 | INFO | Reading frame:  320
2026-05-08 13:44:20 | INFO | Reading frame:  321
2026-05-08 13:44:20 | INFO | Reading frame:  322
2026-05-08 13:44:20 | INFO | Reading frame:  323
2026-05-08 13:44:20 | INFO | Reading frame:  324
2026-05-08 13:44:20 | INFO | Reading frame:  325
2026-05-08 13:44:20 | INFO | Reading frame:  326
2026-05-08 13:44:20 | INFO | Reading frame:  327
2026-05-08 13:44:20 | INFO | Reading frame:  328
2026-05-08 13:44:20 | INFO | Reading frame:  329
2026-05-08 13:44:20 | INFO | Reading frame:  330
2026-05-08 13:44:20 | INFO | Reading frame:  331
2026-05-08 13:44:20 | INFO | Reading frame:  332
2026-05-08 13:44:20 | INFO | Reading frame:  333
2026-05-08 13:44:20 | INFO | Reading frame:  334
2026-05-08 13:44:20 | INFO | Reading frame:  335
2026-05-08 13:44:20 | INFO | Reading frame:  336
2026-05-08 13:44:20 | INFO | Reading frame:  337
2026-05-08 13:44:20 | INFO | Reading frame:  338
2026-05-08 13:44:20 | INFO | Reading frame:  339
2026-05-08 13:44:20 | INFO | Reading frame:  340
2026-05-08 13:44:20 | INFO | Reading frame:  341
2026-05-08 13:44:20 | INFO | Reading frame:  342
2026-05-08 13:44:20 | INFO | Reading frame:  343
2026-05-08 13:44:20 | INFO | Reading frame:  344
2026-05-08 13:44:20 | INFO | Reading frame:  345
2026-05-08 13:44:20 | INFO | Reading frame:  346
2026-05-08 13:44:20 | INFO | Reading frame:  347
2026-05-08 13:44:20 | INFO | Reading frame:  348
2026-05-08 13:44:20 | INFO | Reading frame:  349
2026-05-08 13:44:20 | INFO | Reading frame:  350
2026-05-08 13:44:20 | INFO | Reading frame:  351
2026-05-08 13:44:20 | INFO | Reading frame:  352
2026-05-08 13:44:20 | INFO | Reading frame:  353
2026-05-08 13:44:20 | INFO | Reading frame:  354
2026-05-08 13:44:20 | INFO | Reading frame:  355
2026-05-08 13:44:20 | INFO | Reading frame:  356
2026-05-08 13:44:20 | INFO | Reading frame:  357
2026-05-08 13:44:20 | INFO | Reading frame:  358
2026-05-08 13:44:20 | INFO | Reading frame:  359
2026-05-08 13:44:20 | INFO | Reading frame:  360
2026-05-08 13:44:20 | INFO | Reading frame:  361
2026-05-08 13:44:20 | INFO | Reading frame:  362
2026-05-08 13:44:20 | INFO | Reading frame:  363
2026-05-08 13:44:20 | INFO | Reading frame:  364
2026-05-08 13:44:20 | INFO | Reading frame:  365
2026-05-08 13:44:20 | INFO | Reading frame:  366
2026-05-08 13:44:20 | INFO | Reading frame:  367
2026-05-08 13:44:20 | INFO | Reading frame:  368
2026-05-08 13:44:20 | INFO | Reading frame:  369
2026-05-08 13:44:20 | INFO | Reading frame:  370
2026-05-08 13:44:20 | INFO | Reading frame:  371
2026-05-08 13:44:20 | INFO | Reading frame:  372
2026-05-08 13:44:20 | INFO | Reading frame:  373
2026-05-08 13:44:20 | INFO | Reading frame:  374
2026-05-08 13:44:20 | INFO | Reading frame:  375
2026-05-08 13:44:20 | INFO | Reading frame:  376
2026-05-08 13:44:20 | INFO | Reading frame:  377
2026-05-08 13:44:20 | INFO | Reading frame:  378
2026-05-08 13:44:20 | INFO | Reading frame:  379
2026-05-08 13:44:20 | INFO | Reading frame:  380
2026-05-08 13:44:20 | INFO | Reading frame:  381
2026-05-08 13:44:20 | INFO | Reading frame:  382
2026-05-08 13:44:20 | INFO | Reading frame:  383
2026-05-08 13:44:20 | INFO | Reading frame:  384
2026-05-08 13:44:20 | INFO | Reading frame:  385
2026-05-08 13:44:20 | INFO | Reading frame:  386
2026-05-08 13:44:20 | INFO | Reading frame:  387
2026-05-08 13:44:20 | INFO | Reading frame:  388
2026-05-08 13:44:20 | INFO | Reading frame:  389
2026-05-08 13:44:20 | INFO | Reading frame:  390
2026-05-08 13:44:20 | INFO | Reading frame:  391
2026-05-08 13:44:20 | INFO | Reading frame:  392
2026-05-08 13:44:20 | INFO | Reading frame:  393
2026-05-08 13:44:20 | INFO | Reading frame:  394
2026-05-08 13:44:20 | INFO | Reading frame:  395
2026-05-08 13:44:20 | INFO | Reading frame:  396
2026-05-08 13:44:20 | INFO | Reading frame:  397
2026-05-08 13:44:20 | INFO | Reading frame:  398
2026-05-08 13:44:20 | INFO | Reading frame:  399
2026-05-08 13:44:20 | INFO | Reading frame:  400
2026-05-08 13:44:20 | INFO | Reading frame:  401
2026-05-08 13:44:20 | INFO | Reading frame:  402
2026-05-08 13:44:20 | INFO | Reading frame:  403
2026-05-08 13:44:20 | INFO | Reading frame:  404
2026-05-08 13:44:20 | INFO | Reading frame:  405
2026-05-08 13:44:20 | INFO | Reading frame:  406
2026-05-08 13:44:20 | INFO | Reading frame:  407
2026-05-08 13:44:20 | INFO | Reading frame:  408
2026-05-08 13:44:20 | INFO | Reading frame:  409
2026-05-08 13:44:20 | INFO | Reading frame:  410
2026-05-08 13:44:20 | INFO | Reading frame:  411
2026-05-08 13:44:20 | INFO | Reading frame:  412
2026-05-08 13:44:20 | INFO | Reading frame:  413
2026-05-08 13:44:20 | INFO | Reading frame:  414
2026-05-08 13:44:20 | INFO | Reading frame:  415
2026-05-08 13:44:20 | INFO | Reading frame:  416
2026-05-08 13:44:20 | INFO | Reading frame:  417
2026-05-08 13:44:20 | INFO | Reading frame:  418
2026-05-08 13:44:20 | INFO | Reading frame:  419
2026-05-08 13:44:20 | INFO | Reading frame:  420
2026-05-08 13:44:20 | INFO | Reading frame:  421
2026-05-08 13:44:20 | INFO | Reading frame:  422
2026-05-08 13:44:20 | INFO | Reading frame:  423
2026-05-08 13:44:20 | INFO | Reading frame:  424
2026-05-08 13:44:20 | INFO | Reading frame:  425
2026-05-08 13:44:20 | INFO | Reading frame:  426
2026-05-08 13:44:20 | INFO | Reading frame:  427
2026-05-08 13:44:20 | INFO | Reading frame:  428
2026-05-08 13:44:20 | INFO | Reading frame:  429
2026-05-08 13:44:20 | INFO | Reading frame:  430
2026-05-08 13:44:20 | INFO | Reading frame:  431
2026-05-08 13:44:20 | INFO | Reading frame:  432
2026-05-08 13:44:20 | INFO | Reading frame:  433
2026-05-08 13:44:20 | INFO | Reading frame:  434
2026-05-08 13:44:20 | INFO | Reading frame:  435
2026-05-08 13:44:20 | INFO | Reading frame:  436
2026-05-08 13:44:20 | INFO | Reading frame:  437
2026-05-08 13:44:20 | INFO | Reading frame:  438
2026-05-08 13:44:20 | INFO | Reading frame:  439
2026-05-08 13:44:20 | INFO | Reading frame:  440
2026-05-08 13:44:20 | INFO | Reading frame:  441
2026-05-08 13:44:20 | INFO | Reading frame:  442
2026-05-08 13:44:20 | INFO | Reading frame:  443
2026-05-08 13:44:20 | INFO | Reading frame:  444
2026-05-08 13:44:20 | INFO | Reading frame:  445
2026-05-08 13:44:20 | INFO | Reading frame:  446
2026-05-08 13:44:20 | INFO | Reading frame:  447
2026-05-08 13:44:20 | INFO | Reading frame:  448
2026-05-08 13:44:20 | INFO | Reading frame:  449
2026-05-08 13:44:20 | INFO | Reading frame:  450
2026-05-08 13:44:20 | INFO | Reading frame:  451
2026-05-08 13:44:20 | INFO | Reading frame:  452
2026-05-08 13:44:20 | INFO | Reading frame:  453
2026-05-08 13:44:20 | INFO | Reading frame:  454
2026-05-08 13:44:20 | INFO | Reading frame:  455
2026-05-08 13:44:20 | INFO | Reading frame:  456
2026-05-08 13:44:20 | INFO | Reading frame:  457
2026-05-08 13:44:20 | INFO | Reading frame:  458
2026-05-08 13:44:20 | INFO | Reading frame:  459
2026-05-08 13:44:20 | INFO | Reading frame:  460
2026-05-08 13:44:20 | INFO | Reading frame:  461
2026-05-08 13:44:20 | INFO | Reading frame:  462
2026-05-08 13:44:20 | INFO | Reading frame:  463
2026-05-08 13:44:20 | INFO | Reading frame:  464
2026-05-08 13:44:20 | INFO | Reading frame:  465
2026-05-08 13:44:20 | INFO | Reading frame:  466
2026-05-08 13:44:20 | INFO | Reading frame:  467
2026-05-08 13:44:20 | INFO | Reading frame:  468
2026-05-08 13:44:20 | INFO | Reading frame:  469
2026-05-08 13:44:20 | INFO | Reading frame:  470
2026-05-08 13:44:20 | INFO | Reading frame:  471
2026-05-08 13:44:20 | INFO | Reading frame:  472
2026-05-08 13:44:20 | INFO | Reading frame:  473
2026-05-08 13:44:20 | INFO | Reading frame:  474
2026-05-08 13:44:20 | INFO | Reading frame:  475
2026-05-08 13:44:20 | INFO | Reading frame:  476
2026-05-08 13:44:20 | INFO | Reading frame:  477
2026-05-08 13:44:20 | INFO | Reading frame:  478
2026-05-08 13:44:20 | INFO | Reading frame:  479
2026-05-08 13:44:20 | INFO | Reading frame:  480
2026-05-08 13:44:20 | INFO | Reading frame:  481
2026-05-08 13:44:20 | INFO | Reading frame:  482
2026-05-08 13:44:20 | INFO | Reading frame:  483
2026-05-08 13:44:20 | INFO | Reading frame:  484
2026-05-08 13:44:20 | INFO | Reading frame:  485
2026-05-08 13:44:20 | INFO | Reading frame:  486
2026-05-08 13:44:20 | INFO | Reading frame:  487
2026-05-08 13:44:20 | INFO | Reading frame:  488
2026-05-08 13:44:20 | INFO | Reading frame:  489
2026-05-08 13:44:20 | INFO | Reading frame:  490
2026-05-08 13:44:20 | INFO | Reading frame:  491
2026-05-08 13:44:20 | INFO | Reading frame:  492
2026-05-08 13:44:20 | INFO | Reading frame:  493
2026-05-08 13:44:20 | INFO | Reading frame:  494
2026-05-08 13:44:20 | INFO | Reading frame:  495
2026-05-08 13:44:20 | INFO | Reading frame:  496
2026-05-08 13:44:20 | INFO | Reading frame:  497
2026-05-08 13:44:20 | INFO | Reading frame:  498
2026-05-08 13:44:20 | INFO | Reading frame:  499
2026-05-08 13:44:20 | INFO | Reading frame:  500
2026-05-08 13:44:20 | INFO | Reading frame:  501
2026-05-08 13:44:20 | INFO | Reading frame:  502
2026-05-08 13:44:20 | INFO | Reading frame:  503
2026-05-08 13:44:20 | INFO | Reading frame:  504
2026-05-08 13:44:20 | INFO | Reading frame:  505
2026-05-08 13:44:20 | INFO | Reading frame:  506
2026-05-08 13:44:20 | INFO | Reading frame:  507
2026-05-08 13:44:20 | INFO | Reading frame:  508
2026-05-08 13:44:20 | INFO | Reading frame:  509
2026-05-08 13:44:20 | INFO | Reading frame:  510
2026-05-08 13:44:20 | INFO | Reading frame:  511
2026-05-08 13:44:20 | INFO | Reading frame:  512
2026-05-08 13:44:20 | INFO | Reading frame:  513
2026-05-08 13:44:20 | INFO | Reading frame:  514
2026-05-08 13:44:20 | INFO | Reading frame:  515
2026-05-08 13:44:20 | INFO | Reading frame:  516
2026-05-08 13:44:20 | INFO | Reading frame:  517
2026-05-08 13:44:20 | INFO | Reading frame:  518
2026-05-08 13:44:20 | INFO | Reading frame:  519
2026-05-08 13:44:20 | INFO | Reading frame:  520
2026-05-08 13:44:20 | INFO | Reading frame:  521
2026-05-08 13:44:20 | INFO | Reading frame:  522
2026-05-08 13:44:20 | INFO | Reading frame:  523
2026-05-08 13:44:20 | INFO | Reading frame:  524
2026-05-08 13:44:20 | INFO | Reading frame:  525
2026-05-08 13:44:20 | INFO | Reading frame:  526
2026-05-08 13:44:20 | INFO | Reading frame:  527
2026-05-08 13:44:20 | INFO | Reading frame:  528
2026-05-08 13:44:20 | INFO | Reading frame:  529
2026-05-08 13:44:20 | INFO | Reading frame:  530
2026-05-08 13:44:20 | INFO | Reading frame:  531
2026-05-08 13:44:20 | INFO | Reading frame:  532
2026-05-08 13:44:20 | INFO | Reading frame:  533
2026-05-08 13:44:20 | INFO | Reading frame:  534
2026-05-08 13:44:20 | INFO | Reading frame:  535
2026-05-08 13:44:20 | INFO | Reading frame:  536
2026-05-08 13:44:20 | INFO | Reading frame:  537
2026-05-08 13:44:20 | INFO | Reading frame:  538
2026-05-08 13:44:20 | INFO | Reading frame:  539
2026-05-08 13:44:20 | INFO | Reading frame:  540
2026-05-08 13:44:20 | INFO | Reading frame:  541
2026-05-08 13:44:20 | INFO | Reading frame:  542
2026-05-08 13:44:20 | INFO | Reading frame:  543
2026-05-08 13:44:20 | INFO | Reading frame:  544
2026-05-08 13:44:20 | INFO | Reading frame:  545
2026-05-08 13:44:20 | INFO | Reading frame:  546
2026-05-08 13:44:20 | INFO | Reading frame:  547
2026-05-08 13:44:20 | INFO | Reading frame:  548
2026-05-08 13:44:20 | INFO | Reading frame:  549
2026-05-08 13:44:20 | INFO | Reading frame:  550
2026-05-08 13:44:20 | INFO | Reading frame:  551
2026-05-08 13:44:20 | INFO | Reading frame:  552
2026-05-08 13:44:20 | INFO | Reading frame:  553
2026-05-08 13:44:20 | INFO | Reading frame:  554
2026-05-08 13:44:20 | INFO | Reading frame:  555
2026-05-08 13:44:20 | INFO | Reading frame:  556
2026-05-08 13:44:20 | INFO | Reading frame:  557
2026-05-08 13:44:20 | INFO | Reading frame:  558
2026-05-08 13:44:20 | INFO | Reading frame:  559
2026-05-08 13:44:20 | INFO | Reading frame:  560
2026-05-08 13:44:20 | INFO | Reading frame:  561
2026-05-08 13:44:20 | INFO | Reading frame:  562
2026-05-08 13:44:20 | INFO | Reading frame:  563
2026-05-08 13:44:20 | INFO | Reading frame:  564
2026-05-08 13:44:20 | INFO | Reading frame:  565
2026-05-08 13:44:20 | INFO | Reading frame:  566
2026-05-08 13:44:20 | INFO | Reading frame:  567
2026-05-08 13:44:20 | INFO | Reading frame:  568
2026-05-08 13:44:20 | INFO | Reading frame:  569
2026-05-08 13:44:20 | INFO | Reading frame:  570
2026-05-08 13:44:20 | INFO | Reading frame:  571
2026-05-08 13:44:20 | INFO | Reading frame:  572
2026-05-08 13:44:20 | INFO | Reading frame:  573
2026-05-08 13:44:20 | INFO | Reading frame:  574
2026-05-08 13:44:20 | INFO | Reading frame:  575
2026-05-08 13:44:20 | INFO | Reading frame:  576
2026-05-08 13:44:20 | INFO | Reading frame:  577
2026-05-08 13:44:20 | INFO | Reading frame:  578
2026-05-08 13:44:20 | INFO | Reading frame:  579
2026-05-08 13:44:20 | INFO | Reading frame:  580
2026-05-08 13:44:20 | INFO | Reading frame:  581
2026-05-08 13:44:20 | INFO | Reading frame:  582
2026-05-08 13:44:20 | INFO | Reading frame:  583
2026-05-08 13:44:20 | INFO | Reading frame:  584
2026-05-08 13:44:20 | INFO | Reading frame:  585
2026-05-08 13:44:20 | INFO | Reading frame:  586
2026-05-08 13:44:20 | INFO | Reading frame:  587
2026-05-08 13:44:20 | INFO | Reading frame:  588
2026-05-08 13:44:20 | INFO | Reading frame:  589
2026-05-08 13:44:20 | INFO | Reading frame:  590
2026-05-08 13:44:20 | INFO | Reading frame:  591
2026-05-08 13:44:20 | INFO | Reading frame:  592
2026-05-08 13:44:20 | INFO | Reading frame:  593
2026-05-08 13:44:20 | INFO | Reading frame:  594
2026-05-08 13:44:20 | INFO | Reading frame:  595
2026-05-08 13:44:20 | INFO | Reading frame:  596
2026-05-08 13:44:20 | INFO | Reading frame:  597
2026-05-08 13:44:20 | INFO | Reading frame:  598
2026-05-08 13:44:20 | INFO | Reading frame:  599
2026-05-08 13:44:20 | INFO | Reading frame:  600
2026-05-08 13:44:20 | INFO | 🔍 Detecting stable segments...
2026-05-08 13:44:20 | INFO | 
2026-05-08 13:44:20 | INFO | Loading weights:   0%|          | 0/398 [00:00<?, ?it/s]
2026-05-08 13:44:20 | INFO | Loading weights: 100%|██████████| 398/398 [00:00<00:00, 32999.25it/s]
2026-05-08 13:44:20 | INFO | [1mCLIPModel LOAD REPORT[0m from: openai/clip-vit-base-patch32
2026-05-08 13:44:20 | INFO | Key                                  | Status     |  | 
2026-05-08 13:44:20 | INFO | -------------------------------------+------------+--+-
2026-05-08 13:44:20 | INFO | text_model.embeddings.position_ids   | UNEXPECTED |  | 
2026-05-08 13:44:20 | INFO | vision_model.embeddings.position_ids | UNEXPECTED |  | 
2026-05-08 13:44:20 | INFO | 
2026-05-08 13:44:20 | INFO | Notes:
2026-05-08 13:44:20 | INFO | - UNEXPECTED:	can be ignored when loading from different task/architecture; not ok if you expect identical arch.
2026-05-08 13:45:00 | INFO | `use_return_dict` is deprecated! Use `return_dict` instead!
2026-05-08 13:45:00 | INFO | UserWarning: torch.utils.checkpoint: the use_reentrant parameter should be passed explicitly. Starting in PyTorch 2.9, calling checkpoint without use_reentrant will raise an exception. use_reentrant=False is recommended, but if you need to preserve the current default behavior, you can pass use_reentrant=True. Refer to docs for more details on the differences between the two variants.
2026-05-08 13:45:00 | INFO | UserWarning: None of the inputs have requires_grad=True. Gradients will be None
2026-05-08 13:45:04 | INFO | FutureWarning: `torch.cuda.amp.autocast(args...)` is deprecated. Please use `torch.amp.autocast('cuda', args...)` instead.
2026-05-08 13:46:17 | INFO | Encoding frames with CLIP...
2026-05-08 13:46:17 | INFO |   Encoded 1/600
2026-05-08 13:46:17 | INFO |   Encoded 2/600
2026-05-08 13:46:17 | INFO |   Encoded 3/600
2026-05-08 13:46:17 | INFO |   Encoded 4/600
2026-05-08 13:46:17 | INFO |   Encoded 5/600
2026-05-08 13:46:17 | INFO |   Encoded 6/600
2026-05-08 13:46:17 | INFO |   Encoded 7/600
2026-05-08 13:46:17 | INFO |   Encoded 8/600
2026-05-08 13:46:17 | INFO |   Encoded 9/600
2026-05-08 13:46:17 | INFO |   Encoded 10/600
2026-05-08 13:46:17 | INFO |   Encoded 11/600
2026-05-08 13:46:17 | INFO |   Encoded 12/600
2026-05-08 13:46:17 | INFO |   Encoded 13/600
2026-05-08 13:46:17 | INFO |   Encoded 14/600
2026-05-08 13:46:17 | INFO |   Encoded 15/600
2026-05-08 13:46:17 | INFO |   Encoded 16/600
2026-05-08 13:46:17 | INFO |   Encoded 17/600
2026-05-08 13:46:17 | INFO |   Encoded 18/600
2026-05-08 13:46:17 | INFO |   Encoded 19/600
2026-05-08 13:46:17 | INFO |   Encoded 20/600
2026-05-08 13:46:17 | INFO |   Encoded 21/600
2026-05-08 13:46:17 | INFO |   Encoded 22/600
2026-05-08 13:46:17 | INFO |   Encoded 23/600
2026-05-08 13:46:17 | INFO |   Encoded 24/600
2026-05-08 13:46:17 | INFO |   Encoded 25/600
2026-05-08 13:46:17 | INFO |   Encoded 26/600
2026-05-08 13:46:17 | INFO |   Encoded 27/600
2026-05-08 13:46:17 | INFO |   Encoded 28/600
2026-05-08 13:46:17 | INFO |   Encoded 29/600
2026-05-08 13:46:17 | INFO |   Encoded 30/600
2026-05-08 13:46:17 | INFO |   Encoded 31/600
2026-05-08 13:46:17 | INFO |   Encoded 32/600
2026-05-08 13:46:17 | INFO |   Encoded 33/600
2026-05-08 13:46:17 | INFO |   Encoded 34/600
2026-05-08 13:46:17 | INFO |   Encoded 35/600
2026-05-08 13:46:17 | INFO |   Encoded 36/600
2026-05-08 13:46:17 | INFO |   Encoded 37/600
2026-05-08 13:46:17 | INFO |   Encoded 38/600
2026-05-08 13:46:17 | INFO |   Encoded 39/600
2026-05-08 13:46:17 | INFO |   Encoded 40/600
2026-05-08 13:46:17 | INFO |   Encoded 41/600
2026-05-08 13:46:17 | INFO |   Encoded 42/600
2026-05-08 13:46:17 | INFO |   Encoded 43/600
2026-05-08 13:46:17 | INFO |   Encoded 44/600
2026-05-08 13:46:17 | INFO |   Encoded 45/600
2026-05-08 13:46:17 | INFO |   Encoded 46/600
2026-05-08 13:46:17 | INFO |   Encoded 47/600
2026-05-08 13:46:17 | INFO |   Encoded 48/600
2026-05-08 13:46:17 | INFO |   Encoded 49/600
2026-05-08 13:46:17 | INFO |   Encoded 50/600
2026-05-08 13:46:17 | INFO |   Encoded 51/600
2026-05-08 13:46:17 | INFO |   Encoded 52/600
2026-05-08 13:46:17 | INFO |   Encoded 53/600
2026-05-08 13:46:17 | INFO |   Encoded 54/600
2026-05-08 13:46:17 | INFO |   Encoded 55/600
2026-05-08 13:46:17 | INFO |   Encoded 56/600
2026-05-08 13:46:17 | INFO |   Encoded 57/600
2026-05-08 13:46:17 | INFO |   Encoded 58/600
2026-05-08 13:46:17 | INFO |   Encoded 59/600
2026-05-08 13:46:17 | INFO |   Encoded 60/600
2026-05-08 13:46:17 | INFO |   Encoded 61/600
2026-05-08 13:46:17 | INFO |   Encoded 62/600
2026-05-08 13:46:17 | INFO |   Encoded 63/600
2026-05-08 13:46:17 | INFO |   Encoded 64/600
2026-05-08 13:46:17 | INFO |   Encoded 65/600
2026-05-08 13:46:17 | INFO |   Encoded 66/600
2026-05-08 13:46:17 | INFO |   Encoded 67/600
2026-05-08 13:46:17 | INFO |   Encoded 68/600
2026-05-08 13:46:17 | INFO |   Encoded 69/600
2026-05-08 13:46:17 | INFO |   Encoded 70/600
2026-05-08 13:46:17 | INFO |   Encoded 71/600
2026-05-08 13:46:17 | INFO |   Encoded 72/600
2026-05-08 13:46:17 | INFO |   Encoded 73/600
2026-05-08 13:46:17 | INFO |   Encoded 74/600
2026-05-08 13:46:17 | INFO |   Encoded 75/600
2026-05-08 13:46:17 | INFO |   Encoded 76/600
2026-05-08 13:46:17 | INFO |   Encoded 77/600
2026-05-08 13:46:17 | INFO |   Encoded 78/600
2026-05-08 13:46:17 | INFO |   Encoded 79/600
2026-05-08 13:46:17 | INFO |   Encoded 80/600
2026-05-08 13:46:17 | INFO |   Encoded 81/600
2026-05-08 13:46:17 | INFO |   Encoded 82/600
2026-05-08 13:46:17 | INFO |   Encoded 83/600
2026-05-08 13:46:17 | INFO |   Encoded 84/600
2026-05-08 13:46:17 | INFO |   Encoded 85/600
2026-05-08 13:46:17 | INFO |   Encoded 86/600
2026-05-08 13:46:17 | INFO |   Encoded 87/600
2026-05-08 13:46:17 | INFO |   Encoded 88/600
2026-05-08 13:46:17 | INFO |   Encoded 89/600
2026-05-08 13:46:17 | INFO |   Encoded 90/600
2026-05-08 13:46:17 | INFO |   Encoded 91/600
2026-05-08 13:46:17 | INFO |   Encoded 92/600
2026-05-08 13:46:17 | INFO |   Encoded 93/600
2026-05-08 13:46:17 | INFO |   Encoded 94/600
2026-05-08 13:46:17 | INFO |   Encoded 95/600
2026-05-08 13:46:17 | INFO |   Encoded 96/600
2026-05-08 13:46:17 | INFO |   Encoded 97/600
2026-05-08 13:46:17 | INFO |   Encoded 98/600
2026-05-08 13:46:17 | INFO |   Encoded 99/600
2026-05-08 13:46:17 | INFO |   Encoded 100/600
2026-05-08 13:46:17 | INFO |   Encoded 101/600
2026-05-08 13:46:17 | INFO |   Encoded 102/600
2026-05-08 13:46:17 | INFO |   Encoded 103/600
2026-05-08 13:46:17 | INFO |   Encoded 104/600
2026-05-08 13:46:17 | INFO |   Encoded 105/600
2026-05-08 13:46:17 | INFO |   Encoded 106/600
2026-05-08 13:46:17 | INFO |   Encoded 107/600
2026-05-08 13:46:17 | INFO |   Encoded 108/600
2026-05-08 13:46:17 | INFO |   Encoded 109/600
2026-05-08 13:46:17 | INFO |   Encoded 110/600
2026-05-08 13:46:17 | INFO |   Encoded 111/600
2026-05-08 13:46:17 | INFO |   Encoded 112/600
2026-05-08 13:46:17 | INFO |   Encoded 113/600
2026-05-08 13:46:17 | INFO |   Encoded 114/600
2026-05-08 13:46:17 | INFO |   Encoded 115/600
2026-05-08 13:46:17 | INFO |   Encoded 116/600
2026-05-08 13:46:17 | INFO |   Encoded 117/600
2026-05-08 13:46:17 | INFO |   Encoded 118/600
2026-05-08 13:46:17 | INFO |   Encoded 119/600
2026-05-08 13:46:17 | INFO |   Encoded 120/600
2026-05-08 13:46:17 | INFO |   Encoded 121/600
2026-05-08 13:46:17 | INFO |   Encoded 122/600
2026-05-08 13:46:17 | INFO |   Encoded 123/600
2026-05-08 13:46:17 | INFO |   Encoded 124/600
2026-05-08 13:46:17 | INFO |   Encoded 125/600
2026-05-08 13:46:17 | INFO |   Encoded 126/600
2026-05-08 13:46:17 | INFO |   Encoded 127/600
2026-05-08 13:46:17 | INFO |   Encoded 128/600
2026-05-08 13:46:17 | INFO |   Encoded 129/600
2026-05-08 13:46:17 | INFO |   Encoded 130/600
2026-05-08 13:46:17 | INFO |   Encoded 131/600
2026-05-08 13:46:17 | INFO |   Encoded 132/600
2026-05-08 13:46:17 | INFO |   Encoded 133/600
2026-05-08 13:46:17 | INFO |   Encoded 134/600
2026-05-08 13:46:17 | INFO |   Encoded 135/600
2026-05-08 13:46:17 | INFO |   Encoded 136/600
2026-05-08 13:46:17 | INFO |   Encoded 137/600
2026-05-08 13:46:17 | INFO |   Encoded 138/600
2026-05-08 13:46:17 | INFO |   Encoded 139/600
2026-05-08 13:46:17 | INFO |   Encoded 140/600
2026-05-08 13:46:17 | INFO |   Encoded 141/600
2026-05-08 13:46:17 | INFO |   Encoded 142/600
2026-05-08 13:46:17 | INFO |   Encoded 143/600
2026-05-08 13:46:17 | INFO |   Encoded 144/600
2026-05-08 13:46:17 | INFO |   Encoded 145/600
2026-05-08 13:46:17 | INFO |   Encoded 146/600
2026-05-08 13:46:17 | INFO |   Encoded 147/600
2026-05-08 13:46:17 | INFO |   Encoded 148/600
2026-05-08 13:46:17 | INFO |   Encoded 149/600
2026-05-08 13:46:17 | INFO |   Encoded 150/600
2026-05-08 13:46:17 | INFO |   Encoded 151/600
2026-05-08 13:46:17 | INFO |   Encoded 152/600
2026-05-08 13:46:17 | INFO |   Encoded 153/600
2026-05-08 13:46:17 | INFO |   Encoded 154/600
2026-05-08 13:46:17 | INFO |   Encoded 155/600
2026-05-08 13:46:17 | INFO |   Encoded 156/600
2026-05-08 13:46:17 | INFO |   Encoded 157/600
2026-05-08 13:46:17 | INFO |   Encoded 158/600
2026-05-08 13:46:17 | INFO |   Encoded 159/600
2026-05-08 13:46:17 | INFO |   Encoded 160/600
2026-05-08 13:46:17 | INFO |   Encoded 161/600
2026-05-08 13:46:17 | INFO |   Encoded 162/600
2026-05-08 13:46:17 | INFO |   Encoded 163/600
2026-05-08 13:46:17 | INFO |   Encoded 164/600
2026-05-08 13:46:17 | INFO |   Encoded 165/600
2026-05-08 13:46:17 | INFO |   Encoded 166/600
2026-05-08 13:46:17 | INFO |   Encoded 167/600
2026-05-08 13:46:17 | INFO |   Encoded 168/600
2026-05-08 13:46:17 | INFO |   Encoded 169/600
2026-05-08 13:46:17 | INFO |   Encoded 170/600
2026-05-08 13:46:17 | INFO |   Encoded 171/600
2026-05-08 13:46:17 | INFO |   Encoded 172/600
2026-05-08 13:46:17 | INFO |   Encoded 173/600
2026-05-08 13:46:17 | INFO |   Encoded 174/600
2026-05-08 13:46:17 | INFO |   Encoded 175/600
2026-05-08 13:46:17 | INFO |   Encoded 176/600
2026-05-08 13:46:17 | INFO |   Encoded 177/600
2026-05-08 13:46:17 | INFO |   Encoded 178/600
2026-05-08 13:46:17 | INFO |   Encoded 179/600
2026-05-08 13:46:17 | INFO |   Encoded 180/600
2026-05-08 13:46:17 | INFO |   Encoded 181/600
2026-05-08 13:46:17 | INFO |   Encoded 182/600
2026-05-08 13:46:17 | INFO |   Encoded 183/600
2026-05-08 13:46:17 | INFO |   Encoded 184/600
2026-05-08 13:46:17 | INFO |   Encoded 185/600
2026-05-08 13:46:17 | INFO |   Encoded 186/600
2026-05-08 13:46:17 | INFO |   Encoded 187/600
2026-05-08 13:46:17 | INFO |   Encoded 188/600
2026-05-08 13:46:17 | INFO |   Encoded 189/600
2026-05-08 13:46:17 | INFO |   Encoded 190/600
2026-05-08 13:46:17 | INFO |   Encoded 191/600
2026-05-08 13:46:17 | INFO |   Encoded 192/600
2026-05-08 13:46:17 | INFO |   Encoded 193/600
2026-05-08 13:46:17 | INFO |   Encoded 194/600
2026-05-08 13:46:17 | INFO |   Encoded 195/600
2026-05-08 13:46:17 | INFO |   Encoded 196/600
2026-05-08 13:46:17 | INFO |   Encoded 197/600
2026-05-08 13:46:17 | INFO |   Encoded 198/600
2026-05-08 13:46:17 | INFO |   Encoded 199/600
2026-05-08 13:46:17 | INFO |   Encoded 200/600
2026-05-08 13:46:17 | INFO |   Encoded 201/600
2026-05-08 13:46:17 | INFO |   Encoded 202/600
2026-05-08 13:46:17 | INFO |   Encoded 203/600
2026-05-08 13:46:17 | INFO |   Encoded 204/600
2026-05-08 13:46:17 | INFO |   Encoded 205/600
2026-05-08 13:46:17 | INFO |   Encoded 206/600
2026-05-08 13:46:17 | INFO |   Encoded 207/600
2026-05-08 13:46:17 | INFO |   Encoded 208/600
2026-05-08 13:46:17 | INFO |   Encoded 209/600
2026-05-08 13:46:17 | INFO |   Encoded 210/600
2026-05-08 13:46:17 | INFO |   Encoded 211/600
2026-05-08 13:46:17 | INFO |   Encoded 212/600
2026-05-08 13:46:17 | INFO |   Encoded 213/600
2026-05-08 13:46:17 | INFO |   Encoded 214/600
2026-05-08 13:46:17 | INFO |   Encoded 215/600
2026-05-08 13:46:17 | INFO |   Encoded 216/600
2026-05-08 13:46:17 | INFO |   Encoded 217/600
2026-05-08 13:46:17 | INFO |   Encoded 218/600
2026-05-08 13:46:17 | INFO |   Encoded 219/600
2026-05-08 13:46:17 | INFO |   Encoded 220/600
2026-05-08 13:46:17 | INFO |   Encoded 221/600
2026-05-08 13:46:17 | INFO |   Encoded 222/600
2026-05-08 13:46:17 | INFO |   Encoded 223/600
2026-05-08 13:46:17 | INFO |   Encoded 224/600
2026-05-08 13:46:17 | INFO |   Encoded 225/600
2026-05-08 13:46:17 | INFO |   Encoded 226/600
2026-05-08 13:46:17 | INFO |   Encoded 227/600
2026-05-08 13:46:17 | INFO |   Encoded 228/600
2026-05-08 13:46:17 | INFO |   Encoded 229/600
2026-05-08 13:46:17 | INFO |   Encoded 230/600
2026-05-08 13:46:17 | INFO |   Encoded 231/600
2026-05-08 13:46:17 | INFO |   Encoded 232/600
2026-05-08 13:46:17 | INFO |   Encoded 233/600
2026-05-08 13:46:17 | INFO |   Encoded 234/600
2026-05-08 13:46:17 | INFO |   Encoded 235/600
2026-05-08 13:46:17 | INFO |   Encoded 236/600
2026-05-08 13:46:17 | INFO |   Encoded 237/600
2026-05-08 13:46:17 | INFO |   Encoded 238/600
2026-05-08 13:46:17 | INFO |   Encoded 239/600
2026-05-08 13:46:17 | INFO |   Encoded 240/600
2026-05-08 13:46:17 | INFO |   Encoded 241/600
2026-05-08 13:46:17 | INFO |   Encoded 242/600
2026-05-08 13:46:17 | INFO |   Encoded 243/600
2026-05-08 13:46:17 | INFO |   Encoded 244/600
2026-05-08 13:46:17 | INFO |   Encoded 245/600
2026-05-08 13:46:17 | INFO |   Encoded 246/600
2026-05-08 13:46:17 | INFO |   Encoded 247/600
2026-05-08 13:46:17 | INFO |   Encoded 248/600
2026-05-08 13:46:17 | INFO |   Encoded 249/600
2026-05-08 13:46:17 | INFO |   Encoded 250/600
2026-05-08 13:46:17 | INFO |   Encoded 251/600
2026-05-08 13:46:17 | INFO |   Encoded 252/600
2026-05-08 13:46:17 | INFO |   Encoded 253/600
2026-05-08 13:46:17 | INFO |   Encoded 254/600
2026-05-08 13:46:17 | INFO |   Encoded 255/600
2026-05-08 13:46:17 | INFO |   Encoded 256/600
2026-05-08 13:46:17 | INFO |   Encoded 257/600
2026-05-08 13:46:17 | INFO |   Encoded 258/600
2026-05-08 13:46:17 | INFO |   Encoded 259/600
2026-05-08 13:46:17 | INFO |   Encoded 260/600
2026-05-08 13:46:17 | INFO |   Encoded 261/600
2026-05-08 13:46:17 | INFO |   Encoded 262/600
2026-05-08 13:46:17 | INFO |   Encoded 263/600
2026-05-08 13:46:17 | INFO |   Encoded 264/600
2026-05-08 13:46:17 | INFO |   Encoded 265/600
2026-05-08 13:46:17 | INFO |   Encoded 266/600
2026-05-08 13:46:17 | INFO |   Encoded 267/600
2026-05-08 13:46:17 | INFO |   Encoded 268/600
2026-05-08 13:46:17 | INFO |   Encoded 269/600
2026-05-08 13:46:17 | INFO |   Encoded 270/600
2026-05-08 13:46:17 | INFO |   Encoded 271/600
2026-05-08 13:46:17 | INFO |   Encoded 272/600
2026-05-08 13:46:17 | INFO |   Encoded 273/600
2026-05-08 13:46:17 | INFO |   Encoded 274/600
2026-05-08 13:46:17 | INFO |   Encoded 275/600
2026-05-08 13:46:17 | INFO |   Encoded 276/600
2026-05-08 13:46:17 | INFO |   Encoded 277/600
2026-05-08 13:46:17 | INFO |   Encoded 278/600
2026-05-08 13:46:17 | INFO |   Encoded 279/600
2026-05-08 13:46:17 | INFO |   Encoded 280/600
2026-05-08 13:46:17 | INFO |   Encoded 281/600
2026-05-08 13:46:17 | INFO |   Encoded 282/600
2026-05-08 13:46:17 | INFO |   Encoded 283/600
2026-05-08 13:46:17 | INFO |   Encoded 284/600
2026-05-08 13:46:17 | INFO |   Encoded 285/600
2026-05-08 13:46:17 | INFO |   Encoded 286/600
2026-05-08 13:46:17 | INFO |   Encoded 287/600
2026-05-08 13:46:17 | INFO |   Encoded 288/600
2026-05-08 13:46:17 | INFO |   Encoded 289/600
2026-05-08 13:46:17 | INFO |   Encoded 290/600
2026-05-08 13:46:17 | INFO |   Encoded 291/600
2026-05-08 13:46:17 | INFO |   Encoded 292/600
2026-05-08 13:46:17 | INFO |   Encoded 293/600
2026-05-08 13:46:17 | INFO |   Encoded 294/600
2026-05-08 13:46:17 | INFO |   Encoded 295/600
2026-05-08 13:46:17 | INFO |   Encoded 296/600
2026-05-08 13:46:17 | INFO |   Encoded 297/600
2026-05-08 13:46:17 | INFO |   Encoded 298/600
2026-05-08 13:46:17 | INFO |   Encoded 299/600
2026-05-08 13:46:17 | INFO |   Encoded 300/600
2026-05-08 13:46:17 | INFO |   Encoded 301/600
2026-05-08 13:46:17 | INFO |   Encoded 302/600
2026-05-08 13:46:17 | INFO |   Encoded 303/600
2026-05-08 13:46:17 | INFO |   Encoded 304/600
2026-05-08 13:46:17 | INFO |   Encoded 305/600
2026-05-08 13:46:17 | INFO |   Encoded 306/600
2026-05-08 13:46:17 | INFO |   Encoded 307/600
2026-05-08 13:46:17 | INFO |   Encoded 308/600
2026-05-08 13:46:17 | INFO |   Encoded 309/600
2026-05-08 13:46:17 | INFO |   Encoded 310/600
2026-05-08 13:46:17 | INFO |   Encoded 311/600
2026-05-08 13:46:17 | INFO |   Encoded 312/600
2026-05-08 13:46:17 | INFO |   Encoded 313/600
2026-05-08 13:46:17 | INFO |   Encoded 314/600
2026-05-08 13:46:17 | INFO |   Encoded 315/600
2026-05-08 13:46:17 | INFO |   Encoded 316/600
2026-05-08 13:46:17 | INFO |   Encoded 317/600
2026-05-08 13:46:17 | INFO |   Encoded 318/600
2026-05-08 13:46:17 | INFO |   Encoded 319/600
2026-05-08 13:46:17 | INFO |   Encoded 320/600
2026-05-08 13:46:17 | INFO |   Encoded 321/600
2026-05-08 13:46:17 | INFO |   Encoded 322/600
2026-05-08 13:46:17 | INFO |   Encoded 323/600
2026-05-08 13:46:17 | INFO |   Encoded 324/600
2026-05-08 13:46:17 | INFO |   Encoded 325/600
2026-05-08 13:46:17 | INFO |   Encoded 326/600
2026-05-08 13:46:17 | INFO |   Encoded 327/600
2026-05-08 13:46:17 | INFO |   Encoded 328/600
2026-05-08 13:46:17 | INFO |   Encoded 329/600
2026-05-08 13:46:17 | INFO |   Encoded 330/600
2026-05-08 13:46:17 | INFO |   Encoded 331/600
2026-05-08 13:46:17 | INFO |   Encoded 332/600
2026-05-08 13:46:17 | INFO |   Encoded 333/600
2026-05-08 13:46:17 | INFO |   Encoded 334/600
2026-05-08 13:46:17 | INFO |   Encoded 335/600
2026-05-08 13:46:17 | INFO |   Encoded 336/600
2026-05-08 13:46:17 | INFO |   Encoded 337/600
2026-05-08 13:46:17 | INFO |   Encoded 338/600
2026-05-08 13:46:17 | INFO |   Encoded 339/600
2026-05-08 13:46:17 | INFO |   Encoded 340/600
2026-05-08 13:46:17 | INFO |   Encoded 341/600
2026-05-08 13:46:17 | INFO |   Encoded 342/600
2026-05-08 13:46:17 | INFO |   Encoded 343/600
2026-05-08 13:46:17 | INFO |   Encoded 344/600
2026-05-08 13:46:17 | INFO |   Encoded 345/600
2026-05-08 13:46:17 | INFO |   Encoded 346/600
2026-05-08 13:46:17 | INFO |   Encoded 347/600
2026-05-08 13:46:17 | INFO |   Encoded 348/600
2026-05-08 13:46:17 | INFO |   Encoded 349/600
2026-05-08 13:46:17 | INFO |   Encoded 350/600
2026-05-08 13:46:17 | INFO |   Encoded 351/600
2026-05-08 13:46:17 | INFO |   Encoded 352/600
2026-05-08 13:46:17 | INFO |   Encoded 353/600
2026-05-08 13:46:17 | INFO |   Encoded 354/600
2026-05-08 13:46:17 | INFO |   Encoded 355/600
2026-05-08 13:46:17 | INFO |   Encoded 356/600
2026-05-08 13:46:17 | INFO |   Encoded 357/600
2026-05-08 13:46:17 | INFO |   Encoded 358/600
2026-05-08 13:46:17 | INFO |   Encoded 359/600
2026-05-08 13:46:17 | INFO |   Encoded 360/600
2026-05-08 13:46:17 | INFO |   Encoded 361/600
2026-05-08 13:46:17 | INFO |   Encoded 362/600
2026-05-08 13:46:17 | INFO |   Encoded 363/600
2026-05-08 13:46:17 | INFO |   Encoded 364/600
2026-05-08 13:46:17 | INFO |   Encoded 365/600
2026-05-08 13:46:17 | INFO |   Encoded 366/600
2026-05-08 13:46:17 | INFO |   Encoded 367/600
2026-05-08 13:46:17 | INFO |   Encoded 368/600
2026-05-08 13:46:17 | INFO |   Encoded 369/600
2026-05-08 13:46:17 | INFO |   Encoded 370/600
2026-05-08 13:46:17 | INFO |   Encoded 371/600
2026-05-08 13:46:17 | INFO |   Encoded 372/600
2026-05-08 13:46:17 | INFO |   Encoded 373/600
2026-05-08 13:46:17 | INFO |   Encoded 374/600
2026-05-08 13:46:17 | INFO |   Encoded 375/600
2026-05-08 13:46:17 | INFO |   Encoded 376/600
2026-05-08 13:46:17 | INFO |   Encoded 377/600
2026-05-08 13:46:17 | INFO |   Encoded 378/600
2026-05-08 13:46:17 | INFO |   Encoded 379/600
2026-05-08 13:46:17 | INFO |   Encoded 380/600
2026-05-08 13:46:17 | INFO |   Encoded 381/600
2026-05-08 13:46:17 | INFO |   Encoded 382/600
2026-05-08 13:46:17 | INFO |   Encoded 383/600
2026-05-08 13:46:17 | INFO |   Encoded 384/600
2026-05-08 13:46:17 | INFO |   Encoded 385/600
2026-05-08 13:46:17 | INFO |   Encoded 386/600
2026-05-08 13:46:17 | INFO |   Encoded 387/600
2026-05-08 13:46:17 | INFO |   Encoded 388/600
2026-05-08 13:46:17 | INFO |   Encoded 389/600
2026-05-08 13:46:17 | INFO |   Encoded 390/600
2026-05-08 13:46:17 | INFO |   Encoded 391/600
2026-05-08 13:46:17 | INFO |   Encoded 392/600
2026-05-08 13:46:17 | INFO |   Encoded 393/600
2026-05-08 13:46:17 | INFO |   Encoded 394/600
2026-05-08 13:46:17 | INFO |   Encoded 395/600
2026-05-08 13:46:17 | INFO |   Encoded 396/600
2026-05-08 13:46:17 | INFO |   Encoded 397/600
2026-05-08 13:46:17 | INFO |   Encoded 398/600
2026-05-08 13:46:17 | INFO |   Encoded 399/600
2026-05-08 13:46:17 | INFO |   Encoded 400/600
2026-05-08 13:46:17 | INFO |   Encoded 401/600
2026-05-08 13:46:17 | INFO |   Encoded 402/600
2026-05-08 13:46:17 | INFO |   Encoded 403/600
2026-05-08 13:46:17 | INFO |   Encoded 404/600
2026-05-08 13:46:17 | INFO |   Encoded 405/600
2026-05-08 13:46:17 | INFO |   Encoded 406/600
2026-05-08 13:46:17 | INFO |   Encoded 407/600
2026-05-08 13:46:17 | INFO |   Encoded 408/600
2026-05-08 13:46:17 | INFO |   Encoded 409/600
2026-05-08 13:46:17 | INFO |   Encoded 410/600
2026-05-08 13:46:17 | INFO |   Encoded 411/600
2026-05-08 13:46:17 | INFO |   Encoded 412/600
2026-05-08 13:46:17 | INFO |   Encoded 413/600
2026-05-08 13:46:17 | INFO |   Encoded 414/600
2026-05-08 13:46:17 | INFO |   Encoded 415/600
2026-05-08 13:46:17 | INFO |   Encoded 416/600
2026-05-08 13:46:17 | INFO |   Encoded 417/600
2026-05-08 13:46:17 | INFO |   Encoded 418/600
2026-05-08 13:46:17 | INFO |   Encoded 419/600
2026-05-08 13:46:17 | INFO |   Encoded 420/600
2026-05-08 13:46:17 | INFO |   Encoded 421/600
2026-05-08 13:46:17 | INFO |   Encoded 422/600
2026-05-08 13:46:17 | INFO |   Encoded 423/600
2026-05-08 13:46:17 | INFO |   Encoded 424/600
2026-05-08 13:46:17 | INFO |   Encoded 425/600
2026-05-08 13:46:17 | INFO |   Encoded 426/600
2026-05-08 13:46:17 | INFO |   Encoded 427/600
2026-05-08 13:46:17 | INFO |   Encoded 428/600
2026-05-08 13:46:17 | INFO |   Encoded 429/600
2026-05-08 13:46:17 | INFO |   Encoded 430/600
2026-05-08 13:46:17 | INFO |   Encoded 431/600
2026-05-08 13:46:17 | INFO |   Encoded 432/600
2026-05-08 13:46:17 | INFO |   Encoded 433/600
2026-05-08 13:46:17 | INFO |   Encoded 434/600
2026-05-08 13:46:17 | INFO |   Encoded 435/600
2026-05-08 13:46:17 | INFO |   Encoded 436/600
2026-05-08 13:46:17 | INFO |   Encoded 437/600
2026-05-08 13:46:17 | INFO |   Encoded 438/600
2026-05-08 13:46:17 | INFO |   Encoded 439/600
2026-05-08 13:46:17 | INFO |   Encoded 440/600
2026-05-08 13:46:17 | INFO |   Encoded 441/600
2026-05-08 13:46:17 | INFO |   Encoded 442/600
2026-05-08 13:46:17 | INFO |   Encoded 443/600
2026-05-08 13:46:17 | INFO |   Encoded 444/600
2026-05-08 13:46:17 | INFO |   Encoded 445/600
2026-05-08 13:46:17 | INFO |   Encoded 446/600
2026-05-08 13:46:17 | INFO |   Encoded 447/600
2026-05-08 13:46:17 | INFO |   Encoded 448/600
2026-05-08 13:46:17 | INFO |   Encoded 449/600
2026-05-08 13:46:17 | INFO |   Encoded 450/600
2026-05-08 13:46:17 | INFO |   Encoded 451/600
2026-05-08 13:46:17 | INFO |   Encoded 452/600
2026-05-08 13:46:17 | INFO |   Encoded 453/600
2026-05-08 13:46:17 | INFO |   Encoded 454/600
2026-05-08 13:46:17 | INFO |   Encoded 455/600
2026-05-08 13:46:17 | INFO |   Encoded 456/600
2026-05-08 13:46:17 | INFO |   Encoded 457/600
2026-05-08 13:46:17 | INFO |   Encoded 458/600
2026-05-08 13:46:17 | INFO |   Encoded 459/600
2026-05-08 13:46:31 | INFO |   Encoded 460/600UserWarning: torch.utils.checkpoint: the use_reentrant parameter should be passed explicitly. Starting in PyTorch 2.9, calling checkpoint without use_reentrant will raise an exception. use_reentrant=False is recommended, but if you need to preserve the current default behavior, you can pass use_reentrant=True. Refer to docs for more details on the differences between the two variants.
2026-05-08 13:46:31 | INFO | UserWarning: None of the inputs have requires_grad=True. Gradients will be None
2026-05-08 13:46:35 | INFO | FutureWarning: `torch.cuda.amp.autocast(args...)` is deprecated. Please use `torch.amp.autocast('cuda', args...)` instead.
2026-05-08 13:47:09 | INFO | UserWarning: torch.utils.checkpoint: the use_reentrant parameter should be passed explicitly. Starting in PyTorch 2.9, calling checkpoint without use_reentrant will raise an exception. use_reentrant=False is recommended, but if you need to preserve the current default behavior, you can pass use_reentrant=True. Refer to docs for more details on the differences between the two variants.
2026-05-08 13:47:09 | INFO | UserWarning: None of the inputs have requires_grad=True. Gradients will be None
2026-05-08 13:47:13 | INFO | FutureWarning: `torch.cuda.amp.autocast(args...)` is deprecated. Please use `torch.amp.autocast('cuda', args...)` instead.
2026-05-08 13:47:47 | INFO | UserWarning: torch.utils.checkpoint: the use_reentrant parameter should be passed explicitly. Starting in PyTorch 2.9, calling checkpoint without use_reentrant will raise an exception. use_reentrant=False is recommended, but if you need to preserve the current default behavior, you can pass use_reentrant=True. Refer to docs for more details on the differences between the two variants.
2026-05-08 13:47:47 | INFO | UserWarning: None of the inputs have requires_grad=True. Gradients will be None
2026-05-08 13:47:50 | INFO | FutureWarning: `torch.cuda.amp.autocast(args...)` is deprecated. Please use `torch.amp.autocast('cuda', args...)` instead.
2026-05-08 13:48:15 | INFO | UserWarning: torch.utils.checkpoint: the use_reentrant parameter should be passed explicitly. Starting in PyTorch 2.9, calling checkpoint without use_reentrant will raise an exception. use_reentrant=False is recommended, but if you need to preserve the current default behavior, you can pass use_reentrant=True. Refer to docs for more details on the differences between the two variants.
2026-05-08 13:48:15 | INFO | UserWarning: None of the inputs have requires_grad=True. Gradients will be None
2026-05-08 13:48:18 | INFO | FutureWarning: `torch.cuda.amp.autocast(args...)` is deprecated. Please use `torch.amp.autocast('cuda', args...)` instead.
2026-05-08 13:48:28 | INFO | 
2026-05-08 13:48:28 | INFO |   Encoded 461/600
2026-05-08 13:48:28 | INFO |   Encoded 462/600
2026-05-08 13:48:28 | INFO |   Encoded 463/600
2026-05-08 13:48:28 | INFO |   Encoded 464/600
2026-05-08 13:48:28 | INFO |   Encoded 465/600
2026-05-08 13:48:28 | INFO |   Encoded 466/600
2026-05-08 13:48:28 | INFO |   Encoded 467/600
2026-05-08 13:48:28 | INFO |   Encoded 468/600
2026-05-08 13:48:28 | INFO |   Encoded 469/600
2026-05-08 13:48:28 | INFO |   Encoded 470/600
2026-05-08 13:48:28 | INFO |   Encoded 471/600
2026-05-08 13:48:28 | INFO |   Encoded 472/600
2026-05-08 13:48:28 | INFO |   Encoded 473/600
2026-05-08 13:48:28 | INFO |   Encoded 474/600
2026-05-08 13:48:28 | INFO |   Encoded 475/600
2026-05-08 13:48:28 | INFO |   Encoded 476/600
2026-05-08 13:48:28 | INFO |   Encoded 477/600
2026-05-08 13:48:28 | INFO |   Encoded 478/600
2026-05-08 13:48:28 | INFO |   Encoded 479/600
2026-05-08 13:48:28 | INFO |   Encoded 480/600
2026-05-08 13:48:28 | INFO |   Encoded 481/600
2026-05-08 13:48:28 | INFO |   Encoded 482/600
2026-05-08 13:48:28 | INFO |   Encoded 483/600
2026-05-08 13:48:28 | INFO |   Encoded 484/600
2026-05-08 13:48:28 | INFO |   Encoded 485/600
2026-05-08 13:48:28 | INFO |   Encoded 486/600
2026-05-08 13:48:28 | INFO |   Encoded 487/600
2026-05-08 13:48:28 | INFO |   Encoded 488/600
2026-05-08 13:48:28 | INFO |   Encoded 489/600
2026-05-08 13:48:28 | INFO |   Encoded 490/600
2026-05-08 13:48:28 | INFO |   Encoded 491/600
2026-05-08 13:48:28 | INFO |   Encoded 492/600
2026-05-08 13:48:28 | INFO |   Encoded 493/600
2026-05-08 13:48:28 | INFO |   Encoded 494/600
2026-05-08 13:48:28 | INFO |   Encoded 495/600
2026-05-08 13:48:28 | INFO |   Encoded 496/600
2026-05-08 13:48:28 | INFO |   Encoded 497/600
2026-05-08 13:48:28 | INFO |   Encoded 498/600
2026-05-08 13:48:28 | INFO |   Encoded 499/600
2026-05-08 13:48:28 | INFO |   Encoded 500/600
2026-05-08 13:48:28 | INFO |   Encoded 501/600
2026-05-08 13:48:28 | INFO |   Encoded 502/600
2026-05-08 13:48:28 | INFO |   Encoded 503/600
2026-05-08 13:48:28 | INFO |   Encoded 504/600
2026-05-08 13:48:28 | INFO |   Encoded 505/600
2026-05-08 13:48:28 | INFO |   Encoded 506/600
2026-05-08 13:48:28 | INFO |   Encoded 507/600
2026-05-08 13:48:28 | INFO |   Encoded 508/600
2026-05-08 13:48:28 | INFO |   Encoded 509/600
2026-05-08 13:48:28 | INFO |   Encoded 510/600
2026-05-08 13:48:28 | INFO |   Encoded 511/600
2026-05-08 13:48:28 | INFO |   Encoded 512/600
2026-05-08 13:48:28 | INFO |   Encoded 513/600
2026-05-08 13:48:28 | INFO |   Encoded 514/600
2026-05-08 13:48:28 | INFO |   Encoded 515/600
2026-05-08 13:48:28 | INFO |   Encoded 516/600
2026-05-08 13:48:28 | INFO |   Encoded 517/600
2026-05-08 13:48:28 | INFO |   Encoded 518/600
2026-05-08 13:48:28 | INFO |   Encoded 519/600
2026-05-08 13:48:28 | INFO |   Encoded 520/600
2026-05-08 13:48:28 | INFO |   Encoded 521/600
2026-05-08 13:48:28 | INFO |   Encoded 522/600
2026-05-08 13:48:28 | INFO |   Encoded 523/600
2026-05-08 13:48:28 | INFO |   Encoded 524/600
2026-05-08 13:48:28 | INFO |   Encoded 525/600
2026-05-08 13:48:28 | INFO |   Encoded 526/600
2026-05-08 13:48:28 | INFO |   Encoded 527/600
2026-05-08 13:48:28 | INFO |   Encoded 528/600
2026-05-08 13:48:28 | INFO |   Encoded 529/600
2026-05-08 13:48:28 | INFO |   Encoded 530/600
2026-05-08 13:48:28 | INFO |   Encoded 531/600
2026-05-08 13:48:28 | INFO |   Encoded 532/600
2026-05-08 13:48:28 | INFO |   Encoded 533/600
2026-05-08 13:48:28 | INFO |   Encoded 534/600
2026-05-08 13:48:28 | INFO |   Encoded 535/600
2026-05-08 13:48:28 | INFO |   Encoded 536/600
2026-05-08 13:48:28 | INFO |   Encoded 537/600
2026-05-08 13:48:28 | INFO |   Encoded 538/600
2026-05-08 13:48:28 | INFO |   Encoded 539/600
2026-05-08 13:48:28 | INFO |   Encoded 540/600
2026-05-08 13:48:28 | INFO |   Encoded 541/600
2026-05-08 13:48:28 | INFO |   Encoded 542/600
2026-05-08 13:48:28 | INFO |   Encoded 543/600
2026-05-08 13:48:28 | INFO |   Encoded 544/600
2026-05-08 13:48:28 | INFO |   Encoded 545/600
2026-05-08 13:48:28 | INFO |   Encoded 546/600
2026-05-08 13:48:28 | INFO |   Encoded 547/600
2026-05-08 13:48:28 | INFO |   Encoded 548/600
2026-05-08 13:48:28 | INFO |   Encoded 549/600
2026-05-08 13:48:28 | INFO |   Encoded 550/600
2026-05-08 13:48:28 | INFO |   Encoded 551/600
2026-05-08 13:48:28 | INFO |   Encoded 552/600
2026-05-08 13:48:28 | INFO |   Encoded 553/600
2026-05-08 13:48:28 | INFO |   Encoded 554/600
2026-05-08 13:48:28 | INFO |   Encoded 555/600
2026-05-08 13:48:28 | INFO |   Encoded 556/600
2026-05-08 13:48:28 | INFO |   Encoded 557/600
2026-05-08 13:48:28 | INFO |   Encoded 558/600
2026-05-08 13:48:28 | INFO |   Encoded 559/600
2026-05-08 13:48:28 | INFO |   Encoded 560/600
2026-05-08 13:48:28 | INFO |   Encoded 561/600
2026-05-08 13:48:28 | INFO |   Encoded 562/600
2026-05-08 13:48:28 | INFO |   Encoded 563/600
2026-05-08 13:48:28 | INFO |   Encoded 564/600
2026-05-08 13:48:28 | INFO |   Encoded 565/600
2026-05-08 13:48:28 | INFO |   Encoded 566/600
2026-05-08 13:48:28 | INFO |   Encoded 567/600
2026-05-08 13:48:28 | INFO |   Encoded 568/600
2026-05-08 13:48:28 | INFO |   Encoded 569/600
2026-05-08 13:48:28 | INFO |   Encoded 570/600
2026-05-08 13:48:28 | INFO |   Encoded 571/600
2026-05-08 13:48:28 | INFO |   Encoded 572/600
2026-05-08 13:48:28 | INFO |   Encoded 573/600
2026-05-08 13:48:28 | INFO |   Encoded 574/600
2026-05-08 13:48:28 | INFO |   Encoded 575/600
2026-05-08 13:48:28 | INFO |   Encoded 576/600
2026-05-08 13:48:28 | INFO |   Encoded 577/600
2026-05-08 13:48:28 | INFO |   Encoded 578/600
2026-05-08 13:48:28 | INFO |   Encoded 579/600
2026-05-08 13:48:28 | INFO |   Encoded 580/600
2026-05-08 13:48:28 | INFO |   Encoded 581/600
2026-05-08 13:48:28 | INFO |   Encoded 582/600
2026-05-08 13:48:28 | INFO |   Encoded 583/600
2026-05-08 13:48:28 | INFO |   Encoded 584/600
2026-05-08 13:48:28 | INFO |   Encoded 585/600
2026-05-08 13:48:28 | INFO |   Encoded 586/600
2026-05-08 13:48:28 | INFO |   Encoded 587/600
2026-05-08 13:48:28 | INFO |   Encoded 588/600
2026-05-08 13:48:28 | INFO |   Encoded 589/600
2026-05-08 13:48:28 | INFO |   Encoded 590/600
2026-05-08 13:48:28 | INFO |   Encoded 591/600
2026-05-08 13:48:28 | INFO |   Encoded 592/600
2026-05-08 13:48:28 | INFO |   Encoded 593/600
2026-05-08 13:48:28 | INFO |   Encoded 594/600
2026-05-08 13:48:28 | INFO |   Encoded 595/600
2026-05-08 13:48:28 | INFO |   Encoded 596/600
2026-05-08 13:48:28 | INFO |   Encoded 597/600
2026-05-08 13:48:28 | INFO |   Encoded 598/600
2026-05-08 13:48:28 | INFO |   Encoded 599/600
2026-05-08 13:48:28 | INFO |   Encoded 600/600
2026-05-08 13:48:28 | INFO | Computing similarity sequence...
2026-05-08 13:48:28 | INFO | 📼 CLIP similarity list calculated and saved.
2026-05-08 13:48:28 | INFO | 
2026-05-08 13:48:28 | INFO | 📂 Processing segment 0...
2026-05-08 13:48:28 | INFO | Taking screenshot: /sdcard/screenshot-0.png -> /Users/tanmaybhuskute/Documents/gifdroid-reproduction/apps/adaway/llm/ViBR_gemini/screenrec/run-006/artifacts/srv-002/step_0_screenshot-0.png
2026-05-08 13:48:28 | INFO | 🔍 Annotated DINO output saved to /Users/tanmaybhuskute/Documents/gifdroid-reproduction/apps/adaway/llm/ViBR_gemini/screenrec/run-006/artifacts/srv-002/step_0_dino.png
2026-05-08 13:48:28 | INFO | /Users/tanmaybhuskute/Documents/gifdroid-reproduction/apps/adaway/llm/ViBR_gemini/screenrec/run-006/artifacts/srv-002/step_0_dino.png
2026-05-08 13:48:28 | INFO | /Users/tanmaybhuskute/Documents/gifdroid-reproduction/apps/adaway/llm/ViBR_gemini/screenrec/run-006/artifacts/srv-002/step_0_tmp_stop.png
2026-05-08 13:48:28 | INFO | Relevant Region Response from Gemini: ```json
2026-05-08 13:48:28 | INFO | {
2026-05-08 13:48:28 | INFO |   "target_regions": [
2026-05-08 13:48:28 | INFO |     9
2026-05-08 13:48:28 | INFO |   ],
2026-05-08 13:48:28 | INFO |   "predicted_action": "tap"
2026-05-08 13:48:28 | INFO | }
2026-05-08 13:48:28 | INFO | ```
2026-05-08 13:48:28 | INFO | 🔍 Relevant regions: {'target_regions': [9], 'predicted_action': 'tap'}
2026-05-08 13:48:28 | INFO | 🧠 GPT selected regions: [9]
2026-05-08 13:48:28 | INFO | ✅ Relevant-only annotation saved to /Users/tanmaybhuskute/Documents/gifdroid-reproduction/apps/adaway/llm/ViBR_gemini/screenrec/run-006/artifacts/srv-002/step_0_relevant_regions.png
2026-05-08 13:48:28 | INFO | /Users/tanmaybhuskute/Documents/gifdroid-reproduction/apps/adaway/llm/ViBR_gemini/screenrec/run-006/artifacts/srv-002/step_0_relevant_regions.png
2026-05-08 13:48:28 | INFO | /Users/tanmaybhuskute/Documents/gifdroid-reproduction/apps/adaway/llm/ViBR_gemini/screenrec/run-006/artifacts/srv-002/step_0_screenshot-0.png
2026-05-08 13:48:28 | INFO | Consistency Response from Gemini: ```json
2026-05-08 13:48:28 | INFO | {
2026-05-08 13:48:28 | INFO |   "same_state": "no",
2026-05-08 13:48:28 | INFO |   "description": "The reference screen shows the app's page in an app store or management interface, with an 'Open' button. The current screen is the main interface of the app itself, which is what you see after opening it. The action 'Open' cannot be performed from the current screen because the app is already open."
2026-05-08 13:48:28 | INFO | }
2026-05-08 13:48:28 | INFO | ```
2026-05-08 13:48:28 | INFO | 🔄 Attempting to align state (try 1/3)...
2026-05-08 13:48:28 | INFO | /Users/tanmaybhuskute/Documents/gifdroid-reproduction/apps/adaway/llm/ViBR_gemini/screenrec/run-006/artifacts/srv-002/step_0_tmp_start.png
2026-05-08 13:48:28 | INFO | /Users/tanmaybhuskute/Documents/gifdroid-reproduction/apps/adaway/llm/ViBR_gemini/screenrec/run-006/artifacts/srv-002/step_0_tmp_stop.png
2026-05-08 13:48:28 | INFO | /Users/tanmaybhuskute/Documents/gifdroid-reproduction/apps/adaway/llm/ViBR_gemini/screenrec/run-006/artifacts/srv-002/step_0_labeled.png
2026-05-08 13:48:28 | INFO | Region Action Response from Gemini: ```json
2026-05-08 13:48:28 | INFO | {
2026-05-08 13:48:28 | INFO |   "action": "tap",
2026-05-08 13:48:28 | INFO |   "region": 0,
2026-05-08 13:48:28 | INFO |   "description": "Tap on the version number 6.1.4"
2026-05-08 13:48:28 | INFO | }
2026-05-08 13:48:28 | INFO | ```
2026-05-08 13:48:28 | INFO | 🎯 Recovery using region index: 0 at (1008, 115)
2026-05-08 13:48:28 | INFO | [1] Tap on the version number 6.1.4 -> tap
2026-05-08 13:48:28 | INFO | Taking screenshot: /sdcard/screenshot-0.png -> /Users/tanmaybhuskute/Documents/gifdroid-reproduction/apps/adaway/llm/ViBR_gemini/screenrec/run-006/artifacts/srv-002/step_0_screenshot-0.png
2026-05-08 13:48:28 | INFO | /Users/tanmaybhuskute/Documents/gifdroid-reproduction/apps/adaway/llm/ViBR_gemini/screenrec/run-006/artifacts/srv-002/step_0_tmp_start.png
2026-05-08 13:48:28 | INFO | /Users/tanmaybhuskute/Documents/gifdroid-reproduction/apps/adaway/llm/ViBR_gemini/screenrec/run-006/artifacts/srv-002/step_0_screenshot-0.png
2026-05-08 13:48:28 | INFO | Consistency Response from Gemini: ```json
2026-05-08 13:48:28 | INFO | {
2026-05-08 13:48:28 | INFO |   "same_state": "no",
2026-05-08 13:48:28 | INFO |   "description": "The reference screen shows the app's page in an app store or manager, with options to 'Uninstall' or 'Open' the app. The current screen is the main interface of the app itself, showing an 'up-to-date' status. The two screens are completely different and offer different functionalities."
2026-05-08 13:48:28 | INFO | }
2026-05-08 13:48:28 | INFO | ```
2026-05-08 13:48:28 | INFO | 🔄 Attempting to align state (try 2/3)...
2026-05-08 13:48:28 | INFO | /Users/tanmaybhuskute/Documents/gifdroid-reproduction/apps/adaway/llm/ViBR_gemini/screenrec/run-006/artifacts/srv-002/step_0_tmp_start.png
2026-05-08 13:48:28 | INFO | /Users/tanmaybhuskute/Documents/gifdroid-reproduction/apps/adaway/llm/ViBR_gemini/screenrec/run-006/artifacts/srv-002/step_0_tmp_stop.png
2026-05-08 13:48:28 | INFO | /Users/tanmaybhuskute/Documents/gifdroid-reproduction/apps/adaway/llm/ViBR_gemini/screenrec/run-006/artifacts/srv-002/step_0_labeled.png
2026-05-08 13:48:28 | INFO | Region Action Response from Gemini: ```json
2026-05-08 13:48:28 | INFO | {
2026-05-08 13:48:28 | INFO |   "action": "back",
2026-05-08 13:48:28 | INFO |   "description": "Go back to the previous screen."
2026-05-08 13:48:28 | INFO | }
2026-05-08 13:48:28 | INFO | ```
2026-05-08 13:48:28 | INFO | [1] Go back to the previous screen. -> back
2026-05-08 13:48:28 | INFO | Taking screenshot: /sdcard/screenshot-0.png -> /Users/tanmaybhuskute/Documents/gifdroid-reproduction/apps/adaway/llm/ViBR_gemini/screenrec/run-006/artifacts/srv-002/step_0_screenshot-0.png
2026-05-08 13:48:28 | INFO | /Users/tanmaybhuskute/Documents/gifdroid-reproduction/apps/adaway/llm/ViBR_gemini/screenrec/run-006/artifacts/srv-002/step_0_tmp_start.png
2026-05-08 13:48:28 | INFO | /Users/tanmaybhuskute/Documents/gifdroid-reproduction/apps/adaway/llm/ViBR_gemini/screenrec/run-006/artifacts/srv-002/step_0_screenshot-0.png
2026-05-08 13:48:28 | INFO | Consistency Response from Gemini: ```json
2026-05-08 13:48:28 | INFO | {
2026-05-08 13:48:28 | INFO |   "same_state": "no",
2026-05-08 13:48:28 | INFO |   "description": "The reference screen is an app store page for the AdAway app, with options to 'Uninstall' or 'Open' it. The current screen is the main interface of the AdAway app itself, which is the state after the app has been opened. The two screens represent completely different functionalities."
2026-05-08 13:48:28 | INFO | }
2026-05-08 13:48:28 | INFO | ```
2026-05-08 13:48:28 | INFO | 🔄 Attempting to align state (try 3/3)...
2026-05-08 13:48:28 | INFO | /Users/tanmaybhuskute/Documents/gifdroid-reproduction/apps/adaway/llm/ViBR_gemini/screenrec/run-006/artifacts/srv-002/step_0_tmp_start.png
2026-05-08 13:48:28 | INFO | /Users/tanmaybhuskute/Documents/gifdroid-reproduction/apps/adaway/llm/ViBR_gemini/screenrec/run-006/artifacts/srv-002/step_0_tmp_stop.png
2026-05-08 13:48:28 | INFO | /Users/tanmaybhuskute/Documents/gifdroid-reproduction/apps/adaway/llm/ViBR_gemini/screenrec/run-006/artifacts/srv-002/step_0_labeled.png
2026-05-08 13:48:28 | INFO | Region Action Response from Gemini: ```json
2026-05-08 13:48:28 | INFO | {
2026-05-08 13:48:28 | INFO |   "action": "no action",
2026-05-08 13:48:28 | INFO |   "description": "No Action needed."
2026-05-08 13:48:28 | INFO | }
2026-05-08 13:48:28 | INFO | ```
2026-05-08 13:48:28 | INFO | [1] No Action needed. -> no action
2026-05-08 13:48:28 | INFO | Taking screenshot: /sdcard/screenshot-0.png -> /Users/tanmaybhuskute/Documents/gifdroid-reproduction/apps/adaway/llm/ViBR_gemini/screenrec/run-006/artifacts/srv-002/step_0_screenshot-0.png
2026-05-08 13:48:54 | INFO | /Users/tanmaybhuskute/Documents/gifdroid-reproduction/apps/adaway/llm/ViBR_gemini/screenrec/run-006/artifacts/srv-002/step_0_tmp_start.pngUserWarning: torch.utils.checkpoint: the use_reentrant parameter should be passed explicitly. Starting in PyTorch 2.9, calling checkpoint without use_reentrant will raise an exception. use_reentrant=False is recommended, but if you need to preserve the current default behavior, you can pass use_reentrant=True. Refer to docs for more details on the differences between the two variants.
2026-05-08 13:48:54 | INFO | UserWarning: None of the inputs have requires_grad=True. Gradients will be None
2026-05-08 13:48:58 | INFO | FutureWarning: `torch.cuda.amp.autocast(args...)` is deprecated. Please use `torch.amp.autocast('cuda', args...)` instead.
2026-05-08 13:50:08 | INFO | UserWarning: torch.utils.checkpoint: the use_reentrant parameter should be passed explicitly. Starting in PyTorch 2.9, calling checkpoint without use_reentrant will raise an exception. use_reentrant=False is recommended, but if you need to preserve the current default behavior, you can pass use_reentrant=True. Refer to docs for more details on the differences between the two variants.
2026-05-08 13:50:08 | INFO | UserWarning: None of the inputs have requires_grad=True. Gradients will be None
2026-05-08 13:50:12 | INFO | FutureWarning: `torch.cuda.amp.autocast(args...)` is deprecated. Please use `torch.amp.autocast('cuda', args...)` instead.
2026-05-08 13:53:03 | INFO | 
2026-05-08 13:53:03 | INFO | /Users/tanmaybhuskute/Documents/gifdroid-reproduction/apps/adaway/llm/ViBR_gemini/screenrec/run-006/artifacts/srv-002/step_0_screenshot-0.png
2026-05-08 13:53:03 | INFO | Consistency Response from Gemini: ```json
2026-05-08 13:53:03 | INFO | {
2026-05-08 13:53:03 | INFO |   "same_state": "no",
2026-05-08 13:53:03 | INFO |   "description": "The reference screen is an app store page for the 'AdAway' app, showing options to 'Uninstall' or 'Open' it. The current screen is the main interface of the 'AdAway' app itself, which is the state after the app has been opened. The two screens have completely different functionalities and available actions."
2026-05-08 13:53:03 | INFO | }
2026-05-08 13:53:03 | INFO | ```
2026-05-08 13:53:03 | INFO | ⚠️ Skipping action: current GUI state does not match start state.
2026-05-08 13:53:03 | INFO | Mismatch reason: the reference screen is an app store page for the 'adaway' app, showing options to 'uninstall' or 'open' it. the current screen is the main interface of the 'adaway' app itself, which is the state after the app has been opened. the two screens have completely different functionalities and available actions.
2026-05-08 13:53:03 | INFO | 
2026-05-08 13:53:03 | INFO | 📂 Processing segment 1...
2026-05-08 13:53:03 | INFO | Taking screenshot: /sdcard/screenshot-0.png -> /Users/tanmaybhuskute/Documents/gifdroid-reproduction/apps/adaway/llm/ViBR_gemini/screenrec/run-006/artifacts/srv-002/step_1_screenshot-0.png
2026-05-08 13:53:03 | INFO | 🔍 Annotated DINO output saved to /Users/tanmaybhuskute/Documents/gifdroid-reproduction/apps/adaway/llm/ViBR_gemini/screenrec/run-006/artifacts/srv-002/step_1_dino.png
2026-05-08 13:53:03 | INFO | /Users/tanmaybhuskute/Documents/gifdroid-reproduction/apps/adaway/llm/ViBR_gemini/screenrec/run-006/artifacts/srv-002/step_1_dino.png
2026-05-08 13:53:03 | INFO | /Users/tanmaybhuskute/Documents/gifdroid-reproduction/apps/adaway/llm/ViBR_gemini/screenrec/run-006/artifacts/srv-002/step_1_tmp_stop.png
2026-05-08 13:53:03 | INFO | Relevant Region Response from Gemini: ```json
2026-05-08 13:53:03 | INFO | {
2026-05-08 13:53:03 | INFO |   "target_regions": [
2026-05-08 13:53:03 | INFO |     23
2026-05-08 13:53:03 | INFO |   ],
2026-05-08 13:53:03 | INFO |   "predicted_action": "tap"
2026-05-08 13:53:03 | INFO | }
2026-05-08 13:53:03 | INFO | ```
2026-05-08 13:53:03 | INFO | 🔍 Relevant regions: {'target_regions': [23], 'predicted_action': 'tap'}
2026-05-08 13:53:03 | INFO | 🧠 GPT selected regions: [23]
2026-05-08 13:53:03 | INFO | ✅ Relevant-only annotation saved to /Users/tanmaybhuskute/Documents/gifdroid-reproduction/apps/adaway/llm/ViBR_gemini/screenrec/run-006/artifacts/srv-002/step_1_relevant_regions.png
2026-05-08 13:53:03 | INFO | /Users/tanmaybhuskute/Documents/gifdroid-reproduction/apps/adaway/llm/ViBR_gemini/screenrec/run-006/artifacts/srv-002/step_1_relevant_regions.png
2026-05-08 13:53:03 | INFO | /Users/tanmaybhuskute/Documents/gifdroid-reproduction/apps/adaway/llm/ViBR_gemini/screenrec/run-006/artifacts/srv-002/step_1_screenshot-0.png
2026-05-08 13:53:03 | INFO | Consistency Response from Gemini: ```json
2026-05-08 13:53:03 | INFO | {
2026-05-08 13:53:03 | INFO |   "same_state": "yes"
2026-05-08 13:53:03 | INFO | }
2026-05-08 13:53:03 | INFO | ```
2026-05-08 13:53:03 | INFO | /Users/tanmaybhuskute/Documents/gifdroid-reproduction/apps/adaway/llm/ViBR_gemini/screenrec/run-006/artifacts/srv-002/step_1_relevant_regions.png
2026-05-08 13:53:03 | INFO | /Users/tanmaybhuskute/Documents/gifdroid-reproduction/apps/adaway/llm/ViBR_gemini/screenrec/run-006/artifacts/srv-002/step_1_tmp_stop.png
2026-05-08 13:53:03 | INFO | /Users/tanmaybhuskute/Documents/gifdroid-reproduction/apps/adaway/llm/ViBR_gemini/screenrec/run-006/artifacts/srv-002/step_1_labeled.png
2026-05-08 13:53:03 | INFO | Region Action Response from Gemini: ```json
2026-05-08 13:53:03 | INFO | {
2026-05-08 13:53:03 | INFO |   "action": "tap",
2026-05-08 13:53:03 | INFO |   "region": 5,
2026-05-08 13:53:03 | INFO |   "description": "Tap the refresh icon to update sources."
2026-05-08 13:53:03 | INFO | }
2026-05-08 13:53:03 | INFO | ```
2026-05-08 13:53:03 | INFO | 🎯 Using region index: 5 at (954, 765)
2026-05-08 13:53:03 | INFO | [1] Tap the refresh icon to update sources. -> tap
2026-05-08 13:53:03 | INFO | ✅ Action executed.
2026-05-08 13:53:03 | INFO | 
2026-05-08 13:53:03 | INFO | 
2026-05-08 13:53:03 | INFO | 📂 Processing segment 2...
2026-05-08 13:53:03 | INFO | Taking screenshot: /sdcard/screenshot-0.png -> /Users/tanmaybhuskute/Documents/gifdroid-reproduction/apps/adaway/llm/ViBR_gemini/screenrec/run-006/artifacts/srv-002/step_2_screenshot-0.png
2026-05-08 13:53:03 | INFO | 🔍 Annotated DINO output saved to /Users/tanmaybhuskute/Documents/gifdroid-reproduction/apps/adaway/llm/ViBR_gemini/screenrec/run-006/artifacts/srv-002/step_2_dino.png
2026-05-08 13:53:03 | INFO | /Users/tanmaybhuskute/Documents/gifdroid-reproduction/apps/adaway/llm/ViBR_gemini/screenrec/run-006/artifacts/srv-002/step_2_dino.png
2026-05-08 13:53:03 | INFO | /Users/tanmaybhuskute/Documents/gifdroid-reproduction/apps/adaway/llm/ViBR_gemini/screenrec/run-006/artifacts/srv-002/step_2_tmp_stop.png
2026-05-08 13:53:03 | INFO | Relevant Region Response from Gemini: ```json
2026-05-08 13:53:03 | INFO | {
2026-05-08 13:53:03 | INFO |   "target_regions": [
2026-05-08 13:53:03 | INFO |     21,
2026-05-08 13:53:03 | INFO |     26
2026-05-08 13:53:03 | INFO |   ],
2026-05-08 13:53:03 | INFO |   "predicted_action": "tap"
2026-05-08 13:53:03 | INFO | }
2026-05-08 13:53:03 | INFO | ```
2026-05-08 13:53:03 | INFO | 🔍 Relevant regions: {'target_regions': [21, 26], 'predicted_action': 'tap'}
2026-05-08 13:53:03 | INFO | 🧠 GPT selected regions: [21, 26]
2026-05-08 13:53:03 | INFO | ✅ Relevant-only annotation saved to /Users/tanmaybhuskute/Documents/gifdroid-reproduction/apps/adaway/llm/ViBR_gemini/screenrec/run-006/artifacts/srv-002/step_2_relevant_regions.png
2026-05-08 13:53:03 | INFO | /Users/tanmaybhuskute/Documents/gifdroid-reproduction/apps/adaway/llm/ViBR_gemini/screenrec/run-006/artifacts/srv-002/step_2_relevant_regions.png
2026-05-08 13:53:03 | INFO | /Users/tanmaybhuskute/Documents/gifdroid-reproduction/apps/adaway/llm/ViBR_gemini/screenrec/run-006/artifacts/srv-002/step_2_screenshot-0.png
2026-05-08 13:53:03 | INFO | Consistency Response from Gemini: ```json
2026-05-08 13:53:03 | INFO | {
2026-05-08 13:53:03 | INFO |   "same_state": "yes"
2026-05-08 13:53:03 | INFO | }
2026-05-08 13:53:03 | INFO | ```
2026-05-08 13:53:03 | INFO | /Users/tanmaybhuskute/Documents/gifdroid-reproduction/apps/adaway/llm/ViBR_gemini/screenrec/run-006/artifacts/srv-002/step_2_relevant_regions.png
2026-05-08 13:53:03 | INFO | /Users/tanmaybhuskute/Documents/gifdroid-reproduction/apps/adaway/llm/ViBR_gemini/screenrec/run-006/artifacts/srv-002/step_2_tmp_stop.png
2026-05-08 13:53:03 | INFO | /Users/tanmaybhuskute/Documents/gifdroid-reproduction/apps/adaway/llm/ViBR_gemini/screenrec/run-006/artifacts/srv-002/step_2_labeled.png
2026-05-08 13:53:03 | INFO | Region Action Response from Gemini: ```json
2026-05-08 13:53:03 | INFO | {
2026-05-08 13:53:03 | INFO |   "action": "tap",
2026-05-08 13:53:03 | INFO |   "region": 2,
2026-05-08 13:53:03 | INFO |   "description": "Tap on the 'Allowed' button."
2026-05-08 13:53:03 | INFO | }
2026-05-08 13:53:03 | INFO | ```
2026-05-08 13:53:03 | INFO | 🎯 Using region index: 2 at (540, 511)
2026-05-08 13:53:03 | INFO | [1] Tap on the 'Allowed' button. -> tap
2026-05-08 13:53:03 | INFO | ✅ Action executed.
2026-05-08 13:53:03 | INFO | 
2026-05-08 13:53:03 | INFO | 
2026-05-08 13:53:03 | INFO | 📂 Processing segment 3...
2026-05-08 13:53:03 | INFO | Taking screenshot: /sdcard/screenshot-0.png -> /Users/tanmaybhuskute/Documents/gifdroid-reproduction/apps/adaway/llm/ViBR_gemini/screenrec/run-006/artifacts/srv-002/step_3_screenshot-0.png
2026-05-08 13:53:03 | INFO | 🔍 Annotated DINO output saved to /Users/tanmaybhuskute/Documents/gifdroid-reproduction/apps/adaway/llm/ViBR_gemini/screenrec/run-006/artifacts/srv-002/step_3_dino.png
2026-05-08 13:53:03 | INFO | /Users/tanmaybhuskute/Documents/gifdroid-reproduction/apps/adaway/llm/ViBR_gemini/screenrec/run-006/artifacts/srv-002/step_3_dino.png
2026-05-08 13:53:03 | INFO | /Users/tanmaybhuskute/Documents/gifdroid-reproduction/apps/adaway/llm/ViBR_gemini/screenrec/run-006/artifacts/srv-002/step_3_tmp_stop.png
2026-05-08 13:53:03 | INFO | Relevant Region Response from Gemini: ```json
2026-05-08 13:53:03 | INFO | {
2026-05-08 13:53:03 | INFO |   "target_regions": [
2026-05-08 13:53:03 | INFO |     12
2026-05-08 13:53:03 | INFO |   ],
2026-05-08 13:53:03 | INFO |   "predicted_action": "tap"
2026-05-08 13:53:03 | INFO | }
2026-05-08 13:53:03 | INFO | ```
2026-05-08 13:53:03 | INFO | 🔍 Relevant regions: {'target_regions': [12], 'predicted_action': 'tap'}
2026-05-08 13:53:03 | INFO | 🧠 GPT selected regions: [12]
2026-05-08 13:53:03 | INFO | ✅ Relevant-only annotation saved to /Users/tanmaybhuskute/Documents/gifdroid-reproduction/apps/adaway/llm/ViBR_gemini/screenrec/run-006/artifacts/srv-002/step_3_relevant_regions.png
2026-05-08 13:53:03 | INFO | /Users/tanmaybhuskute/Documents/gifdroid-reproduction/apps/adaway/llm/ViBR_gemini/screenrec/run-006/artifacts/srv-002/step_3_relevant_regions.png
2026-05-08 13:53:03 | INFO | /Users/tanmaybhuskute/Documents/gifdroid-reproduction/apps/adaway/llm/ViBR_gemini/screenrec/run-006/artifacts/srv-002/step_3_screenshot-0.png
2026-05-08 13:53:03 | INFO | Consistency Response from Gemini: ```json
2026-05-08 13:53:03 | INFO | {
2026-05-08 13:53:03 | INFO |   "same_state": "yes"
2026-05-08 13:53:03 | INFO | }
2026-05-08 13:53:03 | INFO | ```
2026-05-08 13:53:03 | INFO | /Users/tanmaybhuskute/Documents/gifdroid-reproduction/apps/adaway/llm/ViBR_gemini/screenrec/run-006/artifacts/srv-002/step_3_relevant_regions.png
2026-05-08 13:53:03 | INFO | /Users/tanmaybhuskute/Documents/gifdroid-reproduction/apps/adaway/llm/ViBR_gemini/screenrec/run-006/artifacts/srv-002/step_3_tmp_stop.png
2026-05-08 13:53:03 | INFO | /Users/tanmaybhuskute/Documents/gifdroid-reproduction/apps/adaway/llm/ViBR_gemini/screenrec/run-006/artifacts/srv-002/step_3_labeled.png
2026-05-08 13:53:03 | INFO | Region Action Response from Gemini: ```json
2026-05-08 13:53:03 | INFO | {
2026-05-08 13:53:03 | INFO |   "action": "tap",
2026-05-08 13:53:03 | INFO |   "region": 3,
2026-05-08 13:53:03 | INFO |   "description": "Tap the plus button to add a new item to the list."
2026-05-08 13:53:03 | INFO | }
2026-05-08 13:53:03 | INFO | ```
2026-05-08 13:53:03 | INFO | 🎯 Using region index: 3 at (964, 1594)
2026-05-08 13:53:03 | INFO | [1] Tap the plus button to add a new item to the list. -> tap
2026-05-08 13:53:03 | INFO | ✅ Action executed.
2026-05-08 13:53:03 | INFO | 
2026-05-08 13:53:03 | INFO | 
2026-05-08 13:53:03 | INFO | 📂 Processing segment 4...
2026-05-08 13:53:03 | INFO | Taking screenshot: /sdcard/screenshot-0.png -> /Users/tanmaybhuskute/Documents/gifdroid-reproduction/apps/adaway/llm/ViBR_gemini/screenrec/run-006/artifacts/srv-002/step_4_screenshot-0.png
2026-05-08 13:53:03 | INFO | 🔍 Annotated DINO output saved to /Users/tanmaybhuskute/Documents/gifdroid-reproduction/apps/adaway/llm/ViBR_gemini/screenrec/run-006/artifacts/srv-002/step_4_dino.png
2026-05-08 13:53:03 | INFO | /Users/tanmaybhuskute/Documents/gifdroid-reproduction/apps/adaway/llm/ViBR_gemini/screenrec/run-006/artifacts/srv-002/step_4_dino.png
2026-05-08 13:53:03 | INFO | /Users/tanmaybhuskute/Documents/gifdroid-reproduction/apps/adaway/llm/ViBR_gemini/screenrec/run-006/artifacts/srv-002/step_4_tmp_stop.png
2026-05-08 13:53:03 | INFO | Relevant Region Response from Gemini: ```json
2026-05-08 13:53:03 | INFO | {
2026-05-08 13:53:03 | INFO |   "target_regions": [
2026-05-08 13:53:03 | INFO |     8
2026-05-08 13:53:03 | INFO |   ],
2026-05-08 13:53:03 | INFO |   "predicted_action": "input_text"
2026-05-08 13:53:03 | INFO | }
2026-05-08 13:53:03 | INFO | ```
2026-05-08 13:53:03 | INFO | 🔍 Relevant regions: {'target_regions': [8], 'predicted_action': 'input_text'}
2026-05-08 13:53:03 | INFO | 🧠 GPT selected regions: [8]
2026-05-08 13:53:54 | INFO | ✅ Relevant-only annotation saved to /Users/tanmaybhuskute/Documents/gifdroid-reproduction/apps/adaway/llm/ViBR_gemini/screenrec/run-006/artifacts/srv-002/step_4_relevant_regions.pngUserWarning: torch.utils.checkpoint: the use_reentrant parameter should be passed explicitly. Starting in PyTorch 2.9, calling checkpoint without use_reentrant will raise an exception. use_reentrant=False is recommended, but if you need to preserve the current default behavior, you can pass use_reentrant=True. Refer to docs for more details on the differences between the two variants.
2026-05-08 13:53:54 | INFO | UserWarning: None of the inputs have requires_grad=True. Gradients will be None
2026-05-08 13:53:57 | INFO | FutureWarning: `torch.cuda.amp.autocast(args...)` is deprecated. Please use `torch.amp.autocast('cuda', args...)` instead.
2026-05-08 13:55:55 | INFO | UserWarning: torch.utils.checkpoint: the use_reentrant parameter should be passed explicitly. Starting in PyTorch 2.9, calling checkpoint without use_reentrant will raise an exception. use_reentrant=False is recommended, but if you need to preserve the current default behavior, you can pass use_reentrant=True. Refer to docs for more details on the differences between the two variants.
2026-05-08 13:55:55 | INFO | UserWarning: None of the inputs have requires_grad=True. Gradients will be None
2026-05-08 13:55:59 | INFO | FutureWarning: `torch.cuda.amp.autocast(args...)` is deprecated. Please use `torch.amp.autocast('cuda', args...)` instead.
2026-05-08 13:57:20 | INFO | 
2026-05-08 13:57:20 | INFO | /Users/tanmaybhuskute/Documents/gifdroid-reproduction/apps/adaway/llm/ViBR_gemini/screenrec/run-006/artifacts/srv-002/step_4_relevant_regions.png
2026-05-08 13:57:20 | INFO | /Users/tanmaybhuskute/Documents/gifdroid-reproduction/apps/adaway/llm/ViBR_gemini/screenrec/run-006/artifacts/srv-002/step_4_screenshot-0.png
2026-05-08 13:57:20 | INFO | Consistency Response from Gemini: ```json
2026-05-08 13:57:20 | INFO | {
2026-05-08 13:57:20 | INFO |   "same_state": "yes"
2026-05-08 13:57:20 | INFO | }
2026-05-08 13:57:20 | INFO | ```
2026-05-08 13:57:20 | INFO | /Users/tanmaybhuskute/Documents/gifdroid-reproduction/apps/adaway/llm/ViBR_gemini/screenrec/run-006/artifacts/srv-002/step_4_relevant_regions.png
2026-05-08 13:57:20 | INFO | /Users/tanmaybhuskute/Documents/gifdroid-reproduction/apps/adaway/llm/ViBR_gemini/screenrec/run-006/artifacts/srv-002/step_4_tmp_stop.png
2026-05-08 13:57:20 | INFO | /Users/tanmaybhuskute/Documents/gifdroid-reproduction/apps/adaway/llm/ViBR_gemini/screenrec/run-006/artifacts/srv-002/step_4_labeled.png
2026-05-08 13:57:20 | INFO | Region Action Response from Gemini: ```json
2026-05-08 13:57:20 | INFO | {
2026-05-08 13:57:20 | INFO |   "action": "input_text",
2026-05-08 13:57:20 | INFO |   "text": "a",
2026-05-08 13:57:20 | INFO |   "description": "Type 'a' into the text input field with current value The hosts source URL."
2026-05-08 13:57:20 | INFO | }
2026-05-08 13:57:20 | INFO | ```
2026-05-08 13:57:20 | INFO | 🎯 Matched element: 'Add host to whitelist' at (349, 757)
2026-05-08 13:57:20 | INFO | [1] Type 'a' into the text input field with current value The hosts source URL. -> input_text
2026-05-08 13:57:20 | INFO | ✅ Action executed.
2026-05-08 13:57:20 | INFO | 
2026-05-08 13:57:20 | INFO | 
2026-05-08 13:57:20 | INFO | 📂 Processing segment 5...
2026-05-08 13:57:20 | INFO | Taking screenshot: /sdcard/screenshot-0.png -> /Users/tanmaybhuskute/Documents/gifdroid-reproduction/apps/adaway/llm/ViBR_gemini/screenrec/run-006/artifacts/srv-002/step_5_screenshot-0.png
2026-05-08 13:57:20 | INFO | 🔍 Annotated DINO output saved to /Users/tanmaybhuskute/Documents/gifdroid-reproduction/apps/adaway/llm/ViBR_gemini/screenrec/run-006/artifacts/srv-002/step_5_dino.png
2026-05-08 13:57:20 | INFO | /Users/tanmaybhuskute/Documents/gifdroid-reproduction/apps/adaway/llm/ViBR_gemini/screenrec/run-006/artifacts/srv-002/step_5_dino.png
2026-05-08 13:57:20 | INFO | /Users/tanmaybhuskute/Documents/gifdroid-reproduction/apps/adaway/llm/ViBR_gemini/screenrec/run-006/artifacts/srv-002/step_5_tmp_stop.png
2026-05-08 13:57:20 | INFO | Relevant Region Response from Gemini: ```json
2026-05-08 13:57:20 | INFO | {
2026-05-08 13:57:20 | INFO |   "target_regions": [
2026-05-08 13:57:20 | INFO |     9
2026-05-08 13:57:20 | INFO |   ],
2026-05-08 13:57:20 | INFO |   "predicted_action": "tap"
2026-05-08 13:57:20 | INFO | }
2026-05-08 13:57:20 | INFO | ```
2026-05-08 13:57:20 | INFO | 🔍 Relevant regions: {'target_regions': [9], 'predicted_action': 'tap'}
2026-05-08 13:57:20 | INFO | 🧠 GPT selected regions: [9]
2026-05-08 13:57:20 | INFO | ✅ Relevant-only annotation saved to /Users/tanmaybhuskute/Documents/gifdroid-reproduction/apps/adaway/llm/ViBR_gemini/screenrec/run-006/artifacts/srv-002/step_5_relevant_regions.png
2026-05-08 13:57:20 | INFO | /Users/tanmaybhuskute/Documents/gifdroid-reproduction/apps/adaway/llm/ViBR_gemini/screenrec/run-006/artifacts/srv-002/step_5_relevant_regions.png
2026-05-08 13:57:20 | INFO | /Users/tanmaybhuskute/Documents/gifdroid-reproduction/apps/adaway/llm/ViBR_gemini/screenrec/run-006/artifacts/srv-002/step_5_screenshot-0.png
2026-05-08 13:57:20 | INFO | Consistency Response from Gemini: ```json
2026-05-08 13:57:20 | INFO | {
2026-05-08 13:57:20 | INFO |   "same_state": "yes"
2026-05-08 13:57:20 | INFO | }
2026-05-08 13:57:20 | INFO | ```
2026-05-08 13:57:20 | INFO | /Users/tanmaybhuskute/Documents/gifdroid-reproduction/apps/adaway/llm/ViBR_gemini/screenrec/run-006/artifacts/srv-002/step_5_relevant_regions.png
2026-05-08 13:57:20 | INFO | /Users/tanmaybhuskute/Documents/gifdroid-reproduction/apps/adaway/llm/ViBR_gemini/screenrec/run-006/artifacts/srv-002/step_5_tmp_stop.png
2026-05-08 13:57:20 | INFO | /Users/tanmaybhuskute/Documents/gifdroid-reproduction/apps/adaway/llm/ViBR_gemini/screenrec/run-006/artifacts/srv-002/step_5_labeled.png
2026-05-08 13:57:20 | INFO | Region Action Response from Gemini: ```json
2026-05-08 13:57:20 | INFO | {
2026-05-08 13:57:20 | INFO |   "action": "tap",
2026-05-08 13:57:20 | INFO |   "region": 7,
2026-05-08 13:57:20 | INFO |   "description": "Tap the ADD button to add the host to the whitelist."
2026-05-08 13:57:20 | INFO | }
2026-05-08 13:57:20 | INFO | ```
2026-05-08 13:57:20 | INFO | 🎯 Using region index: 7 at (884, 1170)
2026-05-08 13:57:20 | INFO | [1] Tap the ADD button to add the host to the whitelist. -> tap
2026-05-08 13:57:20 | INFO | ✅ Action executed.
2026-05-08 13:57:20 | INFO | 
2026-05-08 13:57:20 | INFO | 
2026-05-08 13:57:20 | INFO | 📂 Processing segment 6...
2026-05-08 13:57:20 | INFO | Taking screenshot: /sdcard/screenshot-0.png -> /Users/tanmaybhuskute/Documents/gifdroid-reproduction/apps/adaway/llm/ViBR_gemini/screenrec/run-006/artifacts/srv-002/step_6_screenshot-0.png
2026-05-08 13:57:20 | INFO | 🔍 Annotated DINO output saved to /Users/tanmaybhuskute/Documents/gifdroid-reproduction/apps/adaway/llm/ViBR_gemini/screenrec/run-006/artifacts/srv-002/step_6_dino.png
2026-05-08 13:57:20 | INFO | /Users/tanmaybhuskute/Documents/gifdroid-reproduction/apps/adaway/llm/ViBR_gemini/screenrec/run-006/artifacts/srv-002/step_6_dino.png
2026-05-08 13:57:20 | INFO | /Users/tanmaybhuskute/Documents/gifdroid-reproduction/apps/adaway/llm/ViBR_gemini/screenrec/run-006/artifacts/srv-002/step_6_tmp_stop.png
2026-05-08 13:57:20 | INFO | Relevant Region Response from Gemini: ```json
2026-05-08 13:57:20 | INFO | {
2026-05-08 13:57:20 | INFO |   "target_regions": [
2026-05-08 13:57:20 | INFO |     12
2026-05-08 13:57:20 | INFO |   ],
2026-05-08 13:57:20 | INFO |   "predicted_action": "tap"
2026-05-08 13:57:20 | INFO | }
2026-05-08 13:57:20 | INFO | ```
2026-05-08 13:57:20 | INFO | 🔍 Relevant regions: {'target_regions': [12], 'predicted_action': 'tap'}
2026-05-08 13:57:20 | INFO | 🧠 GPT selected regions: [12]
2026-05-08 13:57:20 | INFO | ✅ Relevant-only annotation saved to /Users/tanmaybhuskute/Documents/gifdroid-reproduction/apps/adaway/llm/ViBR_gemini/screenrec/run-006/artifacts/srv-002/step_6_relevant_regions.png
2026-05-08 13:57:20 | INFO | /Users/tanmaybhuskute/Documents/gifdroid-reproduction/apps/adaway/llm/ViBR_gemini/screenrec/run-006/artifacts/srv-002/step_6_relevant_regions.png
2026-05-08 13:57:20 | INFO | /Users/tanmaybhuskute/Documents/gifdroid-reproduction/apps/adaway/llm/ViBR_gemini/screenrec/run-006/artifacts/srv-002/step_6_screenshot-0.png
2026-05-08 13:57:20 | INFO | Consistency Response from Gemini: ```json
2026-05-08 13:57:20 | INFO | {
2026-05-08 13:57:20 | INFO |   "same_state": "no",
2026-05-08 13:57:20 | INFO |   "description": "The 'Add host to whitelist' dialog is present in the reference image but is not visible in the current image. The current screen shows a list of items and a configuration change banner at the bottom."
2026-05-08 13:57:20 | INFO | }
2026-05-08 13:57:20 | INFO | ```
2026-05-08 13:57:20 | INFO | 🔄 Attempting to align state (try 1/3)...
2026-05-08 13:57:20 | INFO | /Users/tanmaybhuskute/Documents/gifdroid-reproduction/apps/adaway/llm/ViBR_gemini/screenrec/run-006/artifacts/srv-002/step_6_tmp_start.png
2026-05-08 13:57:20 | INFO | /Users/tanmaybhuskute/Documents/gifdroid-reproduction/apps/adaway/llm/ViBR_gemini/screenrec/run-006/artifacts/srv-002/step_6_tmp_stop.png
2026-05-08 13:57:20 | INFO | /Users/tanmaybhuskute/Documents/gifdroid-reproduction/apps/adaway/llm/ViBR_gemini/screenrec/run-006/artifacts/srv-002/step_6_labeled.png
2026-05-08 13:57:20 | INFO | Region Action Response from Gemini: ```json
2026-05-08 13:57:20 | INFO | {
2026-05-08 13:57:20 | INFO |     "action": "tap",
2026-05-08 13:57:20 | INFO |     "region": 4,
2026-05-08 13:57:20 | INFO |     "description": "Tap the APPLY button to apply the configuration change."
2026-05-08 13:57:20 | INFO | }
2026-05-08 13:57:20 | INFO | ```
2026-05-08 13:57:20 | INFO | 🎯 Recovery using region index: 4 at (540, 1034)
2026-05-08 13:57:20 | INFO | [1] Tap the APPLY button to apply the configuration change. -> tap
2026-05-08 13:57:20 | INFO | Taking screenshot: /sdcard/screenshot-0.png -> /Users/tanmaybhuskute/Documents/gifdroid-reproduction/apps/adaway/llm/ViBR_gemini/screenrec/run-006/artifacts/srv-002/step_6_screenshot-0.png
2026-05-08 13:57:20 | INFO | /Users/tanmaybhuskute/Documents/gifdroid-reproduction/apps/adaway/llm/ViBR_gemini/screenrec/run-006/artifacts/srv-002/step_6_tmp_start.png
2026-05-08 13:57:20 | INFO | /Users/tanmaybhuskute/Documents/gifdroid-reproduction/apps/adaway/llm/ViBR_gemini/screenrec/run-006/artifacts/srv-002/step_6_screenshot-0.png
2026-05-08 13:57:20 | INFO | Consistency Response from Gemini: ```json
2026-05-08 13:57:20 | INFO | {
2026-05-08 13:57:20 | INFO |   "same_state": "no",
2026-05-08 13:57:20 | INFO |   "description": "The reference image shows a dialog box titled 'Add host to whitelist' which is not present in the current image. The current image displays the main list view with a banner at the bottom."
2026-05-08 13:57:20 | INFO | }
2026-05-08 13:57:20 | INFO | ```
2026-05-08 13:57:20 | INFO | 🔄 Attempting to align state (try 2/3)...
2026-05-08 13:57:20 | INFO | /Users/tanmaybhuskute/Documents/gifdroid-reproduction/apps/adaway/llm/ViBR_gemini/screenrec/run-006/artifacts/srv-002/step_6_tmp_start.png
2026-05-08 13:57:20 | INFO | /Users/tanmaybhuskute/Documents/gifdroid-reproduction/apps/adaway/llm/ViBR_gemini/screenrec/run-006/artifacts/srv-002/step_6_tmp_stop.png
2026-05-08 13:57:20 | INFO | /Users/tanmaybhuskute/Documents/gifdroid-reproduction/apps/adaway/llm/ViBR_gemini/screenrec/run-006/artifacts/srv-002/step_6_labeled.png
2026-05-08 13:57:20 | INFO | Region Action Response from Gemini: ```json
2026-05-08 13:57:20 | INFO | {
2026-05-08 13:57:20 | INFO |   "action": "tap",
2026-05-08 13:57:20 | INFO |   "region": 7,
2026-05-08 13:57:20 | INFO |   "description": "Tap on the plus button to add a new host."
2026-05-08 13:57:20 | INFO | }
2026-05-08 13:57:20 | INFO | ```
2026-05-08 13:57:20 | INFO | 🎯 Recovery using region index: 7 at (884, 1170)
2026-05-08 13:57:20 | INFO | [1] Tap on the plus button to add a new host. -> tap
2026-05-08 13:57:20 | INFO | Taking screenshot: /sdcard/screenshot-0.png -> /Users/tanmaybhuskute/Documents/gifdroid-reproduction/apps/adaway/llm/ViBR_gemini/screenrec/run-006/artifacts/srv-002/step_6_screenshot-0.png
2026-05-08 13:57:20 | INFO | /Users/tanmaybhuskute/Documents/gifdroid-reproduction/apps/adaway/llm/ViBR_gemini/screenrec/run-006/artifacts/srv-002/step_6_tmp_start.png
2026-05-08 13:57:20 | INFO | /Users/tanmaybhuskute/Documents/gifdroid-reproduction/apps/adaway/llm/ViBR_gemini/screenrec/run-006/artifacts/srv-002/step_6_screenshot-0.png
2026-05-08 13:57:20 | INFO | Consistency Response from Gemini: ```json
2026-05-08 13:57:20 | INFO | {
2026-05-08 13:57:20 | INFO |   "same_state": "no",
2026-05-08 13:57:20 | INFO |   "description": "The 'Add host to whitelist' dialog is present in the reference image but is missing in the current image. The current image shows a list of items and a 'configuration changed' banner at the bottom."
2026-05-08 13:57:20 | INFO | }
2026-05-08 13:57:20 | INFO | ```
2026-05-08 13:57:20 | INFO | 🔄 Attempting to align state (try 3/3)...
2026-05-08 13:57:20 | INFO | /Users/tanmaybhuskute/Documents/gifdroid-reproduction/apps/adaway/llm/ViBR_gemini/screenrec/run-006/artifacts/srv-002/step_6_tmp_start.png
2026-05-08 13:58:02 | INFO | /Users/tanmaybhuskute/Documents/gifdroid-reproduction/apps/adaway/llm/ViBR_gemini/screenrec/run-006/artifacts/srv-002/step_6_tmp_stop.png
2026-05-08 13:58:02 | INFO | /Users/tanmaybhuskute/Documents/gifdroid-reproduction/apps/adaway/llm/ViBR_gemini/screenrec/run-006/artifacts/srv-002/step_6_labeled.png
2026-05-08 13:58:02 | INFO | Region Action Response from Gemini: ```json
2026-05-08 13:58:02 | INFO | {
2026-05-08 13:58:02 | INFO |   "action": "tap",
2026-05-08 13:58:02 | INFO |   "region": 5,
2026-05-08 13:58:02 | INFO |   "description": "Tap the APPLY button to confirm the configuration change."
2026-05-08 13:58:02 | INFO | }
2026-05-08 13:58:02 | INFO | ```
2026-05-08 13:58:02 | INFO | 🎯 Recovery using region index: 5 at (540, 1170)
2026-05-08 13:58:02 | INFO | [1] Tap the APPLY button to confirm the configuration change. -> tap
2026-05-08 13:58:02 | INFO | Taking screenshot: /sdcard/screenshot-0.png -> /Users/tanmaybhuskute/Documents/gifdroid-reproduction/apps/adaway/llm/ViBR_gemini/screenrec/run-006/artifacts/srv-002/step_6_screenshot-0.png
2026-05-08 13:58:02 | INFO | /Users/tanmaybhuskute/Documents/gifdroid-reproduction/apps/adaway/llm/ViBR_gemini/screenrec/run-006/artifacts/srv-002/step_6_tmp_start.png
2026-05-08 13:58:02 | INFO | /Users/tanmaybhuskute/Documents/gifdroid-reproduction/apps/adaway/llm/ViBR_gemini/screenrec/run-006/artifacts/srv-002/step_6_screenshot-0.png
2026-05-08 13:58:02 | INFO | Consistency Response from Gemini: ```json
2026-05-08 13:58:02 | INFO | {
2026-05-08 13:58:02 | INFO |   "same_state": "no",
2026-05-08 13:58:02 | INFO |   "description": "The 'Add host to whitelist' dialog is open in the reference image, but it is not present in the current image. Instead, the current image shows a list and a banner at the bottom."
2026-05-08 13:58:02 | INFO | }
2026-05-08 13:58:02 | INFO | ```
2026-05-08 13:58:02 | INFO | ⚠️ Skipping action: current GUI state does not match start state.
2026-05-08 13:58:02 | INFO | Mismatch reason: the 'add host to whitelist' dialog is open in the reference image, but it is not present in the current image. instead, the current image shows a list and a banner at the bottom.
2026-05-08 13:58:02 | INFO | 
2026-05-08 13:58:02 | INFO | 📂 Processing segment 7...
2026-05-08 13:58:02 | INFO | Taking screenshot: /sdcard/screenshot-0.png -> /Users/tanmaybhuskute/Documents/gifdroid-reproduction/apps/adaway/llm/ViBR_gemini/screenrec/run-006/artifacts/srv-002/step_7_screenshot-0.png
2026-05-08 13:58:02 | INFO | 🔍 Annotated DINO output saved to /Users/tanmaybhuskute/Documents/gifdroid-reproduction/apps/adaway/llm/ViBR_gemini/screenrec/run-006/artifacts/srv-002/step_7_dino.png
2026-05-08 13:58:02 | INFO | /Users/tanmaybhuskute/Documents/gifdroid-reproduction/apps/adaway/llm/ViBR_gemini/screenrec/run-006/artifacts/srv-002/step_7_dino.png
2026-05-08 13:58:02 | INFO | /Users/tanmaybhuskute/Documents/gifdroid-reproduction/apps/adaway/llm/ViBR_gemini/screenrec/run-006/artifacts/srv-002/step_7_tmp_stop.png
2026-05-08 13:58:02 | INFO | Relevant Region Response from Gemini: ```json
2026-05-08 13:58:02 | INFO | {
2026-05-08 13:58:02 | INFO |   "target_regions": [
2026-05-08 13:58:02 | INFO |     8
2026-05-08 13:58:02 | INFO |   ],
2026-05-08 13:58:02 | INFO |   "predicted_action": "tap"
2026-05-08 13:58:02 | INFO | }
2026-05-08 13:58:02 | INFO | ```
2026-05-08 13:58:02 | INFO | 🔍 Relevant regions: {'target_regions': [8], 'predicted_action': 'tap'}
2026-05-08 13:58:02 | INFO | 🧠 GPT selected regions: [8]
2026-05-08 13:58:02 | INFO | ✅ Relevant-only annotation saved to /Users/tanmaybhuskute/Documents/gifdroid-reproduction/apps/adaway/llm/ViBR_gemini/screenrec/run-006/artifacts/srv-002/step_7_relevant_regions.png
2026-05-08 13:58:02 | INFO | /Users/tanmaybhuskute/Documents/gifdroid-reproduction/apps/adaway/llm/ViBR_gemini/screenrec/run-006/artifacts/srv-002/step_7_relevant_regions.png
2026-05-08 13:58:02 | INFO | /Users/tanmaybhuskute/Documents/gifdroid-reproduction/apps/adaway/llm/ViBR_gemini/screenrec/run-006/artifacts/srv-002/step_7_screenshot-0.png
2026-05-08 13:58:02 | INFO | Consistency Response from Gemini: ```json
2026-05-08 13:58:02 | INFO | {
2026-05-08 13:58:02 | INFO |   "same_state": "yes"
2026-05-08 13:58:02 | INFO | }
2026-05-08 13:58:02 | INFO | ```
2026-05-08 13:58:02 | INFO | /Users/tanmaybhuskute/Documents/gifdroid-reproduction/apps/adaway/llm/ViBR_gemini/screenrec/run-006/artifacts/srv-002/step_7_relevant_regions.png
2026-05-08 13:58:02 | INFO | /Users/tanmaybhuskute/Documents/gifdroid-reproduction/apps/adaway/llm/ViBR_gemini/screenrec/run-006/artifacts/srv-002/step_7_tmp_stop.png
2026-05-08 13:58:02 | INFO | /Users/tanmaybhuskute/Documents/gifdroid-reproduction/apps/adaway/llm/ViBR_gemini/screenrec/run-006/artifacts/srv-002/step_7_labeled.png
2026-05-08 13:58:02 | INFO | Region Action Response from Gemini: ```json
2026-05-08 13:58:02 | INFO | {
2026-05-08 13:58:02 | INFO |   "action": "tap",
2026-05-08 13:58:02 | INFO |   "region": 7,
2026-05-08 13:58:02 | INFO |   "description": "Tap on APPLY to apply the configuration change."
2026-05-08 13:58:02 | INFO | }
2026-05-08 13:58:02 | INFO | ```
2026-05-08 13:58:02 | INFO | 🎯 Using region index: 7 at (884, 1170)
2026-05-08 13:58:02 | INFO | [1] Tap on APPLY to apply the configuration change. -> tap
2026-05-08 13:58:02 | INFO | ✅ Action executed.
2026-05-08 13:58:02 | INFO | 
2026-05-08 13:58:02 | INFO | 
2026-05-08 13:58:02 | INFO | 📂 Processing segment 8...
2026-05-08 13:58:02 | INFO | Taking screenshot: /sdcard/screenshot-0.png -> /Users/tanmaybhuskute/Documents/gifdroid-reproduction/apps/adaway/llm/ViBR_gemini/screenrec/run-006/artifacts/srv-002/step_8_screenshot-0.png
2026-05-08 13:58:02 | INFO | 🔍 Annotated DINO output saved to /Users/tanmaybhuskute/Documents/gifdroid-reproduction/apps/adaway/llm/ViBR_gemini/screenrec/run-006/artifacts/srv-002/step_8_dino.png
2026-05-08 13:58:02 | INFO | /Users/tanmaybhuskute/Documents/gifdroid-reproduction/apps/adaway/llm/ViBR_gemini/screenrec/run-006/artifacts/srv-002/step_8_dino.png
2026-05-08 13:58:02 | INFO | /Users/tanmaybhuskute/Documents/gifdroid-reproduction/apps/adaway/llm/ViBR_gemini/screenrec/run-006/artifacts/srv-002/step_8_tmp_stop.png
2026-05-08 13:58:02 | INFO | Relevant Region Response from Gemini: ```json
2026-05-08 13:58:02 | INFO | {
2026-05-08 13:58:02 | INFO |   "target_regions": [
2026-05-08 13:58:02 | INFO |     1
2026-05-08 13:58:02 | INFO |   ],
2026-05-08 13:58:02 | INFO |   "predicted_action": "back"
2026-05-08 13:58:02 | INFO | }
2026-05-08 13:58:02 | INFO | ```
2026-05-08 13:58:02 | INFO | 🔍 Relevant regions: {'target_regions': [1], 'predicted_action': 'back'}
2026-05-08 13:58:02 | INFO | 🧠 GPT selected regions: [1]
2026-05-08 13:58:02 | INFO | ✅ Relevant-only annotation saved to /Users/tanmaybhuskute/Documents/gifdroid-reproduction/apps/adaway/llm/ViBR_gemini/screenrec/run-006/artifacts/srv-002/step_8_relevant_regions.png
2026-05-08 13:58:02 | INFO | /Users/tanmaybhuskute/Documents/gifdroid-reproduction/apps/adaway/llm/ViBR_gemini/screenrec/run-006/artifacts/srv-002/step_8_relevant_regions.png
2026-05-08 13:58:02 | INFO | /Users/tanmaybhuskute/Documents/gifdroid-reproduction/apps/adaway/llm/ViBR_gemini/screenrec/run-006/artifacts/srv-002/step_8_screenshot-0.png
2026-05-08 13:58:02 | INFO | Consistency Response from Gemini: ```json
2026-05-08 13:58:02 | INFO | {
2026-05-08 13:58:02 | INFO |   "same_state": "no",
2026-05-08 13:58:02 | INFO |   "description": "The top-left icon has changed from a menu icon in the reference image to a back arrow in the current image. Additionally, the current screen has a banner at the bottom that says 'Your configuration changed. You need to apply it.' with an 'APPLY' button, which is not present in the reference screen."
2026-05-08 13:58:02 | INFO | }
2026-05-08 13:58:02 | INFO | ```
2026-05-08 13:58:02 | INFO | 🔄 Attempting to align state (try 1/3)...
2026-05-08 13:58:02 | INFO | /Users/tanmaybhuskute/Documents/gifdroid-reproduction/apps/adaway/llm/ViBR_gemini/screenrec/run-006/artifacts/srv-002/step_8_tmp_start.png
2026-05-08 13:58:02 | INFO | /Users/tanmaybhuskute/Documents/gifdroid-reproduction/apps/adaway/llm/ViBR_gemini/screenrec/run-006/artifacts/srv-002/step_8_tmp_stop.png
2026-05-08 13:58:02 | INFO | /Users/tanmaybhuskute/Documents/gifdroid-reproduction/apps/adaway/llm/ViBR_gemini/screenrec/run-006/artifacts/srv-002/step_8_labeled.png
2026-05-08 13:58:02 | INFO | Region Action Response from Gemini: ```json
2026-05-08 13:58:02 | INFO | {
2026-05-08 13:58:02 | INFO |   "action": "back",
2026-05-08 13:58:02 | INFO |   "description": "Go back to the main screen."
2026-05-08 13:58:02 | INFO | }
2026-05-08 13:58:02 | INFO | ```
2026-05-08 13:58:02 | INFO | [1] Go back to the main screen. -> back
2026-05-08 13:58:02 | INFO | Taking screenshot: /sdcard/screenshot-0.png -> /Users/tanmaybhuskute/Documents/gifdroid-reproduction/apps/adaway/llm/ViBR_gemini/screenrec/run-006/artifacts/srv-002/step_8_screenshot-0.png
2026-05-08 13:58:02 | INFO | /Users/tanmaybhuskute/Documents/gifdroid-reproduction/apps/adaway/llm/ViBR_gemini/screenrec/run-006/artifacts/srv-002/step_8_tmp_start.png
2026-05-08 13:58:02 | INFO | /Users/tanmaybhuskute/Documents/gifdroid-reproduction/apps/adaway/llm/ViBR_gemini/screenrec/run-006/artifacts/srv-002/step_8_screenshot-0.png
2026-05-08 13:58:02 | INFO | Consistency Response from Gemini: ```json
2026-05-08 13:58:02 | INFO | {
2026-05-08 13:58:02 | INFO |   "same_state": "no",
2026-05-08 13:58:02 | INFO |   "description": "The two screens are completely different. The reference screen shows a list of allowed domains under \"Your lists\", while the current screen is the main dashboard of the app, showing statistics and general options. The user cannot perform the same actions on both screens."
2026-05-08 13:58:02 | INFO | }
2026-05-08 13:58:02 | INFO | ```
2026-05-08 13:58:02 | INFO | 🔄 Attempting to align state (try 2/3)...
2026-05-08 13:58:02 | INFO | /Users/tanmaybhuskute/Documents/gifdroid-reproduction/apps/adaway/llm/ViBR_gemini/screenrec/run-006/artifacts/srv-002/step_8_tmp_start.png
2026-05-08 13:58:02 | INFO | /Users/tanmaybhuskute/Documents/gifdroid-reproduction/apps/adaway/llm/ViBR_gemini/screenrec/run-006/artifacts/srv-002/step_8_tmp_stop.png
2026-05-08 13:58:02 | INFO | /Users/tanmaybhuskute/Documents/gifdroid-reproduction/apps/adaway/llm/ViBR_gemini/screenrec/run-006/artifacts/srv-002/step_8_labeled.png
2026-05-08 13:58:02 | INFO | Region Action Response from Gemini: ```json
2026-05-08 13:58:02 | INFO | {
2026-05-08 13:58:02 | INFO |   "action": "back",
2026-05-08 13:58:02 | INFO |   "description": "Go back to previous screen."
2026-05-08 13:58:02 | INFO | }
2026-05-08 13:58:02 | INFO | ```
2026-05-08 13:58:02 | INFO | [1] Go back to previous screen. -> back
2026-05-08 13:58:02 | INFO | Taking screenshot: /sdcard/screenshot-0.png -> /Users/tanmaybhuskute/Documents/gifdroid-reproduction/apps/adaway/llm/ViBR_gemini/screenrec/run-006/artifacts/srv-002/step_8_screenshot-0.png
2026-05-08 13:58:02 | INFO | /Users/tanmaybhuskute/Documents/gifdroid-reproduction/apps/adaway/llm/ViBR_gemini/screenrec/run-006/artifacts/srv-002/step_8_tmp_start.png
2026-05-08 13:58:02 | INFO | /Users/tanmaybhuskute/Documents/gifdroid-reproduction/apps/adaway/llm/ViBR_gemini/screenrec/run-006/artifacts/srv-002/step_8_screenshot-0.png
2026-05-08 13:58:02 | INFO | Consistency Response from Gemini: ```json
2026-05-08 13:58:02 | INFO | {
2026-05-08 13:58:02 | INFO |   "same_state": "no",
2026-05-08 13:58:02 | INFO |   "description": "The current screen is the initial setup/welcome screen for the app, while the reference screen is the main interface showing a list of allowed items. The user cannot perform the same actions, such as managing lists or navigating between 'Blocked', 'Allowed', and 'Redirected' tabs."
2026-05-08 13:58:02 | INFO | }
2026-05-08 13:58:02 | INFO | ```
2026-05-08 13:58:02 | INFO | 🔄 Attempting to align state (try 3/3)...
2026-05-08 13:58:02 | INFO | /Users/tanmaybhuskute/Documents/gifdroid-reproduction/apps/adaway/llm/ViBR_gemini/screenrec/run-006/artifacts/srv-002/step_8_tmp_start.png
2026-05-08 13:58:02 | INFO | /Users/tanmaybhuskute/Documents/gifdroid-reproduction/apps/adaway/llm/ViBR_gemini/screenrec/run-006/artifacts/srv-002/step_8_tmp_stop.png
2026-05-08 13:58:02 | INFO | /Users/tanmaybhuskute/Documents/gifdroid-reproduction/apps/adaway/llm/ViBR_gemini/screenrec/run-006/artifacts/srv-002/step_8_labeled.png
2026-05-08 13:58:02 | INFO | Region Action Response from Gemini: ```json
2026-05-08 13:58:02 | INFO | {
2026-05-08 13:58:02 | INFO |   "action": "tap",
2026-05-08 13:58:02 | INFO |   "region": 7,
2026-05-08 13:58:02 | INFO |   "description": "Tap on VPN based ad blocking"
2026-05-08 13:58:02 | INFO | }
2026-05-08 13:58:02 | INFO | ```
2026-05-08 13:58:02 | INFO | 🎯 Recovery using region index: 7 at (884, 1170)
2026-05-08 13:58:02 | INFO | [1] Tap on VPN based ad blocking -> tap
2026-05-08 13:58:02 | INFO | Taking screenshot: /sdcard/screenshot-0.png -> /Users/tanmaybhuskute/Documents/gifdroid-reproduction/apps/adaway/llm/ViBR_gemini/screenrec/run-006/artifacts/srv-002/step_8_screenshot-0.png
2026-05-08 13:58:02 | INFO | /Users/tanmaybhuskute/Documents/gifdroid-reproduction/apps/adaway/llm/ViBR_gemini/screenrec/run-006/artifacts/srv-002/step_8_tmp_start.png
2026-05-08 13:58:02 | INFO | /Users/tanmaybhuskute/Documents/gifdroid-reproduction/apps/adaway/llm/ViBR_gemini/screenrec/run-006/artifacts/srv-002/step_8_screenshot-0.png
2026-05-08 13:58:02 | INFO | Consistency Response from Gemini: ```json
2026-05-08 13:58:02 | INFO | {
2026-05-08 13:58:02 | INFO |   "same_state": "no",
2026-05-08 13:58:02 | INFO |   "description": "The current screen is the initial setup/onboarding screen for the app, while the reference screen is the main interface for managing lists. The user cannot perform the same actions on both screens."
2026-05-08 13:58:02 | INFO | }
2026-05-08 13:58:02 | INFO | ```
2026-05-08 13:58:02 | INFO | ⚠️ Skipping action: current GUI state does not match start state.
2026-05-08 13:58:02 | INFO | Mismatch reason: the current screen is the initial setup/onboarding screen for the app, while the reference screen is the main interface for managing lists. the user cannot perform the same actions on both screens.
2026-05-08 13:58:02 | INFO | ✅ Video processing completed.
2026-05-08 13:58:02 | INFO | 📝 Summary saved to /Users/tanmaybhuskute/Documents/gifdroid-reproduction/apps/adaway/llm/ViBR_gemini/screenrec/run-006/artifacts/srv-002/memory.md
2026-05-08 13:58:04 | INFO | ========================================================================
RUN SUMMARY
  App         : adaway
  Video type  : screenrec
  Status      : success
  Scenes      : 9/9
  Actions     : unknown=9
  LLM calls   : action_inference=15  region_detection=9  state_comparison=18
  LLM latency : min=4.9s  max=89.1s  avg=15.1s  total=634.1s
  Tokens used : prompt=40,722  output=1,878  total=42,600
  Wall time   : 13m 59s
========================================================================

```
