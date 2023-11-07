# Junior Developer in QA_Veeam Software

## Python Veeam-Test Clement Guyonnet 

To resolve your test I used Python and 4 different libraries : 

<h4>I used <i>OS</i> for different reasons and methods such as :</h4>
	» To browse through files and folders(that will be my main loop to synchronize all the files)<br>
	» To get all the different paths for the source one and also the replica<br>
	» To check if the replica path exists <br>
	» To create a folder if necessary 

<h4>I used the <i>SYS</i> library to utilize command lines argument as shown at the end of the files
</h4>

<h4>I used <i>SHUTIL</i> for two main reasons :</h4>
	» First delete files or folders if they don't exist in the original folder.<br>
	» Secondly to copy the content of the original folder and past it in the replica one<br>

<h4>I used the <i>time</i> librairy to add the periodic synchronization function by using the .sleep() method.
</h4>

<h4>Finally I used the <i>datetime</i> library to make the log file a little more readable, allowing you to see when the program has started and finished</h4>

## Start

To start this program run

```bash
  VeeamTest.py (original_folder) (replica_folder) (sync_interval in seconds) (log_file)
```

