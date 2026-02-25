# ലഘുവായ ഒരു പൈത്തൺ ഇമേജ് ഉപയോഗിക്കുന്നു
FROM python:3.9-slim

# വർക്കിംഗ് ഡയറക്ടറി സെറ്റ് ചെയ്യുന്നു
WORKDIR /app

# ലൈബ്രറികൾ ഇൻസ്റ്റാൾ ചെയ്യുന്നു
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# കോഡ് കോപ്പി ചെയ്യുന്നു
COPY . .

# സർവീസ് റൺ ചെയ്യേണ്ട പോർട്ട്
EXPOSE 5001

# ആപ്പ് സ്റ്റാർട്ട് ചെയ്യുന്നു
CMD ["python", "app.py"]
