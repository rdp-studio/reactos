1 stdcall -stub -noname ShellGetUserList(long long long)
2 stdcall -stub -noname ShellStatusHostEnd(long)
3 stdcall -noname ShellIsFriendlyUIActive()
4 stdcall -stub -noname ShellIsSuspendAllowed()
5 stdcall -stub -noname ShellIsRemoteConnectionsEnabled()
6 stdcall -stub -noname ShellEnableFriendlyUI(long)
7 stdcall -stub -noname ShellEnableMultipleUsers(long)
8 stdcall -stub -noname ShellEnableRemoteConnections(long)
9 stdcall -noname ShellTurnOffDialog(ptr)
10 stdcall -stub -noname ShellIsMultipleUsersEnabled()
11 stdcall -stub -noname ShellACPIPowerButtonPressed(long long long)
12 stdcall -stub -noname ShellIsSingleUserNoPassword(wstr wstr)
13 stdcall -stub -noname ShellStatusHostShuttingDown()
14 stdcall -stub -noname ShellNotifyThemeUserChange(long long)
15 stdcall -stub -noname ShellSwitchWhenInteractiveReady(long long)
16 stdcall -noname ShellDimScreen(ptr ptr)
17 stdcall -stub -noname ShellInstallAccountFilterData()
18 stdcall -stub -noname ShellStatusHostBegin(long)
19 stdcall -stub -noname ShellIsUserInteractiveLogonAllowed(long)
20 stdcall -stub -noname ShellSwitchUser(long)
21 stdcall -stub -noname ShellReturnToWelcome(long)
22 stdcall -stub -noname ShellStatusHostPowerEvent()
23 stdcall -stub -noname ShellStartCredentialServer(wstr long long long)
24 stdcall -stub -noname ShellAcquireLogonMutex()
25 stdcall -stub -noname ShellReleaseLogonMutex(long)
26 stdcall -stub -noname ShellSignalShutdown()
27 stdcall -stub -noname ShellStatusHostHide()
28 stdcall -stub -noname ShellStatusHostShow()
@ stdcall ShellShutdownDialog(ptr wstr long)
@ stdcall WlxActivateUserShell(ptr wstr wstr ptr)
@ stdcall WlxDisconnectNotify(ptr)
@ stdcall WlxDisplayLockedNotice(ptr)
@ stdcall WlxDisplaySASNotice(ptr)
@ stdcall WlxDisplayStatusMessage(ptr ptr long wstr wstr)
@ stdcall WlxGetConsoleSwitchCredentials(ptr ptr)
@ stdcall WlxGetStatusMessage(ptr ptr ptr long)
@ stdcall WlxInitialize(wstr ptr ptr ptr ptr)
@ stdcall WlxIsLockOk(ptr)
@ stdcall WlxIsLogoffOk(ptr)
@ stdcall WlxLoggedOnSAS(ptr long ptr)
@ stdcall WlxLoggedOutSAS(ptr long ptr ptr ptr ptr ptr ptr)
@ stdcall WlxLogoff(ptr)
@ stdcall WlxNegotiate(long ptr)
@ stdcall WlxNetworkProviderLoad(ptr ptr)
@ stdcall -stub WlxReconnectNotify(long)
@ stdcall WlxRemoveStatusMessage(ptr)
@ stdcall WlxScreenSaverNotify(ptr ptr)
@ stdcall WlxShutdown(ptr long)
@ stdcall WlxStartApplication(ptr wstr ptr wstr)
@ stdcall WlxWkstaLockedSAS(ptr long)