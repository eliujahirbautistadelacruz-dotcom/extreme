name: Alertas Extreme Automaticas
on:
  schedule:
    - cron: '*/5 * * * *' # Se ejecuta cada 5 minutos automáticamente
  workflow_dispatch:      # Esto agrega un botón en GitHub para probarlo manualmente

jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v2
      
      - name: Configurar Python
        uses: actions/setup-python@v2
        with:
          python-version: '3.9'
          
      - name: Instalar dependencias
        run: pip install firebase-admin requests # Agregamos 'requests' aquí
        
      - name: Ejecutar Monitor
        run: python python/monitor.py