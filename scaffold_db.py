import os

base_dir = r"C:\Users\Neha\OneDrive\Desktop\SIH\SIH WINNERS\database"
os.makedirs(os.path.join(base_dir, "schema"), exist_ok=True)
os.makedirs(os.path.join(base_dir, "seed"), exist_ok=True)

schema_sql = """
CREATE EXTENSION IF NOT EXISTS postgis;

CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    phone VARCHAR(15) UNIQUE NOT NULL,
    role VARCHAR(20) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE workers (
    id SERIAL PRIMARY KEY,
    user_id INTEGER REFERENCES users(id),
    name VARCHAR(100) NOT NULL,
    coop_id VARCHAR(50) UNIQUE,
    experience_years INTEGER,
    rating DECIMAL(2,1) DEFAULT 5.0,
    is_verified BOOLEAN DEFAULT FALSE,
    is_available BOOLEAN DEFAULT FALSE,
    location geometry(Point, 4326),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE skills (
    id SERIAL PRIMARY KEY,
    name VARCHAR(50) UNIQUE NOT NULL
);

CREATE TABLE worker_skills (
    worker_id INTEGER REFERENCES workers(id),
    skill_id INTEGER REFERENCES skills(id),
    PRIMARY KEY (worker_id, skill_id)
);

CREATE TABLE bookings (
    id SERIAL PRIMARY KEY,
    consumer_id INTEGER REFERENCES users(id),
    worker_id INTEGER REFERENCES workers(id),
    service_type VARCHAR(50),
    status VARCHAR(20) DEFAULT 'REQUESTED',
    address TEXT,
    is_emergency BOOLEAN DEFAULT FALSE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
"""

seed_sql = """
-- Insert Skills
INSERT INTO skills (name) VALUES ('Plumbing'), ('Electrical'), ('Cleaning'), ('Carpentry'), ('Painting');

-- Insert Demo Users
INSERT INTO users (phone, role) VALUES ('9999999999', 'CONSUMER'), ('8888888888', 'WORKER'), ('7777777777', 'WORKER');

-- Insert Verified Workers in Coimbatore (Lat/Lng)
INSERT INTO workers (user_id, name, coop_id, experience_years, rating, is_verified, is_available, location) 
VALUES 
((SELECT id FROM users WHERE phone='8888888888'), 'Ramesh Kumar', 'COOP-001', 8, 4.9, TRUE, TRUE, ST_SetSRID(ST_MakePoint(77.001, 11.016), 4326)),
((SELECT id FROM users WHERE phone='7777777777'), 'Suresh Das', 'COOP-002', 5, 4.6, TRUE, TRUE, ST_SetSRID(ST_MakePoint(76.995, 11.018), 4326));

-- Link Skills
INSERT INTO worker_skills (worker_id, skill_id) VALUES 
(1, (SELECT id FROM skills WHERE name='Plumbing')),
(2, (SELECT id FROM skills WHERE name='Electrical'));
"""

with open(os.path.join(base_dir, "schema", "01_init.sql"), "w") as f:
    f.write(schema_sql)

with open(os.path.join(base_dir, "seed", "02_data.sql"), "w") as f:
    f.write(seed_sql)

print("Database schema and seed scripts created.")
