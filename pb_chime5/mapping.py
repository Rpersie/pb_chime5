
Dispatcher = dict

session_to_speakers = Dispatcher({
    'S01': ['P01', 'P02', 'P03', 'P04'],
    'S02': ['P05', 'P06', 'P07', 'P08'],
    'S03': ['P09', 'P10', 'P11', 'P12'],
    'S04': ['P09', 'P10', 'P11', 'P12'],
    'S05': ['P13', 'P14', 'P15', 'P16'],
    'S06': ['P13', 'P14', 'P15', 'P16'],
    'S07': ['P17', 'P18', 'P19', 'P20'],
    'S08': ['P21', 'P22', 'P23', 'P24'],
    'S09': ['P25', 'P26', 'P27', 'P28'],
    'S12': ['P33', 'P34', 'P35', 'P36'],
    'S13': ['P33', 'P34', 'P35', 'P36'],
    'S16': ['P21', 'P22', 'P23', 'P24'],
    'S17': ['P17', 'P18', 'P19', 'P20'],
    'S18': ['P41', 'P42', 'P43', 'P44'],
    'S19': ['P49', 'P50', 'P51', 'P52'],
    'S20': ['P49', 'P50', 'P51', 'P52'],
    'S21': ['P45', 'P46', 'P47', 'P48'],
    'S22': ['P41', 'P42', 'P43', 'P44'],
    'S23': ['P53', 'P54', 'P55', 'P56'],
    'S24': ['P53', 'P54', 'P55', 'P56'],
})

session_to_dataset = Dispatcher({
    'S01': 'eval',
    'S02': 'dev',
    'S03': 'train',
    'S04': 'train',
    'S05': 'train',
    'S06': 'train',
    'S07': 'train',
    'S08': 'train',
    'S09': 'dev',
    'S12': 'train',
    'S13': 'train',
    'S16': 'train',
    'S17': 'train',
    'S18': 'train',
    'S19': 'train',
    'S20': 'train',
    'S21': 'eval',
    'S22': 'train',
    'S23': 'train',
    'S24': 'train'
})

session_to_arrays: dict = Dispatcher({
    'S01': ['U01', 'U02', 'U03', 'U04', 'U05', 'U06'],
    'S02': ['U01', 'U02', 'U03', 'U04', 'U05', 'U06'],
    'S03': ['U01', 'U02', 'U03', 'U04', 'U05', 'U06'],
    'S04': ['U01', 'U02', 'U03', 'U04', 'U05', 'U06'],
    'S05': ['U01', 'U02',        'U04', 'U05', 'U06'],
    'S06': ['U01', 'U02', 'U03', 'U04', 'U05', 'U06'],
    'S07': ['U01', 'U02', 'U03', 'U04', 'U05', 'U06'],
    'S08': ['U01', 'U02', 'U03', 'U04', 'U05', 'U06'],
    'S09': ['U01', 'U02', 'U03', 'U04',        'U06'],
    'S12': ['U01', 'U02', 'U03', 'U04', 'U05', 'U06'],
    'S13': ['U01', 'U02', 'U03', 'U04', 'U05', 'U06'],
    'S16': ['U01', 'U02', 'U03', 'U04', 'U05', 'U06'],
    'S17': ['U01', 'U02', 'U03', 'U04', 'U05', 'U06'],
    'S18': ['U01', 'U02', 'U03', 'U04', 'U05', 'U06'],
    'S19': ['U01', 'U02', 'U03', 'U04', 'U05', 'U06'],
    'S20': ['U01', 'U02', 'U03', 'U04', 'U05', 'U06'],
    'S21': ['U01', 'U02', 'U03', 'U04', 'U05', 'U06'],
    'S22': ['U01', 'U02',        'U04', 'U05', 'U06'],
    'S23': ['U01', 'U02', 'U03', 'U04', 'U05', 'U06'],
    'S24': ['U01', 'U02', 'U03', 'U04', 'U05', 'U06'],
})

session_array_to_num_samples: dict = Dispatcher({
    'S01_U01': 152699840,
    'S01_U02': 152699840,
    'S01_U03': 152699840,
    'S01_U04': 152699840,
    'S01_U05': 152699840,
    'S01_U06': 152699840,
    'S02_P': 142464640,
    'S02_P05': 142464640,
    'S02_P06': 142464640,
    'S02_P07': 142464640,
    'S02_P08': 142464640,
    'S02_U01': 142464640,
    'S02_U02': 142464640,
    'S02_U03': 142464640,
    'S02_U04': 142464640,
    'S02_U05': 142464640,
    'S02_U06': 142464640,
    'S03_P': 126116800,
    'S03_P09': 126116800,
    'S03_P10': 126116800,
    'S03_P11': 126116800,
    'S03_P12': 126116800,
    'S03_U01': 126116800,
    'S03_U02': 126116800,
    'S03_U03': 126116800,
    'S03_U04': 126116800,
    'S03_U05': 126116800,
    'S03_U06': 126116800,
    'S04_P': 143615200,
    'S04_P09': 143615200,
    'S04_P10': 143615200,
    'S04_P11': 143615200,
    'S04_P12': 143615200,
    'S04_U01': 143615200,
    'S04_U02': 143615200,
    'S04_U03': 143615200,
    'S04_U04': 143615200,
    'S04_U05': 143615200,
    'S04_U06': 143615200,
    'S05_P': 145660480,
    'S05_P13': 145660480,
    'S05_P14': 145660480,
    'S05_P15': 145660480,
    'S05_P16': 145660480,
    'S05_U01': 145660480,
    'S05_U02': 145660480,
    'S05_U04': 144414928,
    'S05_U05': 145660480,
    'S05_U06': 145660480,
    'S06_P': 144103520,
    'S06_P13': 144103520,
    'S06_P14': 144103520,
    'S06_P15': 144103520,
    'S06_P16': 144103520,
    'S06_U01': 144103520,
    'S06_U02': 144103520,
    'S06_U03': 144103520,
    'S06_U04': 144103520,
    'S06_U05': 144103520,
    'S06_U06': 144103520,
    'S07_P': 141009280,
    'S07_P17': 141009280,
    'S07_P18': 141009280,
    'S07_P19': 141009280,
    'S07_P20': 141009280,
    'S07_U01': 141009280,
    'S07_U02': 141009280,
    'S07_U03': 141009280,
    'S07_U04': 141009280,
    'S07_U05': 141009280,
    'S07_U06': 141009280,
    'S08_P': 145521280,
    'S08_P21': 145521280,
    'S08_P22': 145521280,
    'S08_P23': 145521280,
    'S08_P24': 145521280,
    'S08_U01': 145521280,
    'S08_U02': 145521280,
    'S08_U03': 145521280,
    'S08_U04': 145521280,
    'S08_U05': 145521280,
    'S08_U06': 145521280,
    'S09_P': 114583520,
    'S09_P25': 114583520,
    'S09_P26': 114583520,
    'S09_P27': 114583520,
    'S09_P28': 114583520,
    'S09_U01': 114583520,
    'S09_U02': 114583520,
    'S09_U03': 114583520,
    'S09_U04': 114583520,
    'S09_U06': 114583520,
    'S12_P': 143421600,
    'S12_P33': 143421600,
    'S12_P34': 143421600,
    'S12_P35': 143421600,
    'S12_P36': 143421600,
    'S12_U01': 143421600,
    'S12_U02': 143421600,
    'S12_U03': 143421600,
    'S12_U04': 143421600,
    'S12_U05': 129600000,
    'S12_U06': 143421600,
    'S13_P': 144170880,
    'S13_P33': 144170880,
    'S13_P34': 144170880,
    'S13_P35': 144170880,
    'S13_P36': 144170880,
    'S13_U01': 144170880,
    'S13_U02': 144170880,
    'S13_U03': 144170880,
    'S13_U04': 144170880,
    'S13_U05': 144170880,
    'S13_U06': 144170880,
    'S16_P': 146221440,
    'S16_P21': 146221440,
    'S16_P22': 146221440,
    'S16_P23': 146221440,
    'S16_P24': 146221440,
    'S16_U01': 146221440,
    'S16_U02': 146221440,
    'S16_U03': 146221440,
    'S16_U04': 146221440,
    'S16_U05': 146221440,
    'S16_U06': 146221440,
    'S17_P': 146177280,
    'S17_P17': 146177280,
    'S17_P18': 146177280,
    'S17_P19': 146177280,
    'S17_P20': 146177280,
    'S17_U01': 146177280,
    'S17_U02': 146177280,
    'S17_U03': 146177280,
    'S17_U04': 146177280,
    'S17_U05': 146177280,
    'S17_U06': 146177280,
    'S18_P': 155882080,
    'S18_P41': 155882080,
    'S18_P42': 155882080,
    'S18_P43': 155882080,
    'S18_P44': 155882080,
    'S18_U01': 155882080,
    'S18_U02': 155882080,
    'S18_U03': 155882080,
    'S18_U04': 155882080,
    'S18_U05': 155882080,
    'S18_U06': 155592867,
    'S19_P': 146522240,
    'S19_P49': 146522240,
    'S19_P50': 146522240,
    'S19_P51': 146522240,
    'S19_P52': 146522240,
    'S19_U01': 146522240,
    'S19_U02': 146522240,
    'S19_U03': 146522240,
    'S19_U04': 146522240,
    'S19_U05': 146522240,
    'S19_U06': 146522240,
    'S20_P': 132542400,
    'S20_P49': 132542400,
    'S20_P50': 132542400,
    'S20_P51': 132542400,
    'S20_P52': 132542400,
    'S20_U01': 132542400,
    'S20_U02': 132542400,
    'S20_U03': 132542400,
    'S20_U04': 132542400,
    'S20_U05': 132542400,
    'S20_U06': 132542400,
    'S21_U01': 147199840,
    'S21_U02': 147199840,
    'S21_U03': 147199840,
    'S21_U04': 147199840,
    'S21_U05': 147199840,
    'S21_U06': 147199840,
    'S22_P': 149503360,
    'S22_P41': 149503360,
    'S22_P42': 149503360,
    'S22_P43': 149503360,
    'S22_P44': 149503360,
    'S22_U01': 149503360,
    'S22_U02': 149503360,
    'S22_U04': 149503360,
    'S22_U05': 149503360,
    'S22_U06': 149503360,
    'S23_P': 171567520,
    'S23_P53': 171567520,
    'S23_P54': 171567520,
    'S23_P55': 171567520,
    'S23_P56': 171567520,
    'S23_U01': 171567520,
    'S23_U02': 171567520,
    'S23_U03': 171567520,
    'S23_U04': 171567520,
    'S23_U05': 171567520,
    'S23_U06': 171567520,
    'S24_P': 150862080,
    'S24_P53': 150862080,
    'S24_P54': 150862080,
    'S24_P55': 150862080,
    'S24_P56': 150862080,
    'S24_U01': 150862080,
    'S24_U02': 150862080,
    'S24_U03': 150862080,
    'S24_U04': 150862080,
    'S24_U05': 150862080,
    'S24_U06': 150862080,
})








