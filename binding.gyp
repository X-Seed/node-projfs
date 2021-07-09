{
    "targets": [
        {
            "target_name": "NativeExtension",
            "sources": [ "NativeExtension.cc", "functions.cc" ],
            "include_dirs" : [
 	 			"<!(node -e \"require('nan')\")"
			],
            "defines": [ "_UNICODE", "UNICODE" ],
            "libraries": [ 
                "ProjectedFSLib.lib",
                "kernel32.lib",
                "user32.lib",
                "gdi32.lib",
                "winspool.lib",
                "comdlg32.lib",
                "advapi32.lib",
                "shell32.lib",
                "ole32.lib",
                "oleaut32.lib",
                "uuid.lib",
                "odbc32.lib",
                "odbccp32.lib"
            ],
        }
    ],
}