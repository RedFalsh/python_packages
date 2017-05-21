# python_packages
常用的一些python包，自己写的，以及github上面的包


- [colorprint](#colorprint)

- [pyqt5_stylesheet](#pyqt5_stylesheet)


## git python_packages

`git clone https://github.com/RedFalsh/python_packages.git`

colorprint
----

- install:

    `cd colorprint`

    `sudo python setup.py install`

- use:

    ```
    from colorprint import colorprint
    cl = colorprint()
    print(cl.red('this is a red print test '))
    ```

pyqt5_stylesheet
----

- install:

    `cd colorprint`

    `sudo python setup.py install`

- use:

    ```
    import PyQt5_stylesheets
    app = QtGui.QApplication().instance()

    # PyQt5
    app.setStyleSheet(PyQt5_stylesheets.load_stylesheet_pyqt5(style="style_black"))
    ```





