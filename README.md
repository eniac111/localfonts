# localfonts

Linux packages for open-source fonts with Bulgarian typography, built on the openSUSE Build Service (OBS) in the project [home:blago:localfonts](https://build.opensuse.org/project/show/home:blago:localfonts).

## Install

The [download page](https://software.opensuse.org/download.html?project=home%3Ablago%3Alocalfonts&package=veleka-world-fonts) shows the commands that add the repository on each distribution.

| Font | openSUSE, Fedora | Debian, Ubuntu | Arch | Source |
|---|---|---|---|---|
| Veleka World | `veleka-world-fonts` | `fonts-veleka-world` | `otf-veleka-world` | [eniac111/Veleka](https://github.com/eniac111/Veleka) |

## How this repository works

OBS reads this repository directly: each top-level folder is one OBS package, and a GitHub webhook tells OBS to re-read it after every push.

The fonts are not compiled here. Each font's own repository builds it and publishes a zip with every release. The recipes in each folder turn that zip into distribution packages:

| File | Used for |
|---|---|
| `<name>.spec` | openSUSE, Fedora, Mageia, CentOS |
| `<name>.dsc` and `debian.*` | Debian, Ubuntu (OBS turns `debian.X` into `debian/X`) |
| `PKGBUILD` | Arch |

OBS downloads the zip from the URLs in the spec (the `Source0` line after `#!RemoteAsset`) and in the `PKGBUILD`, and checks it against the checksums there. The Debian build reuses the same zip.

## Updating a font to a new release

1. Get the checksum of the new zip:
   ```sh
   curl -sL https://github.com/eniac111/Veleka/releases/download/v<version>/veleka-world-fonts-<version>.zip | sha256sum
   ```
2. In the font's folder, update:
   - `<name>.spec`: `Version`, the checksum on the `#!RemoteAsset` line, and a new `%changelog` entry
   - `<name>.dsc`: `Version` and the file name in `DEBTRANSFORM-TAR`
   - `debian.changelog`: a new entry at the top
   - `PKGBUILD`: `pkgver` and `sha256sums`
3. Push. OBS downloads the new zip and rebuilds every distribution. If a checksum doesn't match, OBS rejects the download and reports an error for that package.

## Adding a font

Copy an existing folder, rename the folder and its `.spec` and `.dsc` files, and change the names, URLs, version, checksums and descriptions inside. Follow the naming pattern of each distribution: `<name>-fonts` for RPM, `fonts-<name>` for Debian, and `otf-<name>` for Arch. The new folder appears as a package in OBS after the next push.
