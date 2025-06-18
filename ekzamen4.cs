using System;

abstract class Document
{
    public abstract void Print();

    public void PrepareForPrinting()
    {
        Console.WriteLine("Підготовка документа до друку...");
        Print();
        Console.WriteLine("Документ готовий до друку.\n");
    }
}

class PDFDocument : Document
{
    public override void Print()
    {
        Console.WriteLine("Друк PDF-документа.");
    }
}

class WordDocument : Document
{
    public override void Print()
    {
        Console.WriteLine("Друк Word-документа.");
    }
}

class ExcelDocument : Document
{
    public override void Print()
    {
        Console.WriteLine("Друк Excel-документа.");
    }
}

class DocumentFactory
{
    public static Document CreateDocument(string type)
    {
        switch (type.ToLower())
        {
            case "pdf":
                return new PDFDocument();
            case "word":
                return new WordDocument();
            case "excel":
                return new ExcelDocument();
            default:
                throw new ArgumentException("Невідомий тип документа.");
        }
    }
}

class Program
{
    static void Main()
    {
        Document pdf = DocumentFactory.CreateDocument("pdf");
        Document word = DocumentFactory.CreateDocument("word");
        Document excel = DocumentFactory.CreateDocument("excel");

        pdf.PrepareForPrinting();
        word.PrepareForPrinting();
        excel.PrepareForPrinting();
    }
}
