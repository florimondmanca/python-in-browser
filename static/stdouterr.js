// Define a stdout and stderr function that will output to the page.

class PyConsole {
  write(buffer) {
    if (buffer === "\n") return;
    console.log(buffer);
  }
  flush() {}
}

class PyErrConsole {
  write(buffers) {
    console.error(buffers[0]);
  }
  flush() {}
}
