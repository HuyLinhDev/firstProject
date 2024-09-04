from sqlalchemy import MetaData
from sqlalchemy.orm import Session
import pandas as pd
from io import StringIO
from fastapi.responses import StreamingResponse

class CsvService:
    def __init__(self, db: Session):
        self.db = db

    def export_table_to_csv(self, table_name: str):
        try:
            metadata = MetaData()
            metadata.reflect(bind=self.db.bind)  

            df = pd.read_sql_table(table_name, con=self.db.bind)

            output = StringIO()
            df.to_csv(output, index=False)
            output.seek(0)

            return StreamingResponse(
                iter([output.getvalue()]),
                media_type="text/csv",
                headers={"Content-Disposition": f"attachment; filename={table_name}.csv"}
            )
        except Exception as e:
            raise RuntimeError(f"Failed to export table to CSV: {str(e)}")
