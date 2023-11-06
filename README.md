# Junior Developer in QA_Veeam Software

## Python Veeam-Test Clement Guyonnet 

In order to resolve your test I used python and 4 different libraries : 

<h3>I used <i>OS</i> for different reasons and methods such as :</h3>
	» To browse through files and folders(that will be my main loop to synchronize all the files)<br>
	» To get all the different path for the source one and also the replica<br>
	» To check if the replica path exist <br>
	» To create a folder if necessary 

<h3>I used the <i>SYS</i> library to utlize command lines argument as shwon at the end of the files
</h3>

<h3>I used <i>SHUTIL</i> for two main reasons :</h3>
	» First to delete files or folder if they don't exist in the original folder.<br>
	» Secondly to copy the content of the original folder and past it in the replica one<br>

<h3>I used the <i>time</i> librairy to add the periodic synchronization function by using the .sleep() method.
</h3>

<h3>Finaly I used the <i>datetime</i> library to make the log file a little more readable, allowing you to see when the program has started and finished</h3>

## Start

To start this program run

```bash
  VeeamTest.py (original_folder) (replica_folder) (sync_interval in seconds) (log_file)
```

