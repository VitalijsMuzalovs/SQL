#   DROP TABLE perosna;
#   SELECT * FROM persona;

#   UPDATE persona SET pilseta='Rīga'  WHERE id=1;
#   INSERT INTO persona (id,vards,uzvards,pilseta) VALUES (2,'Andrejs','Jansons','Aizpute');

from msilib.schema import ServiceInstall


CREATE TABLE darbinieki(
    darbinieki_id INT not null PRIMARY KEY,
    vards VARCHAR(30),
    uzvards VARCHAR(30),
    personas_kods VARCHAR(12),
    adrese VARCHAR(80),
    talrunis VARCHAR(12),
    amats VARCHAR(30)
);


CREATE TABLE marsruti(
    id INT SERIAL NOT NULL PRIMARY KEY ,
    marsruta_id INT PRIMARY KEY,
    valsts VARCHAR(30),
    transports VARCHAR(30),
    ilguma_dienas INT,
    cena FLOAT(5,2),
    darbinieka_id NOT NULL VARCHAR(30) FOREIGN KEY
    REFERENCES(darbinieka_id)
);

INSERT INTO darbinieki
VALUES (
    1,
    'Vitalijs',
    'Muzalovs',
    '111184-10888',
    'Liepāja,Dzintaru iela 11-1',
    '+37129812855',
    'Operators'
  );

  CREATE TABLE marsruti(
    marsruta_id INT PRIMARY KEY,
    valsts VARCHAR(30),
    transports VARCHAR(30),
    ilguma_dienas INT,
    cena INT,
    darbinieka_id  INT NOT NULL,
    FOREIGN KEY (darbinieka_id)
      REFERENCES darbinieki(darbinieki_id)
);