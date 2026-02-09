from pathlib import Path

imagens = [".png", ".jpg", ".jpeg", ".gif", ".bmp", ".tiff", ".ico", ".webp"]
documentos = [".pdf", ".doc", ".docx", ".txt", ".xls", ".xlsx", ".ppt", ".pptx"]
instaladores = [".exe", ".msi", ".dmg", ".pkg", ".deb", ".rpm", ".tar", ".zip", ".rar", ".7z"]
dados = [".csv", ".log", ".json", ".md"]
musica = [".mp3", ".wav"]
video = [".mp4", ".avi", ".mkv"]

BASE_DIR = Path.home() / "Downloads"


def _categoria_para_pasta(ext: str) -> Path | None:
    ext = ext.lower()
    if ext in imagens:
        return BASE_DIR / "imagens"
    if ext in documentos:
        return BASE_DIR / "documentos"
    if ext in instaladores:
        return BASE_DIR / "instaladores"
    if ext in dados:
        return BASE_DIR / "dados"
    if ext in musica:
        return BASE_DIR / "musica"
    if ext in video:
        return BASE_DIR / "video"
    return None


def organizar_arquivos() -> None:
    for item in BASE_DIR.iterdir():
        if not item.is_file():
            continue

        pasta_destino = _categoria_para_pasta(item.suffix)
        if pasta_destino is None:
            continue  # extensão não categorizada

        pasta_destino.mkdir(exist_ok=True)

        destino = pasta_destino / item.name
        # Evita sobrescrever arquivos com o mesmo nome
        if destino.exists():
            stem = item.stem
            suffix = item.suffix
            i = 1
            while True:
                novo_destino = pasta_destino / f"{stem}_{i}{suffix}"
                if not novo_destino.exists():
                    destino = novo_destino
                    break
                i += 1

        item.rename(destino)


if __name__ == "__main__":
    print("Iniciando Organizador de Arquivos...")
    try:
        organizar_arquivos()
        print("Concluído com sucesso!")
    except Exception as e:
        print("ERRO:",e)
    finally:
        print("Programa Encerrado.")
