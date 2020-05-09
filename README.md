# Porn Download Directory Categoriser (pddcat) 🐈
Organise your all-in-one everything's-a-jumbled-mess downloads directory into different directories based on models' names using regex. Check [functionality example](#functionality-example) below.

Download [the latest release](https://github.com/kittenparry/pddcat/releases/latest), extract its contents and run `make install` to install the program.

## HOW TO ❓
* Set path to your downloads and archive directories by running `-s` & `-d` options.
* Download [curated_list](db/curated_list.txt) by running `-c`, otherwise it doesn't start with much data to work with.
* Then execute it without any parameters and watch your downloads directory untangle!
```
$ ./pddcat -s /path/to/src -d /path/to/dest -c
$ ./pddcat
```

### USAGE
```
$ ./pddcat [-h] [-i] [-l] [-s path] [-d path] [-w] [-ts path] [-td path]
              [-c] [-a name [name ...]]

Organise your all-in-one porn download directory into separate directories by model names.

optional arguments:
  -h, --help            show this help message and exit
  -i, --info            print currently set src/dest directories and exit. can
                        be combined with -w, -ts, -td to display paths with
                        modifiers. terminates the program nonetheless
  -l, --symlink         create symlinks/shortcuts after moving in the source
                        directory

config options:
  -s path, --source path
                        set downloads dir where files are matched & moved from
  -d path, --dest path  set archive dir where directories with model names are
                        created & files moved to

temporary path:
  -w, --working-dir     temporarily source from current working directory. can
                        not be combined with -ts
  -ts path, --temp-src path
                        temporarily move files from a different directory than
                        currently set src. can not be combined with -w
  -td path, --temp-dest path
                        temporarily move files to a different directory than
                        currently set dest

name lists:
  -c, --curated-list    download a list of model names for a quick start
  -a name [name ...], --add name [name ...]
                        add your own model names to a different file. use
                        underscore (_) in place of spaces and use space to
                        separate multiple names. e.g. riley_reid bryci

```

### Contributing to model list
You can comment new names to [topic #9](https://github.com/kittenparry/pddcat/issues/9) or send a pull request to add more model names to [curated list](db/curated_list.txt) that you download with `-c` option.

#### Functionality Example
 * Source is `~/dwn` and destination is `~/arch`
 * `~/dwn/ariana.marie.awards.mp4` --> `~/arch/ariana_marie/ariana.marie.awards.mp4`
 * `~/dwn/bryci_youtube_playlist/` --> `~/arch/bryci/bryci_youtube_playlist/`
 * Meaning into their separate directories based on name.
 * `~/dwn/18.02.25.Lana.Rhoades.And.Jade.Nile.XXX.1080p/` --> `~/arch/lana_rhoades/18.02.25.Lana.Rhoades.And.Jade.Nile.XXX.1080p/`
   * `lana_rhoades` is longer than `jade_nile` in character length and gets checked, matched & moved to first. If using `-l/--symlink` option, second model's !TODO:

### NOTES
An uncorrectable shortcoming is it can't tell the difference between models with different names, for example `Nadya Nabakova` and `Bunny Colby` are the same person with different names/aliases. Depending on the file/directory name, it will put them into separate directories.

### LICENSING
`pddcat` is licensed under GNU General Public License v3.0 (GPL-3.0), see [LICENSE](LICENSE).
