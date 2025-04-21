# Custom Export Templates

![GitHub contributors](https://img.shields.io/github/contributors/push2game/custom-export-templates)
![GitHub top language](https://img.shields.io/github/languages/top/push2game/custom-export-templates)
![GitHub repo size](https://img.shields.io/github/repo-size/push2game/custom-export-templates)
![GitHub License](https://img.shields.io/github/license/push2game/custom-export-templates)

> Custom Godot Engine export templates

> [!IMPORTANT]  
> Support Windows, Linux (x86_64), and Android (arm32-v7a, arm64-v8a) platforms.

## What is this?

- This repository contains custom export templates for the [Godot Engine](https://github.com/godotengine/godot).
- These templates are built from the source code of the [Godot Engine](https://github.com/godotengine/godot).

## What changes have been made?

### For release templates

| #   | Flag         | Value              |
| --- | ------------ | ------------------ |
| 1   | `target`     | `template_release` |
| 2   | `production` | `yes`              |
| 3   | `optimize`   | `speed_trace`      |

### For debug templates

| #   | Flag       | Value            |
| --- | ---------- | ---------------- |
| 1   | `target`   | `template_debug` |
| 2   | `dev_mode` | `yes`            |
| 3   | `optimize` | `debug`          |

### For Android templates

| #   | Flag     | Value |
| --- | -------- | ----- |
| 1   | `swappy` | `yes` |

## License

- This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
