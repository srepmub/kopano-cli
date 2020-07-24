# Kopano-cli

An improved Kopano admin utility built on python-kopano.

Originally part of Kopano Core, it will be removed with the upcoming release (version 10?).

# Usage

    Usage: kopano-cli [options]

    Options:
      -h, --help                              show this help message and exit
      -C FILE, --config=FILE                  load settings from FILE
      -S SOCKET, --server-socket=SOCKET       connect to server SOCKET
      -K FILE, --ssl-key=FILE                 SSL key file
      -Q PASS, --ssl-pass=PASS                SSL key passphrase
      -U NAME, --auth-user=NAME               login as user
      -P PASS, --auth-pass=PASS               login with password
      -g NAME, --group=NAME                   Specify group
      -c NAME, --company=NAME                 Specify company
      -u NAME, --user=NAME                    Specify user
      -s GUID, --store=GUID                   Specify store
      -f PATH, --folder=PATH                  Specify folder
      -V, --version                           show program version
      --debug                                 Debug mode
      --lang=LANG                             Create folders in this language
      --create                                Create object
      --delete                                Delete object

      Listings:
        --list-users                          List users
        --list-groups                         List groups
        --list-companies                      List companies
        --list-stores                         List stores
        --list-orphans                        List orphan stores
        --user-count                          Output user counts

      User/Group attributes:
        --name=NAME                           Name (User/Group)
        --fullname=NAME                       Full name (User)
        --email=NAME                          Email address (User/Group)
        --password=NAME                       Password (User)
        --password-prompt                     Password (prompt) (User)
        --active=YESNO                        User is active (User)
        --add-feature=NAME                    Feature to add (User)
        --remove-feature=NAME                 Feature to remove (User)
        --admin=NAME                          Administrator (User)
        --admin-level=N                       Admin level (User)

      Store and archive:
        --create-store                        Create store
        --unhook-store                        Unhook (public) store
        --unhook-archive                      Unhook archive store
        --hook-store=GUID                     Hook store
        --hook-archive=GUID                   Hook archive store
        --remove-store=GUID                   Remove orphaned store
        --add-permission=NAME                 Permission to add
                                              (member:right1,right2..)
        --remove-permission=NAME              Permission to remove

      Group membership:
        --add-user=NAME                       User to add
        --remove-user=NAME                    User to remove

      Meeting request processing:
        --mr-accept=YESNO                     Auto-accept meeting requests
        --mr-accept-conflicts=YESNO           Auto-accept conflicting meeting
                                              requests
        --mr-accept-recurring=YESNO           Auto-accept recurring meeting
                                              requests
        --mr-process=YESNO                    Auto-process meeting requests

      Send-as and delegations:
        --add-sendas=NAME                     User to add to send-as
        --remove-sendas=NAME                  User to remove from send-as
        --add-delegation=NAME                 Delegation to add
                                              (user:flag1,flag2..)
        --remove-delegation=NAME              Delegation to remove
        --send-only-to-delegates=YESNO        Send meeting requests only to
                                              delegates

      Quota options:
        --quota-override=YESNO                Override server quota limits
        --quota-hard=N                        Hardquota limit in MB
        --quota-soft=N                        Softquota limit in MB
        --quota-warn=N                        Warnquota limit in MB
        --add-companyquota-recipient=NAME     User to add to companyquota
                                              recipients
        --remove-companyquota-recipient=NAME  User to remove from companyquota
                                              recipients
        --add-userquota-recipient=NAME        User to add to userquota recipients
        --remove-userquota-recipient=NAME     User to remove from userquota
                                              recipients

      Out of office options:
        --ooo=YESNO                           Out-of-office is enabled
        --ooo-clear                           Clear Out-of-office settings
        --ooo-subject=NAME                    Out-of-office subject
        --ooo-message=PATH                    Out-of-office message (path to file)
        --ooo-from=DATE                       Out-of-office from date
        --ooo-until=DATE                      Out-of-office until date

      Misc commands:
        --sync                                Synchronize users and groups with
                                              external source
        --clear-cache                         Clear all server caches
        --purge-softdelete=N                  Purge items marked as softdeleted
                                              more than N days ago
        --purge-deferred                      Purge all items in the deferred
                                              update table
        --reset-folder-count                  Reset folder counts

      Remote:
        --add-admin=NAME                      User to add as remote-admin
        --remove-admin=NAME                   User to remove as remote-admin
        --add-view=NAME                       Company to add as remote-viewer of
                                              address book
        --remove-view=NAME                    Company to remove as remote-viewer
                                              of address book
