from enum import StrEnum


class EC2Instance(StrEnum):
    SMALL = "ml.m5.xlarge"
    MEDIUM = "ml.p3.2xlarge"
    LARGE = "ml.g5.12xlarge"


class HuggingFaceTask(StrEnum):
    AudioClassification = "audio-classification"
    AutomaticSpeechRecognition = "automatic-speech-recognition"
    Conversational = "conversational"
    DepthEstimation = "depth-estimation"
    DocumentQuestionAnswering = "document-question-answering"
    FeatureExtraction = "feature-extraction"
    FillMask = "fill-mask"
    ImageClassification = "image-classification"
    ImageFeatureExtraction = "image-feature-extraction"
    ImageSegmentation = "image-segmentation"
    ImageToImage = "image-to-image"
    ImageToText = "image-to-text"
    MaskGeneration = "mask-generation"
    ObjectDetection = "object-detection"
    QuestionAnswering = "question-answering"
    Summarization = "summarization"
    TableQuestionAnswering = "table-question-answering"
    Text2TextGeneration = "text2text-generation"
    TextClassification = "text-classification"
    TextGeneration = "text-generation"
    TextToAudio = "text-to-audio"
    TokenClassification = "token-classification"
    Translation = "translation"
    TranslationXXtoYY = "translation_xx_to_yy"
    VideoClassification = "video-classification"
    VisualQuestionAnswering = "visual-question-answering"
    ZeroShotClassification = "zero-shot-classification"
    ZeroShotImageClassification = "zero-shot-image-classification"
    ZeroShotAudioClassification = "zero-shot-audio-classification"
    ZeroShotObjectDetection = "zero-shot-object-detection"


class SagemakerTask(StrEnum):
    AutomaticSpeechRecognition = "asr"
    AudioEmbedding = "audioembedding"
    Classification = "classification"
    Depth2img = "depth2img"
    ExtractiveQuestionAnswering = "eqa"
    FillMask = "fillmask"
    ImageClassification = "ic"
    ImageEmbedding = "icembedding"
    ImageGeneration = "imagegeneration"
    Inpainting = "inpainting"
    ImageSegmentation = "is"
    LLM = "llm"
    NamedEntityRecognition = "ner"
    ObjectDetection = "od"
    Od1 = "od1"
    Regression = "regression"
    SemanticSegmentation = "semseg"
    SentenceSimilarity = "sentencesimilarity"
    SentencePairClassification = "spc"
    Summarization = "summarization"
    TabTransformerClassification = "tabtransformerclassification"
    TabTransformerRegression = "tabtransformerregression"
    TextClassification = "tc"
    TcEmbedding = "tcembedding"
    Text2text = "text2text"
    TextEmbedding = "textembedding"
    TextGeneration = "textgeneration"
    TextGeneration1 = "textgeneration1"
    TextGeneration2 = "textgeneration2"
    TextGenerationJP = "textgenerationjp"
    TextGenerationNeuron = "textgenerationneuron"
    Translation = "translation"
    Txt2img = "txt2img"
    Upscaling = "upscaling"
    ZeroShotTextClassification = "zstc"


AVAILABLE_PIPELINES = ["feature-extraction",
                       "text-classification", "token-classification", "question-answering",
                       "table-question-answering", "fill-mask", "summarization", "translation",
                       "text2text-generation", "text-generation", "zero-shot-classification", "conversational",
                       "image-classification", "translation_XX_to_YY"]
