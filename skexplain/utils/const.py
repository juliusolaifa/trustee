import numpy as np

import rootpath
from skexplain.enums.feature_type import FeatureType

WINE_DATASET_META = {
    "name": "wine",
    "path": "{}/res/dataset/wine.csv".format(rootpath.detect()),
    "has_header": True,
    "delimiter": ";",
    "fields": [
        ("fixed acidity", FeatureType.NUMERICAL, None, False),
        ("volatile acidity", FeatureType.NUMERICAL, None, False),
        ("citric acid", FeatureType.NUMERICAL, None, False),
        ("residual sugar", FeatureType.NUMERICAL, None, False),
        ("chlorides", FeatureType.NUMERICAL, None, False),
        ("free sulfur dioxide", FeatureType.NUMERICAL, None, False),
        ("total sulfur dioxide", FeatureType.NUMERICAL, None, False),
        ("density", FeatureType.NUMERICAL, None, False),
        ("pH", FeatureType.NUMERICAL, None, False),
        ("sulphates", FeatureType.NUMERICAL, None, False),
        ("alcohol", FeatureType.NUMERICAL, None, False),
        ("quality", FeatureType.NUMERICAL, None, True),
    ],
    "type": "regression",
    "url": "https://archive.ics.uci.edu/ml/datasets/wine",
}

DIABETES_DATASET_META = {
    "name": "diabetes",
    "path": "{}/res/dataset/diabetes/diabetic_data.csv".format(rootpath.detect()),
    "has_header": True,
    "delimiter": ",",
    "fields": [
        ("encounter_id", FeatureType.IDENTIFIER, None, False),
        ("patient_nbr", FeatureType.IDENTIFIER, None, False),
        ("race", FeatureType.CATEGORICAL, None, False),
        ("gender", FeatureType.CATEGORICAL, None, False),
        ("age", FeatureType.CATEGORICAL, None, False),
        ("weight", FeatureType.CATEGORICAL, None, False),
        ("admission_type_id", FeatureType.CATEGORICAL, None, False),
        ("discharge_disposition_id", FeatureType.CATEGORICAL, None, False),
        ("admission_source_id", FeatureType.CATEGORICAL, None, False),
        ("time_in_hospital", FeatureType.NUMERICAL, None, False),
        ("payer_code", FeatureType.CATEGORICAL, None, False),
        ("medical_specialty", FeatureType.CATEGORICAL, None, False),
        ("num_lab_procedures", FeatureType.NUMERICAL, None, False),
        ("num_procedures", FeatureType.NUMERICAL, None, False),
        ("num_medications", FeatureType.NUMERICAL, None, False),
        ("number_outpatient", FeatureType.NUMERICAL, None, False),
        ("number_emergency", FeatureType.NUMERICAL, None, False),
        ("number_inpatient", FeatureType.NUMERICAL, None, False),
        ("diag_1", FeatureType.CATEGORICAL, None, False),
        ("diag_2", FeatureType.CATEGORICAL, None, False),
        ("diag_3", FeatureType.CATEGORICAL, None, False),
        ("number_diagnoses", FeatureType.NUMERICAL, None, False),
        ("max_glu_serum", FeatureType.CATEGORICAL, None, False),
        ("A1Cresult", FeatureType.CATEGORICAL, None, False),
        ("metformin", FeatureType.CATEGORICAL, None, False),
        ("repaglinide", FeatureType.CATEGORICAL, None, False),
        ("nateglinide", FeatureType.CATEGORICAL, None, False),
        ("chlorpropamide", FeatureType.CATEGORICAL, None, False),
        ("glimepiride", FeatureType.CATEGORICAL, None, False),
        ("acetohexamide", FeatureType.CATEGORICAL, None, False),
        ("glipizide", FeatureType.CATEGORICAL, None, False),
        ("glyburide", FeatureType.CATEGORICAL, None, False),
        ("tolbutamide", FeatureType.CATEGORICAL, None, False),
        ("pioglitazone", FeatureType.CATEGORICAL, None, False),
        ("rosiglitazone", FeatureType.CATEGORICAL, None, False),
        ("acarbose", FeatureType.CATEGORICAL, None, False),
        ("miglitol", FeatureType.CATEGORICAL, None, False),
        ("troglitazone", FeatureType.CATEGORICAL, None, False),
        ("tolazamide", FeatureType.CATEGORICAL, None, False),
        ("examide", FeatureType.CATEGORICAL, None, False),
        ("citoglipton", FeatureType.CATEGORICAL, None, False),
        ("insulin", FeatureType.CATEGORICAL, None, False),
        ("glyburide-metformin", FeatureType.CATEGORICAL, None, False),
        ("glipizide-metformin", FeatureType.CATEGORICAL, None, False),
        ("glimepiride-pioglitazone", FeatureType.CATEGORICAL, None, False),
        ("metformin-rosiglitazone", FeatureType.CATEGORICAL, None, False),
        ("metformin-pioglitazone", FeatureType.CATEGORICAL, None, False),
        ("change", FeatureType.CATEGORICAL, None, False),
        ("diabetesMed", FeatureType.CATEGORICAL, None, False),
        ("readmitted", FeatureType.CATEGORICAL, None, True),
    ],
    "type": "classification",
    "url": "https://www.kaggle.com/brandao/diabetes?select=diabetic_data.csv",
}

IOT_DATASET_META = {
    "name": "iot",
    "path": "{}/res/dataset/iot/csv_files/16-09-23-labeled.csv".format(
        rootpath.detect()
    ),
    # "path": "{}/res/dataset/iot/csv_files/".format(rootpath.detect()),
    # "is_dir": True,
    "has_header": False,
    "fields": [
        ("Frame Length", FeatureType.NUMERICAL, None, False),
        ("Ethernet Type", FeatureType.NUMERICAL, None, False),
        ("IP Protocol", FeatureType.CATEGORICAL, None, False),
        ("IPv4 Flags", FeatureType.CATEGORICAL, None, False),
        ("IPv6 Next Header", FeatureType.CATEGORICAL, None, False),
        ("IPv6 Option", FeatureType.CATEGORICAL, None, False),
        ("TCP Flags", FeatureType.CATEGORICAL, None, False),
        ("IoT Device Type", FeatureType.CATEGORICAL, None, True),
    ],
    "classes": ["Smart Static", "Sensor", "Audio", "Video", "Other"],
    "converters": {
        1: lambda x: int(x, 16) if x else None,
        3: lambda x: int(x, 16) if x else None,
        6: lambda x: int(x, 16) if x else None,
    },
    "type": "classification",
    "categories": {
        "IP Protocol": [-1, 0, 1, 2, 6, 17, 145, 242],
        "IPv4 Flags": [
            -1,
            0,
            185,
            925,
            8192,
            8377,
            8562,
            8747,
            8932,
            16384,
            48299,
            60692,
        ],
        "IPv6 Next Header": [-1, 0, 6, 17, 44, 58],
        "IPv6 Option": [-1, 1],
        "TCP Flags": [
            -1,
            1,
            2,
            4,
            16,
            17,
            18,
            20,
            24,
            25,
            28,
            47,
            49,
            56,
            82,
            144,
            152,
            153,
            168,
            194,
            210,
            1041,
            2050,
            2051,
            2513,
            3345,
            3610,
        ],
    },
    "url": "https://iotanalytics.unsw.edu.au/iottraces.html",
}

BOSTON_DATASET_META = {
    "name": "boston",
    "path": "{}/res/dataset/boston.csv".format(rootpath.detect()),
    "has_header": True,
    "fields": [
        ("CRIM", FeatureType.NUMERICAL, None, False),
        ("ZN", FeatureType.NUMERICAL, None, False),
        ("INDUS", FeatureType.NUMERICAL, None, False),
        ("CHAS", FeatureType.CATEGORICAL, None, False),
        ("NOX", FeatureType.NUMERICAL, None, False),
        ("RM", FeatureType.NUMERICAL, None, False),
        ("AGE", FeatureType.NUMERICAL, None, False),
        ("DIS", FeatureType.NUMERICAL, None, False),
        ("RAD", FeatureType.NUMERICAL, None, False),
        ("TAX", FeatureType.NUMERICAL, None, False),
        ("PTRATIO", FeatureType.NUMERICAL, None, False),
        ("B", FeatureType.NUMERICAL, None, False),
        ("LSTAT", FeatureType.NUMERICAL, None, False),
        ("MEDV", FeatureType.CATEGORICAL, None, True),
    ],
    "type": "regression",
    "url": "https://www.cs.toronto.edu/~delve/data/boston/bostonDetail.html",
}


def cic_ids_2017_label_converter(label):
    value = -1
    labels = {
        "BENIGN": 0,
        "Bot": 1,
        "DDoS": 2,
        "DoS GoldenEye": 3,
        "DoS Hulk": 4,
        "DoS Slowhttptest": 5,
        "DoS slowloris": 6,
        "FTP-Patator": 7,
        "Heartbleed": 8,
        "Infiltration": 9,
        "PortScan": 10,
        "SSH-Patator": 11,
        "Web Attack Brute Force": 12,
        "Web Attack Sql Injection": 13,
        "Web Attack XSS": 14,
    }

    try:
        value = labels[label.strip()]
    except Exception as err:
        print("Exception", err, label)

    return np.uint8(value)


CIC_IDS_2017_DATASET_META = {
    "name": "cic_ids_2017",
    "path": "{}/res/dataset/CIC-IDS-2017/MachineLearningCVE/".format(rootpath.detect()),
    "is_dir": True,
    "oversampled_path": "{}/res/dataset/CIC-IDS-2017/MachineLearningCVE_OverSampled.csv.zip".format(
        rootpath.detect()
    ),
    "undersampled_path": "{}/res/dataset/CIC-IDS-2017/MachineLearningCVE_UnderSampled.csv".format(
        rootpath.detect()
    ),
    "has_header": True,
    "fields": [
        ("Destination Port", FeatureType.IDENTIFIER, "uint32", False),
        ("Flow Duration", FeatureType.NUMERICAL, "uint32", False),
        ("Total Fwd Packets", FeatureType.NUMERICAL, "uint32", False),
        ("Total Backward Packets", FeatureType.NUMERICAL, "uint32", False),
        ("Total Length of Fwd Packets", FeatureType.NUMERICAL, "uint32", False),
        ("Total Length of Bwd Packets", FeatureType.NUMERICAL, "uint32", False),
        ("Fwd Packet Length Max", FeatureType.NUMERICAL, "uint16", False),
        ("Fwd Packet Length Min", FeatureType.NUMERICAL, "uint16", False),
        ("Fwd Packet Length Mean", FeatureType.NUMERICAL, "float16", False),
        ("Fwd Packet Length Std", FeatureType.NUMERICAL, "float16", False),
        ("Bwd Packet Length Max", FeatureType.NUMERICAL, "uint16", False),
        ("Bwd Packet Length Min", FeatureType.NUMERICAL, "uint16", False),
        ("Bwd Packet Length Mean", FeatureType.NUMERICAL, "float16", False),
        ("Bwd Packet Length Std", FeatureType.NUMERICAL, "float16", False),
        ("Flow Bytes/s", FeatureType.NUMERICAL, "float32", False),
        ("Flow Packets/s", FeatureType.NUMERICAL, "float32", False),
        ("Flow IAT Mean", FeatureType.NUMERICAL, "float32", False),
        ("Flow IAT Std", FeatureType.NUMERICAL, "float32", False),
        ("Flow IAT Max", FeatureType.NUMERICAL, "uint32", False),
        ("Flow IAT Min", FeatureType.NUMERICAL, "uint32", False),
        ("Fwd IAT Total", FeatureType.NUMERICAL, "uint32", False),
        ("Fwd IAT Mean", FeatureType.NUMERICAL, "float32", False),
        ("Fwd IAT Std", FeatureType.NUMERICAL, "float32", False),
        ("Fwd IAT Max", FeatureType.NUMERICAL, "uint32", False),
        ("Fwd IAT Min", FeatureType.NUMERICAL, "uint32", False),
        ("Bwd IAT Total", FeatureType.NUMERICAL, "uint32", False),
        ("Bwd IAT Mean", FeatureType.NUMERICAL, "float32", False),
        ("Bwd IAT Std", FeatureType.NUMERICAL, "float32", False),
        ("Bwd IAT Max", FeatureType.NUMERICAL, "uint32", False),
        ("Bwd IAT Min", FeatureType.NUMERICAL, "uint32", False),
        ("Fwd PSH Flags", FeatureType.CATEGORICAL, "uint8", False),
        ("Bwd PSH Flags", FeatureType.IDENTIFIER, "uint8", False),
        ("Fwd URG Flags", FeatureType.CATEGORICAL, "uint8", False),
        ("Bwd URG Flags", FeatureType.IDENTIFIER, "uint8", False),
        (
            "Fwd Header Length 2",
            FeatureType.IDENTIFIER,
            "uint32",
            False,
        ),  # duplicate column, so ignore it
        ("Bwd Header Length", FeatureType.NUMERICAL, "uint32", False),
        ("Fwd Packets/s", FeatureType.NUMERICAL, "float16", False),
        ("Bwd Packets/s", FeatureType.NUMERICAL, "float16", False),
        ("Min Packet Length", FeatureType.NUMERICAL, "float16", False),
        ("Max Packet Length", FeatureType.NUMERICAL, "float16", False),
        ("Packet Length Mean", FeatureType.NUMERICAL, "float16", False),
        ("Packet Length Std", FeatureType.NUMERICAL, "float16", False),
        ("Packet Length Variance", FeatureType.NUMERICAL, "float32", False),
        ("FIN Flag Count", FeatureType.NUMERICAL, "uint8", False),
        ("SYN Flag Count", FeatureType.NUMERICAL, "uint8", False),
        ("RST Flag Count", FeatureType.NUMERICAL, "uint8", False),
        ("PSH Flag Count", FeatureType.NUMERICAL, "uint8", False),
        ("ACK Flag Count", FeatureType.NUMERICAL, "uint8", False),
        ("URG Flag Count", FeatureType.NUMERICAL, "uint8", False),
        ("CWE Flag Count", FeatureType.NUMERICAL, "uint8", False),
        ("ECE Flag Count", FeatureType.NUMERICAL, "uint8", False),
        ("Down/Up Ratio", FeatureType.NUMERICAL, "float16", False),
        ("Average Packet Size", FeatureType.NUMERICAL, "float16", False),
        ("Avg Fwd Segment Size", FeatureType.NUMERICAL, "float16", False),
        ("Avg Bwd Segment Size", FeatureType.NUMERICAL, "float16", False),
        ("Fwd Header Length", FeatureType.NUMERICAL, "uint32", False),
        ("Fwd Avg Bytes/Bulk", FeatureType.IDENTIFIER, "uint8", False),
        ("Fwd Avg Packets/Bulk", FeatureType.IDENTIFIER, "uint8", False),
        ("Fwd Avg Bulk Rate", FeatureType.IDENTIFIER, "uint8", False),
        ("Bwd Avg Bytes/Bulk", FeatureType.IDENTIFIER, "uint8", False),
        ("Bwd Avg Packets/Bulk", FeatureType.IDENTIFIER, "uint8", False),
        ("Bwd Avg Bulk Rate", FeatureType.IDENTIFIER, "uint8", False),
        ("Subflow Fwd Packets", FeatureType.NUMERICAL, "uint32", False),
        ("Subflow Fwd Bytes", FeatureType.NUMERICAL, "uint32", False),
        ("Subflow Bwd Packets", FeatureType.NUMERICAL, "uint32", False),
        ("Subflow Bwd Bytes", FeatureType.NUMERICAL, "uint32", False),
        ("Init_Win_bytes_forward", FeatureType.NUMERICAL, "uint32", False),
        ("Init_Win_bytes_backward", FeatureType.NUMERICAL, "uint32", False),
        ("act_data_pkt_fwd", FeatureType.NUMERICAL, "uint16", False),
        ("min_seg_size_forward", FeatureType.NUMERICAL, "uint16", False),
        ("Active Mean", FeatureType.NUMERICAL, "float32", False),
        ("Active Std", FeatureType.NUMERICAL, "float32", False),
        ("Active Max", FeatureType.NUMERICAL, "uint32", False),
        ("Active Min", FeatureType.NUMERICAL, "uint32", False),
        ("Idle Mean", FeatureType.NUMERICAL, "float32", False),
        ("Idle Std", FeatureType.NUMERICAL, "float32", False),
        ("Idle Max", FeatureType.NUMERICAL, "uint32", False),
        ("Idle Min", FeatureType.NUMERICAL, "uint32", False),
        ("Label", FeatureType.CATEGORICAL, "uint8", True),
    ],
    "categories": {
        "Fwd PSH Flags": [np.uint8(0), np.uint8(1)],
        # "Bwd PSH Flags": [np.uint8(0)],
        "Fwd URG Flags": [np.uint8(0), np.uint8(1)],
        # "Bwd URG Flags": [np.uint8(0)],
    },
    "classes": [
        "BENIGN",
        "Bot",
        "DDoS",
        "DoS GoldenEye",
        "DoS Hulk",
        "DoS Slowhttptest",
        "DoS slowloris",
        "FTP-Patator",
        "Heartbleed",
        "Infiltration",
        "PortScan",
        "SSH-Patator",
        "Web Attack Brute Force",
        "Web Attack Sql Injection",
        "Web Attack XSS",
    ],
    "converters": {"Label": lambda x: cic_ids_2017_label_converter(x)},
    "type": "classification",
    "url": "https://www.unb.ca/cic/datasets/ids-2017.html",
}


CIC_IDS_2017_HB_DATASET_META = {
    "name": "cic_ids_2017",
    "path": "{}/res/dataset/CIC-IDS-2017-HB/MachineLearningCVE/".format(
        rootpath.detect()
    ),
    "is_dir": True,
    "oversampled_path": "{}/res/dataset/CIC-IDS-2017-HB/MachineLearningCVE_OverSampled.csv.zip".format(
        rootpath.detect()
    ),
    "undersampled_path": "{}/res/dataset/CIC-IDS-2017-HB/MachineLearningCVE_UnderSampled.csv".format(
        rootpath.detect()
    ),
    "has_header": True,
    "fields": CIC_IDS_2017_DATASET_META["fields"],
    "categories": {
        "Fwd PSH Flags": [np.uint8(0), np.uint8(1)],
        # "Bwd PSH Flags": [np.uint8(0)],
        "Fwd URG Flags": [np.uint8(0), np.uint8(1)],
        # "Bwd URG Flags": [np.uint8(0)],
    },
    "classes": ["BENIGN", "Heartbleed"],
    # "classes": ['BENIGN', 'DoS slowloris'],
    "converters": {"Label": lambda x: cic_ids_2017_label_converter(x)},
    "type": "classification",
    "url": "https://www.unb.ca/cic/datasets/ids-2017.html",
}

DOWNLOAD_DATASET_META = {
    "name": "download",
    # "path": "{}/res/dataset/CIC-IDS-2017/MachineLearningCVE/Friday-WorkingHours-Afternoon-DDos.pcap_ISCX.csv".format(rootpath.detect()),
    "path": "{}/res/dataset/download/download.csv".format(rootpath.detect()),
    "is_dir": False,
    "oversampled_path": "{}/res/dataset/CIC-IDS-2017/MachineLearningCVE_OverSampled.csv.zip".format(
        rootpath.detect()
    ),
    "undersampled_path": "{}/res/dataset/CIC-IDS-2017/MachineLearningCVE_UnderSampled.csv".format(
        rootpath.detect()
    ),
    "has_header": True,
    "fields": CIC_IDS_2017_DATASET_META["fields"],
    "categories": {
        "Fwd PSH Flags": [np.uint8(0), np.uint8(1)],
        # "Bwd PSH Flags": [np.uint8(0)],
        "Fwd URG Flags": [np.uint8(0), np.uint8(1)],
        # "Bwd URG Flags": [np.uint8(0)],
    },
    # "classes": ['BENIGN', 'Bot', 'DDoS', 'DoS GoldenEye', 'DoS Hulk', 'DoS Slowhttptest', 'DoS slowloris', 'FTP-Patator', 'Heartbleed', 'Infiltration', 'PortScan', 'SSH-Patator', 'Web Attack Brute Force', 'Web Attack Sql Injection', 'Web Attack XSS'],
    "classes": ["BENIGN", "Heartbleed"],
    "converters": {"Label": lambda x: cic_ids_2017_label_converter(x)},
    "type": "classification",
    "url": "https://www.unb.ca/cic/datasets/ids-2017.html",
}

HEARTBLEED_DATASET_META = {
    "name": "heartbleed",
    "path": "{}/res/dataset/heartbleed/heartbleed.csv".format(rootpath.detect()),
    "is_dir": False,
    "has_header": True,
    "fields": CIC_IDS_2017_DATASET_META["fields"],
    "categories": {
        "Fwd PSH Flags": [np.uint8(0), np.uint8(1)],
        # "Bwd PSH Flags": [np.uint8(0)],
        "Fwd URG Flags": [np.uint8(0), np.uint8(1)],
        # "Bwd URG Flags": [np.uint8(0)],
    },
    # "classes": ['BENIGN', 'Bot', 'DDoS', 'DoS GoldenEye', 'DoS Hulk', 'DoS Slowhttptest', 'DoS slowloris', 'FTP-Patator', 'Heartbleed', 'Infiltration', 'PortScan', 'SSH-Patator', 'Web Attack Brute Force', 'Web Attack Sql Injection', 'Web Attack XSS'],
    "classes": ["BENIGN", "Heartbleed"],
    "converters": {"Label": lambda x: np.uint8(0 if x == "BENIGN" else 1)},
    "type": "classification",
    "url": "https://www.unb.ca/cic/datasets/ids-2017.html",
}


HEARTBLEED_LARGE_DATASET_META = {
    "name": "heartbleed-large",
    "path": "{}/res/dataset/heartbleed-large/heartbleed-large.csv".format(
        rootpath.detect()
    ),
    "is_dir": False,
    "has_header": True,
    "fields": CIC_IDS_2017_DATASET_META["fields"],
    "categories": {
        "Fwd PSH Flags": [np.uint8(0), np.uint8(1)],
        # "Bwd PSH Flags": [np.uint8(0)],
        "Fwd URG Flags": [np.uint8(0), np.uint8(1)],
        # "Bwd URG Flags": [np.uint8(0)],
    },
    # "classes": ['BENIGN', 'Bot', 'DDoS', 'DoS GoldenEye', 'DoS Hulk', 'DoS Slowhttptest', 'DoS slowloris', 'FTP-Patator', 'Heartbleed', 'Infiltration', 'PortScan', 'SSH-Patator', 'Web Attack Brute Force', 'Web Attack Sql Injection', 'Web Attack XSS'],
    "classes": ["BENIGN", "Heartbleed"],
    "converters": {"Label": lambda x: np.uint8(0 if x == "BENIGN" else 1)},
    "type": "classification",
    "url": "https://www.unb.ca/cic/datasets/ids-2017.html",
}


CIC_ALT_DATASET_META = {
    "name": "cic_alt",
    "path": "{}/res/dataset/CIC-IDS-2017-HB/MachineLearningCVE/".format(
        rootpath.detect()
    ),
    "is_dir": True,
    "oversampled_path": "{}/res/dataset/CIC-IDS-2017/MachineLearningCVE_OverSampled.csv.zip".format(
        rootpath.detect()
    ),
    "undersampled_path": "{}/res/dataset/CIC-IDS-2017/MachineLearningCVE_UnderSampled.csv".format(
        rootpath.detect()
    ),
    "has_header": True,
    "fields": CIC_IDS_2017_DATASET_META["fields"],
    "categories": {
        "Fwd PSH Flags": [np.uint8(0), np.uint8(1)],
        # "Bwd PSH Flags": [np.uint8(0)],
        "Fwd URG Flags": [np.uint8(0), np.uint8(1)],
        # "Bwd URG Flags": [np.uint8(0)],
    },
    # "classes": ['BENIGN', 'Bot', 'DDoS', 'DoS GoldenEye', 'DoS Hulk', 'DoS Slowhttptest', 'DoS slowloris', 'FTP-Patator', 'Heartbleed', 'Infiltration', 'PortScan', 'SSH-Patator', 'Web Attack Brute Force', 'Web Attack Sql Injection', 'Web Attack XSS'],
    "classes": ["BENIGN", "ANOMALY"],
    "converters": {"Label": lambda x: np.uint8(0 if x == "BENIGN" else 1)},
    "type": "classification",
    "url": "https://www.unb.ca/cic/datasets/ids-2017.html",
}
