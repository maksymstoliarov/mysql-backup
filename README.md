# Mysql backup python script

1. Install requirements
```bash
pip install -r requirements.txt
```

2. Copy .env.example to .env
```bash
cp .env.example .env
```

3. Edit .env file with your mysql credentials
```bash
nano .env
```

4. Run the script
```bash
python main.py
```

5. Setup cron
```
0 4 * * * /usr/bin/python3 /path/to/main.py >> /path/to/logs/backup.log 2>&1
```
