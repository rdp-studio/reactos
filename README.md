<p align=center>
  <a href="https://reactos.org/">
    <img alt="ReactOS" src="https://reactos.org/wiki/images/0/02/ReactOS_logo.png">
  </a>
</p>

---

欢迎访问由中国程序员维护的ReactOS源代码！

[官方版本](https://github.com/reactos/reactos)

# 编译

1. 准备RosBE环境 [点击下载Windows版](https://downloads.sourceforge.net/reactos/RosBE-2.2.1.exe)
2. 打开RosBE CMD
3. 执行 `configure.cmd`
4. 执行 `cd output-MinGW-i386`
5. 执行 `ninja all`
6. 等待数小时后，应该可以在output-MinGW-i386文件夹里看到iso文件。