from typing import Dict


def generate_template(template_name: str, props: Dict[str, str]) -> str:
    if template_name == "new-user":
        return f"""
        <!DOCTYPE html>
        <html lang="ro">
        <head>
            <meta charset="UTF-8" />
            <meta name="viewport" content="width=device-width, initial-scale=1.0" />
            <title>Bun venit pe RoBio</title>
        </head>
        <body style="margin: 0; padding: 0; font-family: Arial, sans-serif; background-color: #f4f4f4;">
            <table width="100%" cellpadding="0" cellspacing="0" style="background-color: #f4f4f4; padding: 30px 0;">
                <tr>
                    <td align="center">
                        <table width="600" cellpadding="0" cellspacing="0" style="background-color: #ffffff; padding: 40px; border-radius: 8px; box-shadow: 0 2px 8px rgba(0,0,0,0.1);">
                            <tr>
                                <td style="text-align: center;">
                                    <h1 style="color: #37474F;">👋 Bun venit pe <span style="color: #1976D2;">RoBio</span></h1>
                                    <p style="font-size: 16px; color: #555;">
                                        Salut, <strong>{props.get("username", "utilizator")}</strong>! Ne bucurăm că te-ai alăturat platformei noastre.
                                    </p>
                                    <p style="font-size: 16px; color: #555;">
                                        RoBio este locul în care poveștile familiei tale prind viață. Creează și explorează arborele tău genealogic,
                                        adaugă documente, confirmă informații și contribuie la construirea unei comunități bazate pe memorie, identitate și apartenență.
                                    </p>
                                    <p style="font-size: 16px; color: #555;">
                                        Începe acum prin a-ți verifica adresa de email:
                                    </p>
                                    <a href="{props.get("verify_url", "#")}" target="_blank" style="display: inline-block; margin-top: 20px; background-color: #1976D2; color: white; padding: 12px 24px; border-radius: 5px; text-decoration: none; font-weight: bold;">
                                        Verifică Emailul
                                    </a>
                                    <p style="font-size: 14px; color: #999; margin-top: 30px;">
                                        Dacă nu ai cerut această înregistrare, poți ignora acest mesaj.
                                    </p>
                                </td>
                            </tr>
                        </table>
                        <p style="font-size: 12px; color: #aaa; margin-top: 20px;">
                            © 2025 RoBio. Toate drepturile rezervate.
                        </p>
                    </td>
                </tr>
            </table>
        </body>
        </html>
        """
    return "<p>Șablon necunoscut</p>"
