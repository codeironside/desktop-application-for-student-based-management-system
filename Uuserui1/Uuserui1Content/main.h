#ifndef MAIN_H
#define MAIN_H

#include <QMainWindow>
#include <QObject>
#include <QQuickItem>
#include <QSharedDataPointer>
#include <QWidget>

class mainData;

class main : public QObject
{
    Q_OBJECT
    QML_ELEMENT
public:
    explicit main(QObject *parent = nullptr);
    main(const main &);
    main &operator=(const main &);
    ~main();

signals:


private:
    QSharedDataPointer<mainData> data;
};

#endif // MAIN_H
