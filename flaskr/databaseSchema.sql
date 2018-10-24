DROP TABLE IF EXISTS subject;
DROP TABLE IF EXISTS question;
DROP TABLE IF EXISTS survey;

CREATE TABLE subject (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    lastName TEXT NOT NULL,
    firstName TEXT NOT NULL,
    email TEXT UNIQUE NOT NULL
);

CREATE TABLE question (
    question_id TEXT NOT NULL,
    answer TEXT NOT NULL,
    subject_id INTEGER NOT NULL,
    FOREIGN KEY (subject_id) REFERENCES subject (id)
);

CREATE TABLE survey (
    question_name TEXT UNIQUE NOT NULL,
    unprocessedSample TEXT NOT NULL,
    sampleA TEXT NOT NULL,
    sampleB TEXT NOT NULL
);

INSERT INTO survey(question_name, unprocessedSample, sampleA, sampleB) VALUES ("Fairchild_15-20_ElecGtr", "_ElecGtr_unprocessed.wav", "Fairchild_Digital_15-20dB_ElecGtr.wav", "Fairchild_Analog_15-20dB_ElecGtr.wav");
INSERT INTO survey(question_name, unprocessedSample, sampleA, sampleB) VALUES ("Distressor_3-5_ElecGtr", "_ElecGtr_unprocessed.wav", "Distressor_Digital_3-5dB_ElecGtr.wav", "Distressor_Analog_3-5dB_ElecGtr.wav");
INSERT INTO survey(question_name, unprocessedSample, sampleA, sampleB) VALUES ("DBX160_15-20_Vocal", "_Vocal_unprocessed.wav", "DBX160_Analog_15-20dB_Vocal.wav", "DBX160_Digital_15-20dB_Vocal.wav");
INSERT INTO survey(question_name, unprocessedSample, sampleA, sampleB) VALUES ("DBX160_7-10_Bass", "_Bass_unprocessed.wav", "DBX160_Analog_7-10dB_Bass.wav", "DBX160_Digital_7-10dB_Bass.wav");
INSERT INTO survey(question_name, unprocessedSample, sampleA, sampleB) VALUES ("1176LN_3-5_Bass", "_Bass_unprocessed.wav", "1176LN_Digital_3-5dB_Bass.wav", "1176LN_Analog_3-5dB_Bass.wav");
INSERT INTO survey(question_name, unprocessedSample, sampleA, sampleB) VALUES ("LA2A_7-10_Bass", "_Bass_unprocessed.wav", "LA2A_Digital_7-10dB_Bass.wav", "LA2A_Analog_7-10dB_Bass.wav");
INSERT INTO survey(question_name, unprocessedSample, sampleA, sampleB) VALUES ("DBX160_3-5_ElecGtr", "_ElecGtr_unprocessed.wav", "DBX160_Digital_3-5dB_ElecGtr.wav", "DBX160_Analog_3-5dB_ElecGtr.wav");
INSERT INTO survey(question_name, unprocessedSample, sampleA, sampleB) VALUES ("Fairchild_3-5_Vocal", "_Vocal_unprocessed.wav", "Fairchild_Analog_3-5dB_Vocal.wav", "Fairchild_Digital_3-5dB_Vocal.wav");
INSERT INTO survey(question_name, unprocessedSample, sampleA, sampleB) VALUES ("1176LN_3-5_Vocal", "_Vocal_unprocessed.wav", "1176LN_Digital_3-5dB_Vocal.wav", "1176LN_Analog_3-5dB_Vocal.wav");
INSERT INTO survey(question_name, unprocessedSample, sampleA, sampleB) VALUES ("1176LN_7-10_Bass", "_Bass_unprocessed.wav", "1176LN_Digital_7-10dB_Bass.wav", "1176LN_Analog_7-10dB_Bass.wav");
INSERT INTO survey(question_name, unprocessedSample, sampleA, sampleB) VALUES ("LA2A_15-20_Vocal", "_Vocal_unprocessed.wav", "LA2A_Digital_15-20dB_Vocal.wav", "LA2A_Analog_15-20dB_Vocal.wav");
INSERT INTO survey(question_name, unprocessedSample, sampleA, sampleB) VALUES ("Fairchild_15-20_Bass", "_Bass_unprocessed.wav", "Fairchild_Digital_15-20dB_Bass.wav", "Fairchild_Analog_15-20dB_Bass.wav");
INSERT INTO survey(question_name, unprocessedSample, sampleA, sampleB) VALUES ("LA2A_15-20_ElecGtr", "_ElecGtr_unprocessed.wav", "LA2A_Analog_15-20dB_ElecGtr.wav", "LA2A_Digital_15-20dB_ElecGtr.wav");
INSERT INTO survey(question_name, unprocessedSample, sampleA, sampleB) VALUES ("1176LN_7-10_Vocal", "_Vocal_unprocessed.wav", "1176LN_Digital_7-10dB_Vocal.wav", "1176LN_Analog_7-10dB_Vocal.wav");
INSERT INTO survey(question_name, unprocessedSample, sampleA, sampleB) VALUES ("Distressor_15-20_ElecGtr", "_ElecGtr_unprocessed.wav", "Distressor_Analog_15-20dB_ElecGtr.wav", "Distressor_Digital_15-20dB_ElecGtr.wav");
INSERT INTO survey(question_name, unprocessedSample, sampleA, sampleB) VALUES ("Fairchild_15-20_Vocal", "_Vocal_unprocessed.wav", "Fairchild_Digital_15-20dB_Vocal.wav", "Fairchild_Analog_15-20dB_Vocal.wav");
INSERT INTO survey(question_name, unprocessedSample, sampleA, sampleB) VALUES ("DBX160_3-5_Vocal", "_Vocal_unprocessed.wav", "DBX160_Digital_3-5dB_Vocal.wav", "DBX160_Analog_3-5dB_Vocal.wav");
INSERT INTO survey(question_name, unprocessedSample, sampleA, sampleB) VALUES ("LA2A_3-5_Bass", "_Bass_unprocessed.wav", "LA2A_Digital_3-5dB_Bass.wav", "LA2A_Analog_3-5dB_Bass.wav");
INSERT INTO survey(question_name, unprocessedSample, sampleA, sampleB) VALUES ("LA2A_7-10_ElecGtr", "_ElecGtr_unprocessed.wav", "LA2A_Analog_7-10dB_ElecGtr.wav", "LA2A_Digital_7-10dB_ElecGtr.wav");
INSERT INTO survey(question_name, unprocessedSample, sampleA, sampleB) VALUES ("Distressor_7-10_ElecGtr", "_ElecGtr_unprocessed.wav", "Distressor_Analog_7-10dB_ElecGtr.wav", "Distressor_Digital_7-10dB_ElecGtr.wav");
INSERT INTO survey(question_name, unprocessedSample, sampleA, sampleB) VALUES ("Fairchild_3-5_ElecGtr", "_ElecGtr_unprocessed.wav", "Fairchild_Analog_3-5dB_ElecGtr.wav", "Fairchild_Digital_3-5dB_ElecGtr.wav");
INSERT INTO survey(question_name, unprocessedSample, sampleA, sampleB) VALUES ("DBX160_15-20_Bass", "_Bass_unprocessed.wav", "DBX160_Analog_15-20dB_Bass.wav", "DBX160_Digital_15-20dB_Bass.wav");
INSERT INTO survey(question_name, unprocessedSample, sampleA, sampleB) VALUES ("DBX160_7-10_ElecGtr", "_ElecGtr_unprocessed.wav", "DBX160_Digital_7-10dB_ElecGtr.wav", "DBX160_Analog_7-10dB_ElecGtr.wav");
INSERT INTO survey(question_name, unprocessedSample, sampleA, sampleB) VALUES ("1176LN_3-5_ElecGtr", "_ElecGtr_unprocessed.wav", "1176LN_Digital_3-5dB_ElecGtr.wav", "1176LN_Analog_3-5dB_ElecGtr.wav");
INSERT INTO survey(question_name, unprocessedSample, sampleA, sampleB) VALUES ("1176LN_15-20_Vocal", "_Vocal_unprocessed.wav", "1176LN_Analog_15-20dB_Vocal.wav", "1176LN_Digital_15-20dB_Vocal.wav");
INSERT INTO survey(question_name, unprocessedSample, sampleA, sampleB) VALUES ("Fairchild_7-10_Bass", "_Bass_unprocessed.wav", "Fairchild_Analog_7-10dB_Bass.wav", "Fairchild_Digital_7-10dB_Bass.wav");
INSERT INTO survey(question_name, unprocessedSample, sampleA, sampleB) VALUES ("DBX160_15-20_ElecGtr", "_ElecGtr_unprocessed.wav", "DBX160_Analog_15-20dB_ElecGtr.wav", "DBX160_Digital_15-20dB_ElecGtr.wav");
INSERT INTO survey(question_name, unprocessedSample, sampleA, sampleB) VALUES ("LA2A_3-5_ElecGtr", "_ElecGtr_unprocessed.wav", "LA2A_Analog_3-5dB_ElecGtr.wav", "LA2A_Digital_3-5dB_ElecGtr.wav");
INSERT INTO survey(question_name, unprocessedSample, sampleA, sampleB) VALUES ("Distressor_7-10_Vocal", "_Vocal_unprocessed.wav", "Distressor_Analog_7-10dB_Vocal.wav", "Distressor_Digital_7-10dB_Vocal.wav");
INSERT INTO survey(question_name, unprocessedSample, sampleA, sampleB) VALUES ("LA2A_15-20_Bass", "_Bass_unprocessed.wav", "LA2A_Analog_15-20dB_Bass.wav", "LA2A_Digital_15-20dB_Bass.wav");
INSERT INTO survey(question_name, unprocessedSample, sampleA, sampleB) VALUES ("Distressor_7-10_Bass", "_Bass_unprocessed.wav", "Distressor_Digital_7-10dB_Bass.wav", "Distressor_Analog_7-10dB_Bass.wav");
INSERT INTO survey(question_name, unprocessedSample, sampleA, sampleB) VALUES ("1176LN_15-20_Bass", "_Bass_unprocessed.wav", "1176LN_Analog_15-20dB_Bass.wav", "1176LN_Digital_15-20dB_Bass.wav");
INSERT INTO survey(question_name, unprocessedSample, sampleA, sampleB) VALUES ("LA2A_3-5_Vocal", "_Vocal_unprocessed.wav", "LA2A_Analog_3-5dB_Vocal.wav", "LA2A_Digital_3-5dB_Vocal.wav");
INSERT INTO survey(question_name, unprocessedSample, sampleA, sampleB) VALUES ("DBX160_3-5_Bass", "_Bass_unprocessed.wav", "DBX160_Analog_3-5dB_Bass.wav", "DBX160_Digital_3-5dB_Bass.wav");
INSERT INTO survey(question_name, unprocessedSample, sampleA, sampleB) VALUES ("LA2A_7-10_Vocal", "_Vocal_unprocessed.wav", "LA2A_Digital_7-10dB_Vocal.wav", "LA2A_Analog_7-10dB_Vocal.wav");
INSERT INTO survey(question_name, unprocessedSample, sampleA, sampleB) VALUES ("Fairchild_3-5_Bass", "_Bass_unprocessed.wav", "Fairchild_Digital_3-5dB_Bass.wav", "Fairchild_Analog_3-5dB_Bass.wav");
INSERT INTO survey(question_name, unprocessedSample, sampleA, sampleB) VALUES ("Fairchild_7-10_ElecGtr", "_ElecGtr_unprocessed.wav", "Fairchild_Digital_7-10dB_ElecGtr.wav", "Fairchild_Analog_7-10dB_ElecGtr.wav");
INSERT INTO survey(question_name, unprocessedSample, sampleA, sampleB) VALUES ("1176LN_7-10_ElecGtr", "_ElecGtr_unprocessed.wav", "1176LN_Analog_7-10dB_ElecGtr.wav", "1176LN_Digital_7-10dB_ElecGtr.wav");
INSERT INTO survey(question_name, unprocessedSample, sampleA, sampleB) VALUES ("1176LN_15-20_ElecGtr", "_ElecGtr_unprocessed.wav", "1176LN_Analog_15-20dB_ElecGtr.wav", "1176LN_Digital_15-20dB_ElecGtr.wav");
INSERT INTO survey(question_name, unprocessedSample, sampleA, sampleB) VALUES ("Fairchild_7-10_Vocal", "_Vocal_unprocessed.wav", "Fairchild_Analog_7-10dB_Vocal.wav", "Fairchild_Digital_7-10dB_Vocal.wav");
INSERT INTO survey(question_name, unprocessedSample, sampleA, sampleB) VALUES ("Distressor_3-5_Vocal", "_Vocal_unprocessed.wav", "Distressor_Analog_3-5dB_Vocal.wav", "Distressor_Digital_3-5dB_Vocal.wav");
INSERT INTO survey(question_name, unprocessedSample, sampleA, sampleB) VALUES ("Distressor_15-20_Bass", "_Bass_unprocessed.wav", "Distressor_Digital_15-20dB_Bass.wav", "Distressor_Analog_15-20dB_Bass.wav");
INSERT INTO survey(question_name, unprocessedSample, sampleA, sampleB) VALUES ("Distressor_3-5_Bass", "_Bass_unprocessed.wav", "Distressor_Analog_3-5dB_Bass.wav", "Distressor_Digital_3-5dB_Bass.wav");
INSERT INTO survey(question_name, unprocessedSample, sampleA, sampleB) VALUES ("Distressor_15-20_Vocal", "_Vocal_unprocessed.wav", "Distressor_Digital_15-20dB_Vocal.wav", "Distressor_Analog_15-20dB_Vocal.wav");
INSERT INTO survey(question_name, unprocessedSample, sampleA, sampleB) VALUES ("DBX160_7-10_Vocal", "_Vocal_unprocessed.wav", "DBX160_Analog_7-10dB_Vocal.wav", "DBX160_Digital_7-10dB_Vocal.wav");