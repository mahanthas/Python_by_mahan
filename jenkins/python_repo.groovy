import groovy.io.FileType

def compilePythonFiles(directory) {
    def dir = new File(directory)
    if (!dir.exists() || !dir.isDirectory()) {
        println "Directory does not exist: $directory"
        return
    }

    dir.eachFileRecurse(FileType.FILES) { file ->
        if (file.name.endsWith('.py')) {
            println "Compiling ${file.name}"
            def process = "python -m py_compile ${file.absolutePath}".execute()
            process.waitFor()
            if (process.exitValue() != 0) {
                println "Failed to compile ${file.name}"
                println process.err.text
            } else {
                println "Successfully compiled ${file.name}"
            }
        }
    }
}

def repoPath = '/c:/MAHAN/Python_by_mahan/jenkins/python_repo'
compilePythonFiles(repoPath)