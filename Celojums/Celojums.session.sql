CREATE TABLE marsruti(
    marsruta_id INT PRIMARY KEY,
    valsts VARCHAR(30),
    transports VARCHAR(30),
    ilguma_dienas INT,
    cena INT,
    darbinieka_id  INT NOT NULL,
    CONSTRAINT fk_darbinieka_id FOREIGN KEY (darbinieka_id) REFERENCES darbinieki(darbinieki_id)
);


INSERT INTO marsruti (
    marsruta_id,
    valsts,
    transports,
    ilguma_dienas,
    cena,
    darbinieka_id
  )
VALUES (
    101,
    'Latvia',
    'Bus',
    3,
    200,
    2
  );