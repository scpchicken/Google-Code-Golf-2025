# Google-Code-Golf-2025

### Download zip folder submissions from the code tab on Kaggle and extract them

```bash
# purge all & merge submit
./qpms

# check all solutions in folder_name
./check folder_name

# check solution 1 in submission
./check 1

# check solution 1 in folder_name
./check folder_name 1



# purge folder for bad solution and add working ones to golf.json
./purge folder_name

# if you have them as submission_a, submission_b, ...
./purge submission_*



# merge the golf.json folders and submit the shortest solutions
# outputs sheet.txt (google sheet copy paste)
./ms


# manually submit
zip -r submission.zip submission
kaggle competitions submit -c google-code-golf-2025 -f submission.zip -m "pro"
```

