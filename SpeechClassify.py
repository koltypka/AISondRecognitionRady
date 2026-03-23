from speechbrain.inference.classifiers import EncoderClassifier

def get_language(audio_path):
    classifier = EncoderClassifier.from_hparams(
        source="speechbrain/lang-id-commonlanguage_ecapa",
        savedir="pretrained_models/lang-id-commonlanguage_ecapa"
    )
    out_prob, score, index, text_lab =classifier.classify_file(audio_path)
    return 'en' if text_lab[0] == 'English' else 'ru'