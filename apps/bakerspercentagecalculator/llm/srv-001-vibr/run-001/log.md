# ViBR Run Log

**Status**: SUCCESS

## Full Log

```
2026-05-12 20:53:00 | INFO | === src_vibr.2026-05-13T00-53-00__run-002__pipeline__started ===
2026-05-12 20:53:00 | INFO | Starting ViBR run
2026-05-12 20:53:00 | INFO | App: bakerspercentagecalculator
2026-05-12 20:53:00 | INFO | Video: /Users/tanmaybhuskute/Documents/gifdroid-reproduction/apps/bakerspercentagecalculator/videos/srv-001.mp4
2026-05-12 20:53:00 | INFO | Algorithm: clip
2026-05-12 20:53:00 | INFO | LLM: gemini (gemini-2.5-pro)
2026-05-12 20:53:00 | INFO | Output: /Users/tanmaybhuskute/Documents/gifdroid-reproduction/apps/bakerspercentagecalculator/llm/ViBR_gemini/screenrec/run-002
2026-05-12 20:53:05 | INFO | FutureWarning: Importing from timm.models.layers is deprecated, please import via timm.layers
2026-05-12 20:53:05 | INFO | UserWarning: Failed to load custom C++ ops. Running on CPU mode Only!
2026-05-12 20:53:05 | INFO | UserWarning: torch.meshgrid: in an upcoming release, it will be required to pass the indexing argument. (Triggered internally at /Users/runner/work/pytorch/pytorch/pytorch/aten/src/ATen/native/TensorShape.cpp:4383.)
2026-05-12 20:53:06 | INFO | Warning: You are sending unauthenticated requests to the HF Hub. Please set a HF_TOKEN to enable higher rate limits and faster downloads.
2026-05-12 20:53:07 | INFO | final text_encoder_type: bert-base-uncased
2026-05-12 20:53:07 | INFO | 
2026-05-12 20:53:07 | INFO | Loading weights:   0%|          | 0/199 [00:00<?, ?it/s]
2026-05-12 20:53:07 | INFO | Loading weights: 100%|██████████| 199/199 [00:00<00:00, 8519.96it/s]
2026-05-12 20:53:07 | INFO | [1mBertModel LOAD REPORT[0m from: bert-base-uncased
2026-05-12 20:53:07 | INFO | Key                                        | Status     |  | 
2026-05-12 20:53:07 | INFO | -------------------------------------------+------------+--+-
2026-05-12 20:53:07 | INFO | cls.predictions.transform.dense.bias       | UNEXPECTED |  | 
2026-05-12 20:53:07 | INFO | cls.predictions.transform.dense.weight     | UNEXPECTED |  | 
2026-05-12 20:53:07 | INFO | cls.predictions.transform.LayerNorm.weight | UNEXPECTED |  | 
2026-05-12 20:53:07 | INFO | cls.seq_relationship.weight                | UNEXPECTED |  | 
2026-05-12 20:53:07 | INFO | cls.predictions.bias                       | UNEXPECTED |  | 
2026-05-12 20:53:07 | INFO | cls.predictions.transform.LayerNorm.bias   | UNEXPECTED |  | 
2026-05-12 20:53:07 | INFO | cls.seq_relationship.bias                  | UNEXPECTED |  | 
2026-05-12 20:53:07 | INFO | 
2026-05-12 20:53:07 | INFO | Notes:
2026-05-12 20:53:07 | INFO | - UNEXPECTED:	can be ignored when loading from different task/architecture; not ok if you expect identical arch.
2026-05-12 20:53:13 | INFO | 🔹 Starting video processing (algorithm=clip, llm=gemini, model=gemini-2.5-pro)...
2026-05-12 20:53:13 | INFO | Initializing ADB device controller...
2026-05-12 20:53:13 | INFO | 📱 Preparing device for app: bakerspercentagecalculator
2026-05-12 20:53:13 | INFO | 🏠 Going to home screen...
2026-05-12 20:53:13 | INFO | 🚀 Opening app 'bakerspercentagecalculator' with command: am start -n com.pep1lo.bakerspercentagecalculator/.MainActivity
2026-05-12 20:53:13 | INFO | ✅ App 'bakerspercentagecalculator' opened and ready
2026-05-12 20:53:13 | INFO | Taking screenshot: /sdcard/screenshot-0.png -> /Users/tanmaybhuskute/Documents/gifdroid-reproduction/apps/bakerspercentagecalculator/llm/ViBR_gemini/screenrec/run-002/artifacts/srv-001/screenshot-0.png
2026-05-12 20:53:13 | INFO | Reading frames from video...
2026-05-12 20:53:13 | INFO | Reading frame:  2
2026-05-12 20:53:13 | INFO | Reading frame:  3
2026-05-12 20:53:13 | INFO | Reading frame:  4
2026-05-12 20:53:13 | INFO | Reading frame:  5
2026-05-12 20:53:13 | INFO | Reading frame:  6
2026-05-12 20:53:13 | INFO | Reading frame:  7
2026-05-12 20:53:13 | INFO | Reading frame:  8
2026-05-12 20:53:13 | INFO | Reading frame:  9
2026-05-12 20:53:13 | INFO | Reading frame:  10
2026-05-12 20:53:13 | INFO | Reading frame:  11
2026-05-12 20:53:13 | INFO | Reading frame:  12
2026-05-12 20:53:13 | INFO | Reading frame:  13
2026-05-12 20:53:13 | INFO | Reading frame:  14
2026-05-12 20:53:13 | INFO | Reading frame:  15
2026-05-12 20:53:13 | INFO | Reading frame:  16
2026-05-12 20:53:13 | INFO | Reading frame:  17
2026-05-12 20:53:13 | INFO | Reading frame:  18
2026-05-12 20:53:13 | INFO | Reading frame:  19
2026-05-12 20:53:13 | INFO | Reading frame:  20
2026-05-12 20:53:13 | INFO | Reading frame:  21
2026-05-12 20:53:13 | INFO | Reading frame:  22
2026-05-12 20:53:13 | INFO | Reading frame:  23
2026-05-12 20:53:13 | INFO | Reading frame:  24
2026-05-12 20:53:13 | INFO | Reading frame:  25
2026-05-12 20:53:13 | INFO | Reading frame:  26
2026-05-12 20:53:13 | INFO | Reading frame:  27
2026-05-12 20:53:13 | INFO | Reading frame:  28
2026-05-12 20:53:13 | INFO | Reading frame:  29
2026-05-12 20:53:13 | INFO | Reading frame:  30
2026-05-12 20:53:13 | INFO | Reading frame:  31
2026-05-12 20:53:13 | INFO | Reading frame:  32
2026-05-12 20:53:13 | INFO | Reading frame:  33
2026-05-12 20:53:13 | INFO | Reading frame:  34
2026-05-12 20:53:13 | INFO | Reading frame:  35
2026-05-12 20:53:13 | INFO | Reading frame:  36
2026-05-12 20:53:13 | INFO | Reading frame:  37
2026-05-12 20:53:13 | INFO | Reading frame:  38
2026-05-12 20:53:13 | INFO | Reading frame:  39
2026-05-12 20:53:13 | INFO | Reading frame:  40
2026-05-12 20:53:13 | INFO | Reading frame:  41
2026-05-12 20:53:13 | INFO | Reading frame:  42
2026-05-12 20:53:13 | INFO | Reading frame:  43
2026-05-12 20:53:13 | INFO | Reading frame:  44
2026-05-12 20:53:13 | INFO | Reading frame:  45
2026-05-12 20:53:13 | INFO | Reading frame:  46
2026-05-12 20:53:13 | INFO | Reading frame:  47
2026-05-12 20:53:13 | INFO | Reading frame:  48
2026-05-12 20:53:13 | INFO | Reading frame:  49
2026-05-12 20:53:13 | INFO | Reading frame:  50
2026-05-12 20:53:13 | INFO | Reading frame:  51
2026-05-12 20:53:13 | INFO | Reading frame:  52
2026-05-12 20:53:13 | INFO | Reading frame:  53
2026-05-12 20:53:13 | INFO | Reading frame:  54
2026-05-12 20:53:13 | INFO | Reading frame:  55
2026-05-12 20:53:13 | INFO | Reading frame:  56
2026-05-12 20:53:13 | INFO | Reading frame:  57
2026-05-12 20:53:13 | INFO | Reading frame:  58
2026-05-12 20:53:13 | INFO | Reading frame:  59
2026-05-12 20:53:13 | INFO | Reading frame:  60
2026-05-12 20:53:13 | INFO | Reading frame:  61
2026-05-12 20:53:13 | INFO | Reading frame:  62
2026-05-12 20:53:13 | INFO | Reading frame:  63
2026-05-12 20:53:13 | INFO | Reading frame:  64
2026-05-12 20:53:13 | INFO | Reading frame:  65
2026-05-12 20:53:13 | INFO | Reading frame:  66
2026-05-12 20:53:13 | INFO | Reading frame:  67
2026-05-12 20:53:13 | INFO | Reading frame:  68
2026-05-12 20:53:13 | INFO | Reading frame:  69
2026-05-12 20:53:13 | INFO | Reading frame:  70
2026-05-12 20:53:13 | INFO | Reading frame:  71
2026-05-12 20:53:13 | INFO | Reading frame:  72
2026-05-12 20:53:13 | INFO | Reading frame:  73
2026-05-12 20:53:13 | INFO | Reading frame:  74
2026-05-12 20:53:13 | INFO | Reading frame:  75
2026-05-12 20:53:13 | INFO | Reading frame:  76
2026-05-12 20:53:13 | INFO | Reading frame:  77
2026-05-12 20:53:13 | INFO | Reading frame:  78
2026-05-12 20:53:13 | INFO | Reading frame:  79
2026-05-12 20:53:13 | INFO | Reading frame:  80
2026-05-12 20:53:13 | INFO | Reading frame:  81
2026-05-12 20:53:13 | INFO | Reading frame:  82
2026-05-12 20:53:13 | INFO | Reading frame:  83
2026-05-12 20:53:13 | INFO | Reading frame:  84
2026-05-12 20:53:13 | INFO | Reading frame:  85
2026-05-12 20:53:13 | INFO | Reading frame:  86
2026-05-12 20:53:13 | INFO | Reading frame:  87
2026-05-12 20:53:13 | INFO | Reading frame:  88
2026-05-12 20:53:13 | INFO | Reading frame:  89
2026-05-12 20:53:13 | INFO | Reading frame:  90
2026-05-12 20:53:13 | INFO | Reading frame:  91
2026-05-12 20:53:13 | INFO | Reading frame:  92
2026-05-12 20:53:13 | INFO | Reading frame:  93
2026-05-12 20:53:13 | INFO | Reading frame:  94
2026-05-12 20:53:13 | INFO | Reading frame:  95
2026-05-12 20:53:13 | INFO | Reading frame:  96
2026-05-12 20:53:13 | INFO | Reading frame:  97
2026-05-12 20:53:13 | INFO | Reading frame:  98
2026-05-12 20:53:13 | INFO | Reading frame:  99
2026-05-12 20:53:13 | INFO | Reading frame:  100
2026-05-12 20:53:13 | INFO | Reading frame:  101
2026-05-12 20:53:13 | INFO | Reading frame:  102
2026-05-12 20:53:13 | INFO | Reading frame:  103
2026-05-12 20:53:13 | INFO | Reading frame:  104
2026-05-12 20:53:13 | INFO | Reading frame:  105
2026-05-12 20:53:13 | INFO | Reading frame:  106
2026-05-12 20:53:13 | INFO | Reading frame:  107
2026-05-12 20:53:13 | INFO | Reading frame:  108
2026-05-12 20:53:13 | INFO | Reading frame:  109
2026-05-12 20:53:13 | INFO | Reading frame:  110
2026-05-12 20:53:13 | INFO | Reading frame:  111
2026-05-12 20:53:13 | INFO | Reading frame:  112
2026-05-12 20:53:13 | INFO | Reading frame:  113
2026-05-12 20:53:13 | INFO | Reading frame:  114
2026-05-12 20:53:13 | INFO | Reading frame:  115
2026-05-12 20:53:13 | INFO | Reading frame:  116
2026-05-12 20:53:13 | INFO | Reading frame:  117
2026-05-12 20:53:13 | INFO | Reading frame:  118
2026-05-12 20:53:13 | INFO | Reading frame:  119
2026-05-12 20:53:13 | INFO | Reading frame:  120
2026-05-12 20:53:13 | INFO | Reading frame:  121
2026-05-12 20:53:13 | INFO | Reading frame:  122
2026-05-12 20:53:13 | INFO | Reading frame:  123
2026-05-12 20:53:13 | INFO | Reading frame:  124
2026-05-12 20:53:13 | INFO | Reading frame:  125
2026-05-12 20:53:13 | INFO | Reading frame:  126
2026-05-12 20:53:13 | INFO | Reading frame:  127
2026-05-12 20:53:13 | INFO | Reading frame:  128
2026-05-12 20:53:13 | INFO | Reading frame:  129
2026-05-12 20:53:13 | INFO | Reading frame:  130
2026-05-12 20:53:13 | INFO | Reading frame:  131
2026-05-12 20:53:13 | INFO | Reading frame:  132
2026-05-12 20:53:13 | INFO | Reading frame:  133
2026-05-12 20:53:13 | INFO | Reading frame:  134
2026-05-12 20:53:13 | INFO | Reading frame:  135
2026-05-12 20:53:13 | INFO | Reading frame:  136
2026-05-12 20:53:13 | INFO | Reading frame:  137
2026-05-12 20:53:13 | INFO | Reading frame:  138
2026-05-12 20:53:13 | INFO | Reading frame:  139
2026-05-12 20:53:13 | INFO | Reading frame:  140
2026-05-12 20:53:13 | INFO | Reading frame:  141
2026-05-12 20:53:13 | INFO | Reading frame:  142
2026-05-12 20:53:13 | INFO | Reading frame:  143
2026-05-12 20:53:13 | INFO | Reading frame:  144
2026-05-12 20:53:13 | INFO | Reading frame:  145
2026-05-12 20:53:13 | INFO | Reading frame:  146
2026-05-12 20:53:13 | INFO | Reading frame:  147
2026-05-12 20:53:13 | INFO | Reading frame:  148
2026-05-12 20:53:13 | INFO | Reading frame:  149
2026-05-12 20:53:13 | INFO | Reading frame:  150
2026-05-12 20:53:13 | INFO | Reading frame:  151
2026-05-12 20:53:13 | INFO | Reading frame:  152
2026-05-12 20:53:13 | INFO | Reading frame:  153
2026-05-12 20:53:13 | INFO | Reading frame:  154
2026-05-12 20:53:13 | INFO | Reading frame:  155
2026-05-12 20:53:13 | INFO | Reading frame:  156
2026-05-12 20:53:13 | INFO | Reading frame:  157
2026-05-12 20:53:13 | INFO | Reading frame:  158
2026-05-12 20:53:13 | INFO | Reading frame:  159
2026-05-12 20:53:13 | INFO | Reading frame:  160
2026-05-12 20:53:13 | INFO | Reading frame:  161
2026-05-12 20:53:13 | INFO | Reading frame:  162
2026-05-12 20:53:13 | INFO | Reading frame:  163
2026-05-12 20:53:13 | INFO | Reading frame:  164
2026-05-12 20:53:13 | INFO | Reading frame:  165
2026-05-12 20:53:13 | INFO | Reading frame:  166
2026-05-12 20:53:13 | INFO | Reading frame:  167
2026-05-12 20:53:13 | INFO | Reading frame:  168
2026-05-12 20:53:13 | INFO | Reading frame:  169
2026-05-12 20:53:13 | INFO | Reading frame:  170
2026-05-12 20:53:13 | INFO | Reading frame:  171
2026-05-12 20:53:13 | INFO | Reading frame:  172
2026-05-12 20:53:13 | INFO | Reading frame:  173
2026-05-12 20:53:13 | INFO | Reading frame:  174
2026-05-12 20:53:13 | INFO | Reading frame:  175
2026-05-12 20:53:13 | INFO | Reading frame:  176
2026-05-12 20:53:13 | INFO | Reading frame:  177
2026-05-12 20:53:13 | INFO | Reading frame:  178
2026-05-12 20:53:13 | INFO | Reading frame:  179
2026-05-12 20:53:13 | INFO | Reading frame:  180
2026-05-12 20:53:13 | INFO | Reading frame:  181
2026-05-12 20:53:13 | INFO | Reading frame:  182
2026-05-12 20:53:13 | INFO | Reading frame:  183
2026-05-12 20:53:13 | INFO | Reading frame:  184
2026-05-12 20:53:13 | INFO | Reading frame:  185
2026-05-12 20:53:13 | INFO | Reading frame:  186
2026-05-12 20:53:13 | INFO | Reading frame:  187
2026-05-12 20:53:13 | INFO | Reading frame:  188
2026-05-12 20:53:13 | INFO | Reading frame:  189
2026-05-12 20:53:13 | INFO | Reading frame:  190
2026-05-12 20:53:13 | INFO | Reading frame:  191
2026-05-12 20:53:13 | INFO | Reading frame:  192
2026-05-12 20:53:13 | INFO | Reading frame:  193
2026-05-12 20:53:13 | INFO | Reading frame:  194
2026-05-12 20:53:13 | INFO | Reading frame:  195
2026-05-12 20:53:13 | INFO | Reading frame:  196
2026-05-12 20:53:13 | INFO | Reading frame:  197
2026-05-12 20:53:13 | INFO | Reading frame:  198
2026-05-12 20:53:13 | INFO | Reading frame:  199
2026-05-12 20:53:13 | INFO | Reading frame:  200
2026-05-12 20:53:13 | INFO | Reading frame:  201
2026-05-12 20:53:13 | INFO | Reading frame:  202
2026-05-12 20:53:13 | INFO | Reading frame:  203
2026-05-12 20:53:13 | INFO | Reading frame:  204
2026-05-12 20:53:13 | INFO | Reading frame:  205
2026-05-12 20:53:13 | INFO | Reading frame:  206
2026-05-12 20:53:13 | INFO | Reading frame:  207
2026-05-12 20:53:13 | INFO | Reading frame:  208
2026-05-12 20:53:13 | INFO | Reading frame:  209
2026-05-12 20:53:13 | INFO | Reading frame:  210
2026-05-12 20:53:13 | INFO | Reading frame:  211
2026-05-12 20:53:13 | INFO | Reading frame:  212
2026-05-12 20:53:13 | INFO | Reading frame:  213
2026-05-12 20:53:13 | INFO | Reading frame:  214
2026-05-12 20:53:13 | INFO | Reading frame:  215
2026-05-12 20:53:13 | INFO | Reading frame:  216
2026-05-12 20:53:13 | INFO | Reading frame:  217
2026-05-12 20:53:13 | INFO | Reading frame:  218
2026-05-12 20:53:13 | INFO | Reading frame:  219
2026-05-12 20:53:13 | INFO | Reading frame:  220
2026-05-12 20:53:13 | INFO | Reading frame:  221
2026-05-12 20:53:13 | INFO | Reading frame:  222
2026-05-12 20:53:13 | INFO | Reading frame:  223
2026-05-12 20:53:13 | INFO | Reading frame:  224
2026-05-12 20:53:13 | INFO | Reading frame:  225
2026-05-12 20:53:13 | INFO | Reading frame:  226
2026-05-12 20:53:13 | INFO | Reading frame:  227
2026-05-12 20:53:13 | INFO | Reading frame:  228
2026-05-12 20:53:13 | INFO | Reading frame:  229
2026-05-12 20:53:13 | INFO | Reading frame:  230
2026-05-12 20:53:13 | INFO | Reading frame:  231
2026-05-12 20:53:13 | INFO | Reading frame:  232
2026-05-12 20:53:13 | INFO | Reading frame:  233
2026-05-12 20:53:13 | INFO | Reading frame:  234
2026-05-12 20:53:13 | INFO | Reading frame:  235
2026-05-12 20:53:13 | INFO | Reading frame:  236
2026-05-12 20:53:13 | INFO | Reading frame:  237
2026-05-12 20:53:13 | INFO | Reading frame:  238
2026-05-12 20:53:13 | INFO | Reading frame:  239
2026-05-12 20:53:13 | INFO | Reading frame:  240
2026-05-12 20:53:13 | INFO | Reading frame:  241
2026-05-12 20:53:13 | INFO | Reading frame:  242
2026-05-12 20:53:13 | INFO | Reading frame:  243
2026-05-12 20:53:13 | INFO | Reading frame:  244
2026-05-12 20:53:13 | INFO | Reading frame:  245
2026-05-12 20:53:13 | INFO | Reading frame:  246
2026-05-12 20:53:13 | INFO | Reading frame:  247
2026-05-12 20:53:13 | INFO | Reading frame:  248
2026-05-12 20:53:13 | INFO | Reading frame:  249
2026-05-12 20:53:13 | INFO | Reading frame:  250
2026-05-12 20:53:13 | INFO | Reading frame:  251
2026-05-12 20:53:13 | INFO | Reading frame:  252
2026-05-12 20:53:13 | INFO | Reading frame:  253
2026-05-12 20:53:13 | INFO | Reading frame:  254
2026-05-12 20:53:13 | INFO | Reading frame:  255
2026-05-12 20:53:13 | INFO | Reading frame:  256
2026-05-12 20:53:13 | INFO | Reading frame:  257
2026-05-12 20:53:13 | INFO | Reading frame:  258
2026-05-12 20:53:13 | INFO | Reading frame:  259
2026-05-12 20:53:13 | INFO | Reading frame:  260
2026-05-12 20:53:13 | INFO | Reading frame:  261
2026-05-12 20:53:13 | INFO | Reading frame:  262
2026-05-12 20:53:13 | INFO | Reading frame:  263
2026-05-12 20:53:13 | INFO | Reading frame:  264
2026-05-12 20:53:13 | INFO | Reading frame:  265
2026-05-12 20:53:13 | INFO | Reading frame:  266
2026-05-12 20:53:13 | INFO | Reading frame:  267
2026-05-12 20:53:13 | INFO | Reading frame:  268
2026-05-12 20:53:13 | INFO | Reading frame:  269
2026-05-12 20:53:13 | INFO | Reading frame:  270
2026-05-12 20:53:13 | INFO | Reading frame:  271
2026-05-12 20:53:13 | INFO | Reading frame:  272
2026-05-12 20:53:13 | INFO | Reading frame:  273
2026-05-12 20:53:13 | INFO | Reading frame:  274
2026-05-12 20:53:13 | INFO | Reading frame:  275
2026-05-12 20:53:13 | INFO | Reading frame:  276
2026-05-12 20:53:13 | INFO | Reading frame:  277
2026-05-12 20:53:13 | INFO | Reading frame:  278
2026-05-12 20:53:13 | INFO | Reading frame:  279
2026-05-12 20:53:13 | INFO | Reading frame:  280
2026-05-12 20:53:13 | INFO | Reading frame:  281
2026-05-12 20:53:13 | INFO | Reading frame:  282
2026-05-12 20:53:13 | INFO | Reading frame:  283
2026-05-12 20:53:13 | INFO | Reading frame:  284
2026-05-12 20:53:13 | INFO | Reading frame:  285
2026-05-12 20:53:13 | INFO | Reading frame:  286
2026-05-12 20:53:13 | INFO | Reading frame:  287
2026-05-12 20:53:13 | INFO | Reading frame:  288
2026-05-12 20:53:13 | INFO | Reading frame:  289
2026-05-12 20:53:13 | INFO | Reading frame:  290
2026-05-12 20:53:13 | INFO | Reading frame:  291
2026-05-12 20:53:13 | INFO | Reading frame:  292
2026-05-12 20:53:13 | INFO | Reading frame:  293
2026-05-12 20:53:13 | INFO | Reading frame:  294
2026-05-12 20:53:13 | INFO | Reading frame:  295
2026-05-12 20:53:13 | INFO | Reading frame:  296
2026-05-12 20:53:13 | INFO | Reading frame:  297
2026-05-12 20:53:13 | INFO | Reading frame:  298
2026-05-12 20:53:13 | INFO | Reading frame:  299
2026-05-12 20:53:13 | INFO | Reading frame:  300
2026-05-12 20:53:13 | INFO | Reading frame:  301
2026-05-12 20:53:13 | INFO | Reading frame:  302
2026-05-12 20:53:13 | INFO | Reading frame:  303
2026-05-12 20:53:13 | INFO | Reading frame:  304
2026-05-12 20:53:13 | INFO | Reading frame:  305
2026-05-12 20:53:13 | INFO | Reading frame:  306
2026-05-12 20:53:13 | INFO | Reading frame:  307
2026-05-12 20:53:13 | INFO | Reading frame:  308
2026-05-12 20:53:13 | INFO | Reading frame:  309
2026-05-12 20:53:13 | INFO | Reading frame:  310
2026-05-12 20:53:13 | INFO | Reading frame:  311
2026-05-12 20:53:13 | INFO | Reading frame:  312
2026-05-12 20:53:13 | INFO | Reading frame:  313
2026-05-12 20:53:13 | INFO | Reading frame:  314
2026-05-12 20:53:13 | INFO | Reading frame:  315
2026-05-12 20:53:13 | INFO | Reading frame:  316
2026-05-12 20:53:13 | INFO | Reading frame:  317
2026-05-12 20:53:13 | INFO | Reading frame:  318
2026-05-12 20:53:13 | INFO | Reading frame:  319
2026-05-12 20:53:13 | INFO | Reading frame:  320
2026-05-12 20:53:13 | INFO | Reading frame:  321
2026-05-12 20:53:13 | INFO | Reading frame:  322
2026-05-12 20:53:13 | INFO | Reading frame:  323
2026-05-12 20:53:13 | INFO | Reading frame:  324
2026-05-12 20:53:13 | INFO | Reading frame:  325
2026-05-12 20:53:13 | INFO | Reading frame:  326
2026-05-12 20:53:13 | INFO | Reading frame:  327
2026-05-12 20:53:13 | INFO | Reading frame:  328
2026-05-12 20:53:13 | INFO | Reading frame:  329
2026-05-12 20:53:13 | INFO | Reading frame:  330
2026-05-12 20:53:13 | INFO | Reading frame:  331
2026-05-12 20:53:13 | INFO | Reading frame:  332
2026-05-12 20:53:13 | INFO | Reading frame:  333
2026-05-12 20:53:13 | INFO | Reading frame:  334
2026-05-12 20:53:13 | INFO | Reading frame:  335
2026-05-12 20:53:13 | INFO | Reading frame:  336
2026-05-12 20:53:13 | INFO | Reading frame:  337
2026-05-12 20:53:13 | INFO | Reading frame:  338
2026-05-12 20:53:13 | INFO | Reading frame:  339
2026-05-12 20:53:13 | INFO | Reading frame:  340
2026-05-12 20:53:13 | INFO | Reading frame:  341
2026-05-12 20:53:13 | INFO | Reading frame:  342
2026-05-12 20:53:13 | INFO | Reading frame:  343
2026-05-12 20:53:13 | INFO | Reading frame:  344
2026-05-12 20:53:13 | INFO | Reading frame:  345
2026-05-12 20:53:13 | INFO | Reading frame:  346
2026-05-12 20:53:13 | INFO | Reading frame:  347
2026-05-12 20:53:13 | INFO | Reading frame:  348
2026-05-12 20:53:13 | INFO | Reading frame:  349
2026-05-12 20:53:13 | INFO | Reading frame:  350
2026-05-12 20:53:13 | INFO | Reading frame:  351
2026-05-12 20:53:13 | INFO | Reading frame:  352
2026-05-12 20:53:13 | INFO | Reading frame:  353
2026-05-12 20:53:13 | INFO | Reading frame:  354
2026-05-12 20:53:13 | INFO | Reading frame:  355
2026-05-12 20:53:13 | INFO | Reading frame:  356
2026-05-12 20:53:13 | INFO | Reading frame:  357
2026-05-12 20:53:13 | INFO | Reading frame:  358
2026-05-12 20:53:13 | INFO | Reading frame:  359
2026-05-12 20:53:13 | INFO | Reading frame:  360
2026-05-12 20:53:13 | INFO | Reading frame:  361
2026-05-12 20:53:13 | INFO | Reading frame:  362
2026-05-12 20:53:13 | INFO | Reading frame:  363
2026-05-12 20:53:13 | INFO | Reading frame:  364
2026-05-12 20:53:13 | INFO | Reading frame:  365
2026-05-12 20:53:13 | INFO | Reading frame:  366
2026-05-12 20:53:13 | INFO | Reading frame:  367
2026-05-12 20:53:13 | INFO | Reading frame:  368
2026-05-12 20:53:13 | INFO | Reading frame:  369
2026-05-12 20:53:13 | INFO | Reading frame:  370
2026-05-12 20:53:13 | INFO | Reading frame:  371
2026-05-12 20:53:13 | INFO | Reading frame:  372
2026-05-12 20:53:13 | INFO | Reading frame:  373
2026-05-12 20:53:13 | INFO | Reading frame:  374
2026-05-12 20:53:13 | INFO | Reading frame:  375
2026-05-12 20:53:13 | INFO | Reading frame:  376
2026-05-12 20:53:13 | INFO | Reading frame:  377
2026-05-12 20:53:13 | INFO | Reading frame:  378
2026-05-12 20:53:13 | INFO | Reading frame:  379
2026-05-12 20:53:13 | INFO | Reading frame:  380
2026-05-12 20:53:13 | INFO | Reading frame:  381
2026-05-12 20:53:13 | INFO | Reading frame:  382
2026-05-12 20:53:13 | INFO | Reading frame:  383
2026-05-12 20:53:13 | INFO | Reading frame:  384
2026-05-12 20:53:13 | INFO | Reading frame:  385
2026-05-12 20:53:13 | INFO | Reading frame:  386
2026-05-12 20:53:13 | INFO | Reading frame:  387
2026-05-12 20:53:13 | INFO | Reading frame:  388
2026-05-12 20:53:13 | INFO | Reading frame:  389
2026-05-12 20:53:13 | INFO | Reading frame:  390
2026-05-12 20:53:13 | INFO | Reading frame:  391
2026-05-12 20:53:13 | INFO | Reading frame:  392
2026-05-12 20:53:13 | INFO | Reading frame:  393
2026-05-12 20:53:13 | INFO | Reading frame:  394
2026-05-12 20:53:13 | INFO | Reading frame:  395
2026-05-12 20:53:13 | INFO | Reading frame:  396
2026-05-12 20:53:13 | INFO | Reading frame:  397
2026-05-12 20:53:13 | INFO | Reading frame:  398
2026-05-12 20:53:13 | INFO | Reading frame:  399
2026-05-12 20:53:13 | INFO | Reading frame:  400
2026-05-12 20:53:13 | INFO | Reading frame:  401
2026-05-12 20:53:13 | INFO | Reading frame:  402
2026-05-12 20:53:13 | INFO | Reading frame:  403
2026-05-12 20:53:13 | INFO | Reading frame:  404
2026-05-12 20:53:13 | INFO | Reading frame:  405
2026-05-12 20:53:13 | INFO | Reading frame:  406
2026-05-12 20:53:13 | INFO | Reading frame:  407
2026-05-12 20:53:13 | INFO | Reading frame:  408
2026-05-12 20:53:13 | INFO | Reading frame:  409
2026-05-12 20:53:13 | INFO | Reading frame:  410
2026-05-12 20:53:13 | INFO | Reading frame:  411
2026-05-12 20:53:13 | INFO | Reading frame:  412
2026-05-12 20:53:13 | INFO | Reading frame:  413
2026-05-12 20:53:13 | INFO | Reading frame:  414
2026-05-12 20:53:13 | INFO | Reading frame:  415
2026-05-12 20:53:13 | INFO | Reading frame:  416
2026-05-12 20:53:13 | INFO | Reading frame:  417
2026-05-12 20:53:13 | INFO | Reading frame:  418
2026-05-12 20:53:13 | INFO | Reading frame:  419
2026-05-12 20:53:13 | INFO | Reading frame:  420
2026-05-12 20:53:13 | INFO | Reading frame:  421
2026-05-12 20:53:13 | INFO | Reading frame:  422
2026-05-12 20:53:13 | INFO | Reading frame:  423
2026-05-12 20:53:13 | INFO | Reading frame:  424
2026-05-12 20:53:13 | INFO | Reading frame:  425
2026-05-12 20:53:13 | INFO | Reading frame:  426
2026-05-12 20:53:13 | INFO | Reading frame:  427
2026-05-12 20:53:13 | INFO | Reading frame:  428
2026-05-12 20:53:13 | INFO | Reading frame:  429
2026-05-12 20:53:13 | INFO | Reading frame:  430
2026-05-12 20:53:13 | INFO | Reading frame:  431
2026-05-12 20:53:13 | INFO | Reading frame:  432
2026-05-12 20:53:13 | INFO | Reading frame:  433
2026-05-12 20:53:13 | INFO | Reading frame:  434
2026-05-12 20:53:13 | INFO | Reading frame:  435
2026-05-12 20:53:13 | INFO | Reading frame:  436
2026-05-12 20:53:13 | INFO | Reading frame:  437
2026-05-12 20:53:13 | INFO | Reading frame:  438
2026-05-12 20:53:13 | INFO | Reading frame:  439
2026-05-12 20:53:13 | INFO | Reading frame:  440
2026-05-12 20:53:13 | INFO | Reading frame:  441
2026-05-12 20:53:13 | INFO | Reading frame:  442
2026-05-12 20:53:13 | INFO | Reading frame:  443
2026-05-12 20:53:13 | INFO | Reading frame:  444
2026-05-12 20:53:13 | INFO | Reading frame:  445
2026-05-12 20:53:13 | INFO | Reading frame:  446
2026-05-12 20:53:13 | INFO | Reading frame:  447
2026-05-12 20:53:13 | INFO | Reading frame:  448
2026-05-12 20:53:13 | INFO | Reading frame:  449
2026-05-12 20:53:13 | INFO | Reading frame:  450
2026-05-12 20:53:13 | INFO | Reading frame:  451
2026-05-12 20:53:13 | INFO | Reading frame:  452
2026-05-12 20:53:13 | INFO | Reading frame:  453
2026-05-12 20:53:13 | INFO | Reading frame:  454
2026-05-12 20:53:13 | INFO | Reading frame:  455
2026-05-12 20:53:13 | INFO | Reading frame:  456
2026-05-12 20:53:13 | INFO | Reading frame:  457
2026-05-12 20:53:13 | INFO | Reading frame:  458
2026-05-12 20:53:13 | INFO | Reading frame:  459
2026-05-12 20:53:13 | INFO | Reading frame:  460
2026-05-12 20:53:13 | INFO | Reading frame:  461
2026-05-12 20:53:13 | INFO | Reading frame:  462
2026-05-12 20:53:13 | INFO | 🔍 Detecting stable segments...
2026-05-12 20:53:13 | INFO | 
2026-05-12 20:53:13 | INFO | Loading weights:   0%|          | 0/398 [00:00<?, ?it/s]
2026-05-12 20:53:13 | INFO | Loading weights: 100%|██████████| 398/398 [00:00<00:00, 29036.42it/s]
2026-05-12 20:53:13 | INFO | [1mCLIPModel LOAD REPORT[0m from: openai/clip-vit-base-patch32
2026-05-12 20:53:13 | INFO | Key                                  | Status     |  | 
2026-05-12 20:53:13 | INFO | -------------------------------------+------------+--+-
2026-05-12 20:53:13 | INFO | text_model.embeddings.position_ids   | UNEXPECTED |  | 
2026-05-12 20:53:13 | INFO | vision_model.embeddings.position_ids | UNEXPECTED |  | 
2026-05-12 20:53:13 | INFO | 
2026-05-12 20:53:13 | INFO | Notes:
2026-05-12 20:53:13 | INFO | - UNEXPECTED:	can be ignored when loading from different task/architecture; not ok if you expect identical arch.
2026-05-12 20:53:17 | INFO | `use_return_dict` is deprecated! Use `return_dict` instead!
2026-05-12 20:53:17 | INFO | UserWarning: torch.utils.checkpoint: the use_reentrant parameter should be passed explicitly. Starting in PyTorch 2.9, calling checkpoint without use_reentrant will raise an exception. use_reentrant=False is recommended, but if you need to preserve the current default behavior, you can pass use_reentrant=True. Refer to docs for more details on the differences between the two variants.
2026-05-12 20:53:17 | INFO | UserWarning: None of the inputs have requires_grad=True. Gradients will be None
2026-05-12 20:53:21 | INFO | FutureWarning: `torch.cuda.amp.autocast(args...)` is deprecated. Please use `torch.amp.autocast('cuda', args...)` instead.
2026-05-12 20:53:49 | INFO | UserWarning: torch.utils.checkpoint: the use_reentrant parameter should be passed explicitly. Starting in PyTorch 2.9, calling checkpoint without use_reentrant will raise an exception. use_reentrant=False is recommended, but if you need to preserve the current default behavior, you can pass use_reentrant=True. Refer to docs for more details on the differences between the two variants.
2026-05-12 20:53:49 | INFO | UserWarning: None of the inputs have requires_grad=True. Gradients will be None
2026-05-12 20:53:52 | INFO | FutureWarning: `torch.cuda.amp.autocast(args...)` is deprecated. Please use `torch.amp.autocast('cuda', args...)` instead.
2026-05-12 20:54:21 | INFO | UserWarning: torch.utils.checkpoint: the use_reentrant parameter should be passed explicitly. Starting in PyTorch 2.9, calling checkpoint without use_reentrant will raise an exception. use_reentrant=False is recommended, but if you need to preserve the current default behavior, you can pass use_reentrant=True. Refer to docs for more details on the differences between the two variants.
2026-05-12 20:54:21 | INFO | UserWarning: None of the inputs have requires_grad=True. Gradients will be None
2026-05-12 20:54:24 | INFO | FutureWarning: `torch.cuda.amp.autocast(args...)` is deprecated. Please use `torch.amp.autocast('cuda', args...)` instead.
2026-05-12 20:55:15 | INFO | UserWarning: torch.utils.checkpoint: the use_reentrant parameter should be passed explicitly. Starting in PyTorch 2.9, calling checkpoint without use_reentrant will raise an exception. use_reentrant=False is recommended, but if you need to preserve the current default behavior, you can pass use_reentrant=True. Refer to docs for more details on the differences between the two variants.
2026-05-12 20:55:15 | INFO | UserWarning: None of the inputs have requires_grad=True. Gradients will be None
2026-05-12 20:55:19 | INFO | FutureWarning: `torch.cuda.amp.autocast(args...)` is deprecated. Please use `torch.amp.autocast('cuda', args...)` instead.
2026-05-12 20:56:09 | INFO | UserWarning: torch.utils.checkpoint: the use_reentrant parameter should be passed explicitly. Starting in PyTorch 2.9, calling checkpoint without use_reentrant will raise an exception. use_reentrant=False is recommended, but if you need to preserve the current default behavior, you can pass use_reentrant=True. Refer to docs for more details on the differences between the two variants.
2026-05-12 20:56:09 | INFO | UserWarning: None of the inputs have requires_grad=True. Gradients will be None
2026-05-12 20:56:13 | INFO | FutureWarning: `torch.cuda.amp.autocast(args...)` is deprecated. Please use `torch.amp.autocast('cuda', args...)` instead.
2026-05-12 20:56:53 | INFO | UserWarning: torch.utils.checkpoint: the use_reentrant parameter should be passed explicitly. Starting in PyTorch 2.9, calling checkpoint without use_reentrant will raise an exception. use_reentrant=False is recommended, but if you need to preserve the current default behavior, you can pass use_reentrant=True. Refer to docs for more details on the differences between the two variants.
2026-05-12 20:56:53 | INFO | UserWarning: None of the inputs have requires_grad=True. Gradients will be None
2026-05-12 20:56:56 | INFO | FutureWarning: `torch.cuda.amp.autocast(args...)` is deprecated. Please use `torch.amp.autocast('cuda', args...)` instead.
2026-05-12 20:57:39 | INFO | UserWarning: torch.utils.checkpoint: the use_reentrant parameter should be passed explicitly. Starting in PyTorch 2.9, calling checkpoint without use_reentrant will raise an exception. use_reentrant=False is recommended, but if you need to preserve the current default behavior, you can pass use_reentrant=True. Refer to docs for more details on the differences between the two variants.
2026-05-12 20:57:39 | INFO | UserWarning: None of the inputs have requires_grad=True. Gradients will be None
2026-05-12 20:57:44 | INFO | FutureWarning: `torch.cuda.amp.autocast(args...)` is deprecated. Please use `torch.amp.autocast('cuda', args...)` instead.
2026-05-12 20:57:54 | INFO | ✅ CLIP similarity list loaded from cache.
2026-05-12 20:57:54 | INFO | 
2026-05-12 20:57:54 | INFO | 📂 Processing segment 0...
2026-05-12 20:57:54 | INFO | Taking screenshot: /sdcard/screenshot-0.png -> /Users/tanmaybhuskute/Documents/gifdroid-reproduction/apps/bakerspercentagecalculator/llm/ViBR_gemini/screenrec/run-002/artifacts/srv-001/step_0_screenshot-0.png
2026-05-12 20:57:54 | INFO | 🔍 Annotated DINO output saved to /Users/tanmaybhuskute/Documents/gifdroid-reproduction/apps/bakerspercentagecalculator/llm/ViBR_gemini/screenrec/run-002/artifacts/srv-001/step_0_dino.png
2026-05-12 20:57:54 | INFO | /Users/tanmaybhuskute/Documents/gifdroid-reproduction/apps/bakerspercentagecalculator/llm/ViBR_gemini/screenrec/run-002/artifacts/srv-001/step_0_dino.png
2026-05-12 20:57:54 | INFO | /Users/tanmaybhuskute/Documents/gifdroid-reproduction/apps/bakerspercentagecalculator/llm/ViBR_gemini/screenrec/run-002/artifacts/srv-001/step_0_tmp_stop.png
2026-05-12 20:57:54 | INFO | Relevant Region Response from Gemini: ```json
2026-05-12 20:57:54 | INFO | {
2026-05-12 20:57:54 | INFO |   "target_regions": [],
2026-05-12 20:57:54 | INFO |   "predicted_action": "no action"
2026-05-12 20:57:54 | INFO | }
2026-05-12 20:57:54 | INFO | ```
2026-05-12 20:57:54 | INFO | 🔍 Relevant regions: {'target_regions': [], 'predicted_action': 'no action'}
2026-05-12 20:57:54 | INFO | 🧠 GPT selected regions: []
2026-05-12 20:57:54 | INFO | ⚠️ No relevant regions to annotate.
2026-05-12 20:57:54 | INFO | /Users/tanmaybhuskute/Documents/gifdroid-reproduction/apps/bakerspercentagecalculator/llm/ViBR_gemini/screenrec/run-002/artifacts/srv-001/step_0_relevant_regions.png
2026-05-12 20:57:54 | INFO | /Users/tanmaybhuskute/Documents/gifdroid-reproduction/apps/bakerspercentagecalculator/llm/ViBR_gemini/screenrec/run-002/artifacts/srv-001/step_0_screenshot-0.png
2026-05-12 20:57:54 | INFO | Consistency Response from Gemini: ```json
2026-05-12 20:57:54 | INFO | {
2026-05-12 20:57:54 | INFO |   "same_state": "yes"
2026-05-12 20:57:54 | INFO | }
2026-05-12 20:57:54 | INFO | ```
2026-05-12 20:57:54 | INFO | /Users/tanmaybhuskute/Documents/gifdroid-reproduction/apps/bakerspercentagecalculator/llm/ViBR_gemini/screenrec/run-002/artifacts/srv-001/step_0_relevant_regions.png
2026-05-12 20:57:54 | INFO | /Users/tanmaybhuskute/Documents/gifdroid-reproduction/apps/bakerspercentagecalculator/llm/ViBR_gemini/screenrec/run-002/artifacts/srv-001/step_0_tmp_stop.png
2026-05-12 20:57:54 | INFO | /Users/tanmaybhuskute/Documents/gifdroid-reproduction/apps/bakerspercentagecalculator/llm/ViBR_gemini/screenrec/run-002/artifacts/srv-001/step_0_labeled.png
2026-05-12 20:57:54 | INFO | Region Action Response from Gemini: ```json
2026-05-12 20:57:54 | INFO | {
2026-05-12 20:57:54 | INFO |     "action": "no action",
2026-05-12 20:57:54 | INFO |     "description": "No Action needed."
2026-05-12 20:57:54 | INFO | }
2026-05-12 20:57:54 | INFO | ```
2026-05-12 20:57:54 | INFO | ⚠️ No valid region or element match. Proceeding without position.
2026-05-12 20:57:54 | INFO | [1] No Action needed. -> no action
2026-05-12 20:57:54 | INFO | ✅ Action executed.
2026-05-12 20:57:54 | INFO | 
2026-05-12 20:57:54 | INFO | 
2026-05-12 20:57:54 | INFO | 📂 Processing segment 1...
2026-05-12 20:57:54 | INFO | Taking screenshot: /sdcard/screenshot-0.png -> /Users/tanmaybhuskute/Documents/gifdroid-reproduction/apps/bakerspercentagecalculator/llm/ViBR_gemini/screenrec/run-002/artifacts/srv-001/step_1_screenshot-0.png
2026-05-12 20:57:54 | INFO | 🔍 Annotated DINO output saved to /Users/tanmaybhuskute/Documents/gifdroid-reproduction/apps/bakerspercentagecalculator/llm/ViBR_gemini/screenrec/run-002/artifacts/srv-001/step_1_dino.png
2026-05-12 20:57:54 | INFO | /Users/tanmaybhuskute/Documents/gifdroid-reproduction/apps/bakerspercentagecalculator/llm/ViBR_gemini/screenrec/run-002/artifacts/srv-001/step_1_dino.png
2026-05-12 20:57:54 | INFO | /Users/tanmaybhuskute/Documents/gifdroid-reproduction/apps/bakerspercentagecalculator/llm/ViBR_gemini/screenrec/run-002/artifacts/srv-001/step_1_tmp_stop.png
2026-05-12 20:57:54 | INFO | Relevant Region Response from Gemini: ```json
2026-05-12 20:57:54 | INFO | {
2026-05-12 20:57:54 | INFO |   "target_regions": [],
2026-05-12 20:57:54 | INFO |   "predicted_action": "no action"
2026-05-12 20:57:54 | INFO | }
2026-05-12 20:57:54 | INFO | ```
2026-05-12 20:57:54 | INFO | 🔍 Relevant regions: {'target_regions': [], 'predicted_action': 'no action'}
2026-05-12 20:57:54 | INFO | 🧠 GPT selected regions: []
2026-05-12 20:57:54 | INFO | ⚠️ No relevant regions to annotate.
2026-05-12 20:57:54 | INFO | /Users/tanmaybhuskute/Documents/gifdroid-reproduction/apps/bakerspercentagecalculator/llm/ViBR_gemini/screenrec/run-002/artifacts/srv-001/step_1_relevant_regions.png
2026-05-12 20:57:54 | INFO | /Users/tanmaybhuskute/Documents/gifdroid-reproduction/apps/bakerspercentagecalculator/llm/ViBR_gemini/screenrec/run-002/artifacts/srv-001/step_1_screenshot-0.png
2026-05-12 20:57:54 | INFO | Consistency Response from Gemini: ```json
2026-05-12 20:57:54 | INFO | {
2026-05-12 20:57:54 | INFO |   "same_state": "yes"
2026-05-12 20:57:54 | INFO | }
2026-05-12 20:57:54 | INFO | ```
2026-05-12 20:57:54 | INFO | /Users/tanmaybhuskute/Documents/gifdroid-reproduction/apps/bakerspercentagecalculator/llm/ViBR_gemini/screenrec/run-002/artifacts/srv-001/step_1_relevant_regions.png
2026-05-12 20:57:54 | INFO | /Users/tanmaybhuskute/Documents/gifdroid-reproduction/apps/bakerspercentagecalculator/llm/ViBR_gemini/screenrec/run-002/artifacts/srv-001/step_1_tmp_stop.png
2026-05-12 20:57:54 | INFO | /Users/tanmaybhuskute/Documents/gifdroid-reproduction/apps/bakerspercentagecalculator/llm/ViBR_gemini/screenrec/run-002/artifacts/srv-001/step_1_labeled.png
2026-05-12 20:57:54 | INFO | Region Action Response from Gemini: ```json
2026-05-12 20:57:54 | INFO | {
2026-05-12 20:57:54 | INFO |   "action": "no action",
2026-05-12 20:57:54 | INFO |   "description": "No Action needed."
2026-05-12 20:57:54 | INFO | }
2026-05-12 20:57:54 | INFO | ```
2026-05-12 20:57:54 | INFO | ⚠️ No valid region or element match. Proceeding without position.
2026-05-12 20:57:54 | INFO | [1] No Action needed. -> no action
2026-05-12 20:57:54 | INFO | ✅ Action executed.
2026-05-12 20:57:54 | INFO | 
2026-05-12 20:57:54 | INFO | 
2026-05-12 20:57:54 | INFO | 📂 Processing segment 2...
2026-05-12 20:57:54 | INFO | Taking screenshot: /sdcard/screenshot-0.png -> /Users/tanmaybhuskute/Documents/gifdroid-reproduction/apps/bakerspercentagecalculator/llm/ViBR_gemini/screenrec/run-002/artifacts/srv-001/step_2_screenshot-0.png
2026-05-12 20:57:54 | INFO | 🔍 Annotated DINO output saved to /Users/tanmaybhuskute/Documents/gifdroid-reproduction/apps/bakerspercentagecalculator/llm/ViBR_gemini/screenrec/run-002/artifacts/srv-001/step_2_dino.png
2026-05-12 20:57:54 | INFO | /Users/tanmaybhuskute/Documents/gifdroid-reproduction/apps/bakerspercentagecalculator/llm/ViBR_gemini/screenrec/run-002/artifacts/srv-001/step_2_dino.png
2026-05-12 20:57:54 | INFO | /Users/tanmaybhuskute/Documents/gifdroid-reproduction/apps/bakerspercentagecalculator/llm/ViBR_gemini/screenrec/run-002/artifacts/srv-001/step_2_tmp_stop.png
2026-05-12 20:57:54 | INFO | Relevant Region Response from Gemini: ```json
2026-05-12 20:57:54 | INFO | {
2026-05-12 20:57:54 | INFO |   "target_regions": [
2026-05-12 20:57:54 | INFO |     17
2026-05-12 20:57:54 | INFO |   ],
2026-05-12 20:57:54 | INFO |   "predicted_action": "input_text"
2026-05-12 20:57:54 | INFO | }
2026-05-12 20:57:54 | INFO | ```
2026-05-12 20:57:54 | INFO | 🔍 Relevant regions: {'target_regions': [17], 'predicted_action': 'input_text'}
2026-05-12 20:57:54 | INFO | 🧠 GPT selected regions: [17]
2026-05-12 20:57:54 | INFO | ✅ Relevant-only annotation saved to /Users/tanmaybhuskute/Documents/gifdroid-reproduction/apps/bakerspercentagecalculator/llm/ViBR_gemini/screenrec/run-002/artifacts/srv-001/step_2_relevant_regions.png
2026-05-12 20:57:54 | INFO | /Users/tanmaybhuskute/Documents/gifdroid-reproduction/apps/bakerspercentagecalculator/llm/ViBR_gemini/screenrec/run-002/artifacts/srv-001/step_2_relevant_regions.png
2026-05-12 20:57:54 | INFO | /Users/tanmaybhuskute/Documents/gifdroid-reproduction/apps/bakerspercentagecalculator/llm/ViBR_gemini/screenrec/run-002/artifacts/srv-001/step_2_screenshot-0.png
2026-05-12 20:57:54 | INFO | Consistency Response from Gemini: ```json
2026-05-12 20:57:54 | INFO | {
2026-05-12 20:57:54 | INFO |   "same_state": "no",
2026-05-12 20:57:54 | INFO |   "description": "The reference screen is a form for creating a new recipe with multiple input fields. The current screen is the main screen of the app, which is empty and prompts the user to press the '+' button to add a recipe. The input fields required for the action are not present on the current screen."
2026-05-12 20:57:54 | INFO | }
2026-05-12 20:57:54 | INFO | ```
2026-05-12 20:57:54 | INFO | 🔄 Attempting to align state (try 1/3)...
2026-05-12 20:57:54 | INFO | /Users/tanmaybhuskute/Documents/gifdroid-reproduction/apps/bakerspercentagecalculator/llm/ViBR_gemini/screenrec/run-002/artifacts/srv-001/step_2_tmp_start.png
2026-05-12 20:57:54 | INFO | /Users/tanmaybhuskute/Documents/gifdroid-reproduction/apps/bakerspercentagecalculator/llm/ViBR_gemini/screenrec/run-002/artifacts/srv-001/step_2_tmp_stop.png
2026-05-12 20:57:54 | INFO | /Users/tanmaybhuskute/Documents/gifdroid-reproduction/apps/bakerspercentagecalculator/llm/ViBR_gemini/screenrec/run-002/artifacts/srv-001/step_2_labeled.png
2026-05-12 20:57:54 | INFO | Region Action Response from Gemini: ```json
2026-05-12 20:57:54 | INFO | {
2026-05-12 20:57:54 | INFO |   "action": "tap",
2026-05-12 20:57:54 | INFO |   "region": 3,
2026-05-12 20:57:54 | INFO |   "description": "Tap the plus button to add a new recipe."
2026-05-12 20:57:54 | INFO | }
2026-05-12 20:57:54 | INFO | ```
2026-05-12 20:57:54 | INFO | 🎯 Recovery using region index: 3 at (964, 1741)
2026-05-12 20:57:54 | INFO | [1] Tap the plus button to add a new recipe. -> tap
2026-05-12 20:57:54 | INFO | Taking screenshot: /sdcard/screenshot-0.png -> /Users/tanmaybhuskute/Documents/gifdroid-reproduction/apps/bakerspercentagecalculator/llm/ViBR_gemini/screenrec/run-002/artifacts/srv-001/step_2_screenshot-0.png
2026-05-12 20:57:54 | INFO | /Users/tanmaybhuskute/Documents/gifdroid-reproduction/apps/bakerspercentagecalculator/llm/ViBR_gemini/screenrec/run-002/artifacts/srv-001/step_2_tmp_stop.png
2026-05-12 20:57:54 | INFO | /Users/tanmaybhuskute/Documents/gifdroid-reproduction/apps/bakerspercentagecalculator/llm/ViBR_gemini/screenrec/run-002/artifacts/srv-001/step_2_screenshot-0.png
2026-05-12 20:57:54 | INFO | Consistency Response from Gemini: ```json
2026-05-12 20:57:54 | INFO | {
2026-05-12 20:57:54 | INFO |   "same_state": "yes"
2026-05-12 20:57:54 | INFO | }
2026-05-12 20:57:54 | INFO | ```
2026-05-12 20:57:54 | INFO | /Users/tanmaybhuskute/Documents/gifdroid-reproduction/apps/bakerspercentagecalculator/llm/ViBR_gemini/screenrec/run-002/artifacts/srv-001/step_2_relevant_regions.png
2026-05-12 20:57:54 | INFO | /Users/tanmaybhuskute/Documents/gifdroid-reproduction/apps/bakerspercentagecalculator/llm/ViBR_gemini/screenrec/run-002/artifacts/srv-001/step_2_tmp_stop.png
2026-05-12 20:57:54 | INFO | /Users/tanmaybhuskute/Documents/gifdroid-reproduction/apps/bakerspercentagecalculator/llm/ViBR_gemini/screenrec/run-002/artifacts/srv-001/step_2_labeled.png
2026-05-12 20:57:54 | INFO | Region Action Response from Gemini: ```json
2026-05-12 20:57:54 | INFO | {
2026-05-12 20:57:54 | INFO |   "action": "tap",
2026-05-12 20:57:54 | INFO |   "region": 3,
2026-05-12 20:57:54 | INFO |   "description": "Tap the plus button to add a new recipe."
2026-05-12 20:57:54 | INFO | }
2026-05-12 20:57:54 | INFO | ```
2026-05-12 20:58:10 | INFO | 🎯 Using region index: 3 at (964, 1741)UserWarning: torch.utils.checkpoint: the use_reentrant parameter should be passed explicitly. Starting in PyTorch 2.9, calling checkpoint without use_reentrant will raise an exception. use_reentrant=False is recommended, but if you need to preserve the current default behavior, you can pass use_reentrant=True. Refer to docs for more details on the differences between the two variants.
2026-05-12 20:58:10 | INFO | UserWarning: None of the inputs have requires_grad=True. Gradients will be None
2026-05-12 20:58:14 | INFO | FutureWarning: `torch.cuda.amp.autocast(args...)` is deprecated. Please use `torch.amp.autocast('cuda', args...)` instead.
2026-05-12 20:58:38 | INFO | 
2026-05-12 20:58:38 | INFO | [1] Tap the plus button to add a new recipe. -> tap
2026-05-12 20:58:38 | INFO | ✅ Action executed.
2026-05-12 20:58:38 | INFO | 
2026-05-12 20:58:38 | INFO | 
2026-05-12 20:58:38 | INFO | 📂 Processing segment 3...
2026-05-12 20:58:38 | INFO | Taking screenshot: /sdcard/screenshot-0.png -> /Users/tanmaybhuskute/Documents/gifdroid-reproduction/apps/bakerspercentagecalculator/llm/ViBR_gemini/screenrec/run-002/artifacts/srv-001/step_3_screenshot-0.png
2026-05-12 20:58:38 | INFO | 🔍 Annotated DINO output saved to /Users/tanmaybhuskute/Documents/gifdroid-reproduction/apps/bakerspercentagecalculator/llm/ViBR_gemini/screenrec/run-002/artifacts/srv-001/step_3_dino.png
2026-05-12 20:58:38 | INFO | /Users/tanmaybhuskute/Documents/gifdroid-reproduction/apps/bakerspercentagecalculator/llm/ViBR_gemini/screenrec/run-002/artifacts/srv-001/step_3_dino.png
2026-05-12 20:58:38 | INFO | /Users/tanmaybhuskute/Documents/gifdroid-reproduction/apps/bakerspercentagecalculator/llm/ViBR_gemini/screenrec/run-002/artifacts/srv-001/step_3_tmp_stop.png
2026-05-12 20:58:38 | INFO | Relevant Region Response from Gemini: ```json
2026-05-12 20:58:38 | INFO | {
2026-05-12 20:58:38 | INFO |   "target_regions": [
2026-05-12 20:58:38 | INFO |     28
2026-05-12 20:58:38 | INFO |   ],
2026-05-12 20:58:38 | INFO |   "predicted_action": "long_press"
2026-05-12 20:58:38 | INFO | }
2026-05-12 20:58:38 | INFO | ```
2026-05-12 20:58:38 | INFO | 🔍 Relevant regions: {'target_regions': [28], 'predicted_action': 'long_press'}
2026-05-12 20:58:38 | INFO | 🧠 GPT selected regions: [28]
2026-05-12 20:58:38 | INFO | ✅ Relevant-only annotation saved to /Users/tanmaybhuskute/Documents/gifdroid-reproduction/apps/bakerspercentagecalculator/llm/ViBR_gemini/screenrec/run-002/artifacts/srv-001/step_3_relevant_regions.png
2026-05-12 20:58:38 | INFO | /Users/tanmaybhuskute/Documents/gifdroid-reproduction/apps/bakerspercentagecalculator/llm/ViBR_gemini/screenrec/run-002/artifacts/srv-001/step_3_relevant_regions.png
2026-05-12 20:58:38 | INFO | /Users/tanmaybhuskute/Documents/gifdroid-reproduction/apps/bakerspercentagecalculator/llm/ViBR_gemini/screenrec/run-002/artifacts/srv-001/step_3_screenshot-0.png
2026-05-12 20:58:38 | INFO | Consistency Response from Gemini: ```json
2026-05-12 20:58:38 | INFO | {
2026-05-12 20:58:38 | INFO |   "same_state": "yes"
2026-05-12 20:58:38 | INFO | }
2026-05-12 20:58:38 | INFO | ```
2026-05-12 20:58:38 | INFO | /Users/tanmaybhuskute/Documents/gifdroid-reproduction/apps/bakerspercentagecalculator/llm/ViBR_gemini/screenrec/run-002/artifacts/srv-001/step_3_relevant_regions.png
2026-05-12 20:58:38 | INFO | /Users/tanmaybhuskute/Documents/gifdroid-reproduction/apps/bakerspercentagecalculator/llm/ViBR_gemini/screenrec/run-002/artifacts/srv-001/step_3_tmp_stop.png
2026-05-12 20:58:38 | INFO | /Users/tanmaybhuskute/Documents/gifdroid-reproduction/apps/bakerspercentagecalculator/llm/ViBR_gemini/screenrec/run-002/artifacts/srv-001/step_3_labeled.png
2026-05-12 20:58:38 | INFO | Region Action Response from Gemini: ```json
2026-05-12 20:58:38 | INFO | {
2026-05-12 20:58:38 | INFO |     "action": "long_press",
2026-05-12 20:58:38 | INFO |     "region": 3,
2026-05-12 20:58:38 | INFO |     "description": "Long press on the Flour text input with current value Flour."
2026-05-12 20:58:38 | INFO | }
2026-05-12 20:58:38 | INFO | ```
2026-05-12 20:58:38 | INFO | 🎯 Using region index: 3 at (361, 634)
2026-05-12 20:58:38 | INFO | [1] Long press on the Flour text input with current value Flour. -> long_press
2026-05-12 20:58:38 | INFO | ✅ Action executed.
2026-05-12 20:58:38 | INFO | 
2026-05-12 20:58:38 | INFO | 
2026-05-12 20:58:38 | INFO | 📂 Processing segment 4...
2026-05-12 20:58:38 | INFO | Taking screenshot: /sdcard/screenshot-0.png -> /Users/tanmaybhuskute/Documents/gifdroid-reproduction/apps/bakerspercentagecalculator/llm/ViBR_gemini/screenrec/run-002/artifacts/srv-001/step_4_screenshot-0.png
2026-05-12 20:58:38 | INFO | 🔍 Annotated DINO output saved to /Users/tanmaybhuskute/Documents/gifdroid-reproduction/apps/bakerspercentagecalculator/llm/ViBR_gemini/screenrec/run-002/artifacts/srv-001/step_4_dino.png
2026-05-12 20:58:38 | INFO | /Users/tanmaybhuskute/Documents/gifdroid-reproduction/apps/bakerspercentagecalculator/llm/ViBR_gemini/screenrec/run-002/artifacts/srv-001/step_4_dino.png
2026-05-12 20:58:38 | INFO | /Users/tanmaybhuskute/Documents/gifdroid-reproduction/apps/bakerspercentagecalculator/llm/ViBR_gemini/screenrec/run-002/artifacts/srv-001/step_4_tmp_stop.png
2026-05-12 20:58:38 | INFO | Relevant Region Response from Gemini: ```json
2026-05-12 20:58:38 | INFO | {
2026-05-12 20:58:38 | INFO |   "target_regions": [
2026-05-12 20:58:38 | INFO |     11
2026-05-12 20:58:38 | INFO |   ],
2026-05-12 20:58:38 | INFO |   "predicted_action": "input_text"
2026-05-12 20:58:38 | INFO | }
2026-05-12 20:58:38 | INFO | ```
2026-05-12 20:58:38 | INFO | 🔍 Relevant regions: {'target_regions': [11], 'predicted_action': 'input_text'}
2026-05-12 20:58:38 | INFO | 🧠 GPT selected regions: [11]
2026-05-12 20:58:38 | INFO | ✅ Relevant-only annotation saved to /Users/tanmaybhuskute/Documents/gifdroid-reproduction/apps/bakerspercentagecalculator/llm/ViBR_gemini/screenrec/run-002/artifacts/srv-001/step_4_relevant_regions.png
2026-05-12 20:58:38 | INFO | /Users/tanmaybhuskute/Documents/gifdroid-reproduction/apps/bakerspercentagecalculator/llm/ViBR_gemini/screenrec/run-002/artifacts/srv-001/step_4_relevant_regions.png
2026-05-12 20:58:38 | INFO | /Users/tanmaybhuskute/Documents/gifdroid-reproduction/apps/bakerspercentagecalculator/llm/ViBR_gemini/screenrec/run-002/artifacts/srv-001/step_4_screenshot-0.png
2026-05-12 20:58:38 | INFO | Consistency Response from Gemini: ```json
2026-05-12 20:58:38 | INFO | {
2026-05-12 20:58:38 | INFO |   "same_state": "yes"
2026-05-12 20:58:38 | INFO | }
2026-05-12 20:58:38 | INFO | ```
2026-05-12 20:58:38 | INFO | /Users/tanmaybhuskute/Documents/gifdroid-reproduction/apps/bakerspercentagecalculator/llm/ViBR_gemini/screenrec/run-002/artifacts/srv-001/step_4_relevant_regions.png
2026-05-12 20:58:38 | INFO | /Users/tanmaybhuskute/Documents/gifdroid-reproduction/apps/bakerspercentagecalculator/llm/ViBR_gemini/screenrec/run-002/artifacts/srv-001/step_4_tmp_stop.png
2026-05-12 20:58:38 | INFO | /Users/tanmaybhuskute/Documents/gifdroid-reproduction/apps/bakerspercentagecalculator/llm/ViBR_gemini/screenrec/run-002/artifacts/srv-001/step_4_labeled.png
2026-05-12 20:58:38 | INFO | Region Action Response from Gemini: ```json
2026-05-12 20:58:38 | INFO | {
2026-05-12 20:58:38 | INFO |   "action": "input_text",
2026-05-12 20:58:38 | INFO |   "text": "n",
2026-05-12 20:58:38 | INFO |   "description": "Type 'n' into the Notes text field, which is labeled as region 7."
2026-05-12 20:58:38 | INFO | }
2026-05-12 20:58:38 | INFO | ```
2026-05-12 20:58:38 | INFO | 🎯 Matched element: 'Recipe Name' at (540, 192)
2026-05-12 20:58:38 | INFO | [1] Type 'n' into the Notes text field, which is labeled as region 7. -> input_text
2026-05-12 20:58:38 | INFO | ✅ Action executed.
2026-05-12 20:58:38 | INFO | 
2026-05-12 20:58:38 | INFO | 
2026-05-12 20:58:38 | INFO | 📂 Processing segment 5...
2026-05-12 20:58:38 | INFO | Taking screenshot: /sdcard/screenshot-0.png -> /Users/tanmaybhuskute/Documents/gifdroid-reproduction/apps/bakerspercentagecalculator/llm/ViBR_gemini/screenrec/run-002/artifacts/srv-001/step_5_screenshot-0.png
2026-05-12 20:58:38 | INFO | 🔍 Annotated DINO output saved to /Users/tanmaybhuskute/Documents/gifdroid-reproduction/apps/bakerspercentagecalculator/llm/ViBR_gemini/screenrec/run-002/artifacts/srv-001/step_5_dino.png
2026-05-12 20:58:38 | INFO | /Users/tanmaybhuskute/Documents/gifdroid-reproduction/apps/bakerspercentagecalculator/llm/ViBR_gemini/screenrec/run-002/artifacts/srv-001/step_5_dino.png
2026-05-12 20:58:38 | INFO | /Users/tanmaybhuskute/Documents/gifdroid-reproduction/apps/bakerspercentagecalculator/llm/ViBR_gemini/screenrec/run-002/artifacts/srv-001/step_5_tmp_stop.png
2026-05-12 20:58:38 | INFO | Relevant Region Response from Gemini: ```json
2026-05-12 20:58:38 | INFO | {
2026-05-12 20:58:38 | INFO |   "target_regions": [
2026-05-12 20:58:38 | INFO |     26
2026-05-12 20:58:38 | INFO |   ],
2026-05-12 20:58:38 | INFO |   "predicted_action": "tap"
2026-05-12 20:58:38 | INFO | }
2026-05-12 20:58:38 | INFO | ```
2026-05-12 20:58:38 | INFO | 🔍 Relevant regions: {'target_regions': [26], 'predicted_action': 'tap'}
2026-05-12 20:58:38 | INFO | 🧠 GPT selected regions: [26]
2026-05-12 20:58:38 | INFO | ✅ Relevant-only annotation saved to /Users/tanmaybhuskute/Documents/gifdroid-reproduction/apps/bakerspercentagecalculator/llm/ViBR_gemini/screenrec/run-002/artifacts/srv-001/step_5_relevant_regions.png
2026-05-12 20:58:38 | INFO | /Users/tanmaybhuskute/Documents/gifdroid-reproduction/apps/bakerspercentagecalculator/llm/ViBR_gemini/screenrec/run-002/artifacts/srv-001/step_5_relevant_regions.png
2026-05-12 20:58:38 | INFO | /Users/tanmaybhuskute/Documents/gifdroid-reproduction/apps/bakerspercentagecalculator/llm/ViBR_gemini/screenrec/run-002/artifacts/srv-001/step_5_screenshot-0.png
2026-05-12 20:58:38 | INFO | Consistency Response from Gemini: ```json
2026-05-12 20:58:38 | INFO | {
2026-05-12 20:58:38 | INFO |   "same_state": "yes"
2026-05-12 20:58:38 | INFO | }
2026-05-12 20:58:38 | INFO | ```
2026-05-12 20:58:38 | INFO | /Users/tanmaybhuskute/Documents/gifdroid-reproduction/apps/bakerspercentagecalculator/llm/ViBR_gemini/screenrec/run-002/artifacts/srv-001/step_5_relevant_regions.png
2026-05-12 20:58:38 | INFO | /Users/tanmaybhuskute/Documents/gifdroid-reproduction/apps/bakerspercentagecalculator/llm/ViBR_gemini/screenrec/run-002/artifacts/srv-001/step_5_tmp_stop.png
2026-05-12 20:58:38 | INFO | /Users/tanmaybhuskute/Documents/gifdroid-reproduction/apps/bakerspercentagecalculator/llm/ViBR_gemini/screenrec/run-002/artifacts/srv-001/step_5_labeled.png
2026-05-12 20:58:38 | INFO | Region Action Response from Gemini: ```json
2026-05-12 20:58:38 | INFO | {
2026-05-12 20:58:38 | INFO |     "action": "tap",
2026-05-12 20:58:38 | INFO |     "region": 3,
2026-05-12 20:58:38 | INFO |     "description": "Tap on the Ingredient Name text field with current value Flour"
2026-05-12 20:58:38 | INFO | }
2026-05-12 20:58:38 | INFO | ```
2026-05-12 20:58:38 | INFO | 🎯 Using region index: 3 at (361, 634)
2026-05-12 20:58:38 | INFO | [1] Tap on the Ingredient Name text field with current value Flour -> tap
2026-05-12 20:58:38 | INFO | ✅ Action executed.
2026-05-12 20:58:38 | INFO | 
2026-05-12 20:58:38 | INFO | 
2026-05-12 20:58:38 | INFO | 📂 Processing segment 6...
2026-05-12 20:58:38 | INFO | Taking screenshot: /sdcard/screenshot-0.png -> /Users/tanmaybhuskute/Documents/gifdroid-reproduction/apps/bakerspercentagecalculator/llm/ViBR_gemini/screenrec/run-002/artifacts/srv-001/step_6_screenshot-0.png
2026-05-12 20:58:38 | INFO | 🔍 Annotated DINO output saved to /Users/tanmaybhuskute/Documents/gifdroid-reproduction/apps/bakerspercentagecalculator/llm/ViBR_gemini/screenrec/run-002/artifacts/srv-001/step_6_dino.png
2026-05-12 20:58:38 | INFO | /Users/tanmaybhuskute/Documents/gifdroid-reproduction/apps/bakerspercentagecalculator/llm/ViBR_gemini/screenrec/run-002/artifacts/srv-001/step_6_dino.png
2026-05-12 20:58:38 | INFO | /Users/tanmaybhuskute/Documents/gifdroid-reproduction/apps/bakerspercentagecalculator/llm/ViBR_gemini/screenrec/run-002/artifacts/srv-001/step_6_tmp_stop.png
2026-05-12 20:58:38 | INFO | Relevant Region Response from Gemini: ```json
2026-05-12 20:58:38 | INFO | {
2026-05-12 20:58:38 | INFO |   "target_regions": [
2026-05-12 20:58:38 | INFO |     5
2026-05-12 20:58:38 | INFO |   ],
2026-05-12 20:58:38 | INFO |   "predicted_action": "tap"
2026-05-12 20:58:38 | INFO | }
2026-05-12 20:58:38 | INFO | ```
2026-05-12 20:58:38 | INFO | 🔍 Relevant regions: {'target_regions': [5], 'predicted_action': 'tap'}
2026-05-12 20:58:38 | INFO | 🧠 GPT selected regions: [5]
2026-05-12 20:58:38 | INFO | ✅ Relevant-only annotation saved to /Users/tanmaybhuskute/Documents/gifdroid-reproduction/apps/bakerspercentagecalculator/llm/ViBR_gemini/screenrec/run-002/artifacts/srv-001/step_6_relevant_regions.png
2026-05-12 20:58:38 | INFO | /Users/tanmaybhuskute/Documents/gifdroid-reproduction/apps/bakerspercentagecalculator/llm/ViBR_gemini/screenrec/run-002/artifacts/srv-001/step_6_relevant_regions.png
2026-05-12 20:58:38 | INFO | /Users/tanmaybhuskute/Documents/gifdroid-reproduction/apps/bakerspercentagecalculator/llm/ViBR_gemini/screenrec/run-002/artifacts/srv-001/step_6_screenshot-0.png
2026-05-12 20:58:38 | INFO | Consistency Response from Gemini: ```json
2026-05-12 20:58:38 | INFO | {
2026-05-12 20:58:38 | INFO |   "same_state": "yes"
2026-05-12 20:58:38 | INFO | }
2026-05-12 20:58:38 | INFO | ```
2026-05-12 20:58:38 | INFO | /Users/tanmaybhuskute/Documents/gifdroid-reproduction/apps/bakerspercentagecalculator/llm/ViBR_gemini/screenrec/run-002/artifacts/srv-001/step_6_relevant_regions.png
2026-05-12 20:58:38 | INFO | /Users/tanmaybhuskute/Documents/gifdroid-reproduction/apps/bakerspercentagecalculator/llm/ViBR_gemini/screenrec/run-002/artifacts/srv-001/step_6_tmp_stop.png
2026-05-12 20:58:38 | INFO | /Users/tanmaybhuskute/Documents/gifdroid-reproduction/apps/bakerspercentagecalculator/llm/ViBR_gemini/screenrec/run-002/artifacts/srv-001/step_6_labeled.png
2026-05-12 20:58:38 | INFO | Region Action Response from Gemini: ```json
2026-05-12 20:58:38 | INFO | {
2026-05-12 20:58:38 | INFO |   "action": "tap",
2026-05-12 20:58:38 | INFO |   "region": 8,
2026-05-12 20:58:38 | INFO |   "description": "Tap the Oven Temp & Time text input."
2026-05-12 20:58:38 | INFO | }
2026-05-12 20:58:38 | INFO | ```
2026-05-12 20:58:38 | INFO | 🎯 Using region index: 8 at (540, 1285)
2026-05-12 20:58:38 | INFO | [1] Tap the Oven Temp & Time text input. -> tap
2026-05-12 20:58:38 | INFO | ✅ Action executed.
2026-05-12 20:58:38 | INFO | 
2026-05-12 20:58:38 | INFO | 
2026-05-12 20:58:38 | INFO | 📂 Processing segment 7...
2026-05-12 20:58:38 | INFO | Taking screenshot: /sdcard/screenshot-0.png -> /Users/tanmaybhuskute/Documents/gifdroid-reproduction/apps/bakerspercentagecalculator/llm/ViBR_gemini/screenrec/run-002/artifacts/srv-001/step_7_screenshot-0.png
2026-05-12 20:58:38 | INFO | 🔍 Annotated DINO output saved to /Users/tanmaybhuskute/Documents/gifdroid-reproduction/apps/bakerspercentagecalculator/llm/ViBR_gemini/screenrec/run-002/artifacts/srv-001/step_7_dino.png
2026-05-12 20:58:38 | INFO | /Users/tanmaybhuskute/Documents/gifdroid-reproduction/apps/bakerspercentagecalculator/llm/ViBR_gemini/screenrec/run-002/artifacts/srv-001/step_7_dino.png
2026-05-12 20:58:38 | INFO | /Users/tanmaybhuskute/Documents/gifdroid-reproduction/apps/bakerspercentagecalculator/llm/ViBR_gemini/screenrec/run-002/artifacts/srv-001/step_7_tmp_stop.png
2026-05-12 20:58:38 | INFO | Relevant Region Response from Gemini: ```json
2026-05-12 20:58:38 | INFO | {
2026-05-12 20:58:38 | INFO |   "target_regions": [
2026-05-12 20:58:38 | INFO |     27
2026-05-12 20:58:38 | INFO |   ],
2026-05-12 20:58:38 | INFO |   "predicted_action": "tap"
2026-05-12 20:58:38 | INFO | }
2026-05-12 20:58:38 | INFO | ```
2026-05-12 20:58:38 | INFO | 🔍 Relevant regions: {'target_regions': [27], 'predicted_action': 'tap'}
2026-05-12 20:58:38 | INFO | 🧠 GPT selected regions: [27]
2026-05-12 20:58:38 | INFO | ✅ Relevant-only annotation saved to /Users/tanmaybhuskute/Documents/gifdroid-reproduction/apps/bakerspercentagecalculator/llm/ViBR_gemini/screenrec/run-002/artifacts/srv-001/step_7_relevant_regions.png
2026-05-12 20:58:38 | INFO | /Users/tanmaybhuskute/Documents/gifdroid-reproduction/apps/bakerspercentagecalculator/llm/ViBR_gemini/screenrec/run-002/artifacts/srv-001/step_7_relevant_regions.png
2026-05-12 20:58:38 | INFO | /Users/tanmaybhuskute/Documents/gifdroid-reproduction/apps/bakerspercentagecalculator/llm/ViBR_gemini/screenrec/run-002/artifacts/srv-001/step_7_screenshot-0.png
2026-05-12 20:58:38 | INFO | Consistency Response from Gemini: ```json
2026-05-12 20:58:38 | INFO | {
2026-05-12 20:58:38 | INFO |   "same_state": "yes"
2026-05-12 20:58:38 | INFO | }
2026-05-12 20:58:38 | INFO | ```
2026-05-12 20:58:38 | INFO | /Users/tanmaybhuskute/Documents/gifdroid-reproduction/apps/bakerspercentagecalculator/llm/ViBR_gemini/screenrec/run-002/artifacts/srv-001/step_7_relevant_regions.png
2026-05-12 20:58:38 | INFO | /Users/tanmaybhuskute/Documents/gifdroid-reproduction/apps/bakerspercentagecalculator/llm/ViBR_gemini/screenrec/run-002/artifacts/srv-001/step_7_tmp_stop.png
2026-05-12 20:58:38 | INFO | /Users/tanmaybhuskute/Documents/gifdroid-reproduction/apps/bakerspercentagecalculator/llm/ViBR_gemini/screenrec/run-002/artifacts/srv-001/step_7_labeled.png
2026-05-12 20:58:38 | INFO | Region Action Response from Gemini: ```json
2026-05-12 20:58:38 | INFO | {
2026-05-12 20:58:38 | INFO |   "action": "tap",
2026-05-12 20:58:38 | INFO |   "region": 8,
2026-05-12 20:58:38 | INFO |   "description": "Tap on the 'Oven Temp & Time' input field."
2026-05-12 20:58:38 | INFO | }
2026-05-12 20:58:38 | INFO | ```
2026-05-12 20:58:38 | INFO | 🎯 Using region index: 8 at (540, 1285)
2026-05-12 20:58:38 | INFO | [1] Tap on the 'Oven Temp & Time' input field. -> tap
2026-05-12 20:58:38 | INFO | ✅ Action executed.
2026-05-12 20:58:38 | INFO | 
2026-05-12 20:58:38 | INFO | ✅ Video processing completed.
2026-05-12 20:58:38 | INFO | 📝 Summary saved to /Users/tanmaybhuskute/Documents/gifdroid-reproduction/apps/bakerspercentagecalculator/llm/ViBR_gemini/screenrec/run-002/artifacts/srv-001/memory.md
2026-05-12 20:58:39 | INFO | ========================================================================
RUN SUMMARY
  App         : bakerspercentagecalculator
  Video type  : screenrec
  Status      : success
  Scenes      : 8/8
  Actions     : unknown=8
  LLM calls   : action_inference=9  region_detection=8  state_comparison=9
  LLM latency : min=4.5s  max=25.6s  avg=9.3s  total=241.7s
  Tokens used : prompt=25,169  output=836  total=26,005
  Wall time   : 5m 38s
========================================================================

```
