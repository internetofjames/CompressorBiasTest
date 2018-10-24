INSERT INTO subject (lastName, firstName, email)
VALUES
  ('test', 'flask', 'test@testconfig.com'),
  ('other', 'otherflask', 'other@otherconfig.com');

INSERT INTO question (question_id, answer, subject_id)
VALUES
  ('test title', 'test', '1');