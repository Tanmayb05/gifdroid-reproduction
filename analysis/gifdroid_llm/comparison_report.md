# Gemini 2.5 Pro vs Flash Trace Comparison (AdAway)

## Scope
- App: `AdAway`
- UTGs: `utg-01`, `utg-02`, `utg-03`
- Sources: `handheld` (hhv-001), `screenrec` (srv-001)
- Models: `gemini-2-5-pro` vs `gemini-2-5-flash`
- Pair count: 6

## Aggregate
- pair_count: `6`
- avg_sequence_similarity_action_types: `0.2083`
- avg_aligned_action_type_match_rate: `0.1972`
- avg_aligned_target_token_jaccard: `0.1491`
- avg_aligned_details_token_jaccard: `0.0519`
- avg_aligned_screen_desc_token_jaccard: `0.0455`
- avg_pro_quality_proxy: `0.8545`
- avg_flash_quality_proxy: `0.7088`
- wins_by_quality_proxy: `{'pro': 5, 'flash': 1, 'tie': 0}`
- avg_pro_generic_step_rate: `0.0208`
- avg_flash_generic_step_rate: `0.3569`
- avg_pro_fallback_step_rate: `0.0`
- avg_flash_fallback_step_rate: `0.0`

## Pairwise Highlights
- utg-01 / handheld: winner=pro, seq_sim=0.3333, pro_q=0.8417, flash_q=0.3997, pro_generic=0.0, flash_generic=0.8667, pro_fallback=0.0, flash_fallback=0.0
- utg-01 / screenrec: winner=pro, seq_sim=0.125, pro_q=0.8013, flash_q=0.5588, pro_generic=0.125, flash_generic=0.75, pro_fallback=0.0, flash_fallback=0.0
- utg-02 / handheld: winner=pro, seq_sim=0.4, pro_q=0.8717, flash_q=0.811, pro_generic=0.0, flash_generic=0.1333, pro_fallback=0.0, flash_fallback=0.0
- utg-02 / screenrec: winner=flash, seq_sim=0.125, pro_q=0.8631, flash_q=0.92, pro_generic=0.0, flash_generic=0.125, pro_fallback=0.0, flash_fallback=0.0
- utg-03 / handheld: winner=pro, seq_sim=0.2667, pro_q=0.8607, flash_q=0.7263, pro_generic=0.0, flash_generic=0.2667, pro_fallback=0.0, flash_fallback=0.0
- utg-03 / screenrec: winner=pro, seq_sim=0.0, pro_q=0.8887, flash_q=0.8369, pro_generic=0.0, flash_generic=0.0, pro_fallback=0.0, flash_fallback=0.0

## Cross-Source Robustness (HHV vs SRV within UTG)
- utg-01 / pro: similarity=0.1739 (hhv_steps=15, srv_steps=8)
- utg-01 / flash: similarity=0.087 (hhv_steps=15, srv_steps=8)
- utg-02 / pro: similarity=0.1739 (hhv_steps=15, srv_steps=8)
- utg-02 / flash: similarity=0.1739 (hhv_steps=15, srv_steps=8)
- utg-03 / pro: similarity=0.2609 (hhv_steps=15, srv_steps=8)
- utg-03 / flash: similarity=0.0 (hhv_steps=15, srv_steps=8)

## Cross-UTG Stability (within source)
- handheld / pro: mean_pairwise_similarity=0.7333
- handheld / flash: mean_pairwise_similarity=0.3555
- screenrec / pro: mean_pairwise_similarity=0.4167
- screenrec / flash: mean_pairwise_similarity=0.0833

## Top Disagreements (first 20)
- utg-01 / handheld step 1: pro=`launch` vs flash=`None`
- utg-01 / handheld step 3: pro=`type` vs flash=`Screen transition`
- utg-01 / handheld step 4: pro=`tap` vs flash=`Scroll`
- utg-01 / handheld step 6: pro=`tap` vs flash=`Screen transition`
- utg-01 / handheld step 8: pro=`tap` vs flash=`Screen transition`
- utg-01 / handheld step 9: pro=`tap` vs flash=`Screen transition`
- utg-01 / handheld step 10: pro=`swipe` vs flash=`Complex interaction / Animation`
- utg-01 / handheld step 12: pro=`tap` vs flash=`Screen transition`
- utg-01 / handheld step 13: pro=`tap` vs flash=`Screen transition`
- utg-01 / handheld step 14: pro=`type` vs flash=`Scroll`
- utg-01 / screenrec step 1: pro=`TAP` vs flash=`App Launched`
- utg-01 / screenrec step 3: pro=`WAIT` vs flash=`Screen Transition / Load`
- utg-01 / screenrec step 4: pro=`launch_app` vs flash=`Observe`
- utg-01 / screenrec step 5: pro=`launch_app` vs flash=`Observe`
- utg-01 / screenrec step 6: pro=`launch_app` vs flash=`Observe`
- utg-01 / screenrec step 7: pro=`launch_app` vs flash=`Tap / Interact`
- utg-01 / screenrec step 8: pro=`launch_app` vs flash=`Observe / Bug Manifested`
- utg-02 / handheld step 1: pro=`START` vs flash=`App Launch`
- utg-02 / handheld step 3: pro=`TYPE` vs flash=`Scroll`
- utg-02 / handheld step 7: pro=`TAP` vs flash=`Scroll`